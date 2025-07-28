# Ficheiro: src/services/content_extractor.py

import logging
import requests
import re
from bs4 import BeautifulSoup
from typing import Optional

# Importa a configuração para aceder à chave da ScrapingAnt
from config import Config

logger = logging.getLogger(__name__)

class ContentExtractor:
    """
    Serviço robusto para extrair o conteúdo principal de uma página web.
    Utiliza uma estratégia primária (ScrapingAnt) e um fallback (requisição direta)
    para garantir a máxima chance de sucesso.
    """

    def __init__(self):
        """Inicializa as configurações e a chave de API."""
        self.scrapingant_key = Config.SCRAPINGANT_API_KEY
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        logger.info("✅ Content Extractor inicializado.")

    def _clean_text(self, text: str) -> str:
        """
        Limpa o texto extraído, removendo espaços excessivos, quebras de linha
        e linhas curtas que geralmente correspondem a elementos de navegação.
        """
        if not text:
            return ""
        
        # Remove múltiplas quebras de linha, deixando no máximo duas
        text = re.sub(r'\n\s*\n', '\n\n', text)
        # Remove espaços e tabulações excessivas
        text = re.sub(r'[ \t]+', ' ', text)
        
        lines = (line.strip() for line in text.splitlines())
        # Mantém apenas as linhas com mais de algumas palavras, para focar no conteúdo principal
        meaningful_lines = [line for line in lines if len(line.split()) > 5]
        
        cleaned_text = '\n'.join(meaningful_lines)
        
        # Limita o tamanho final para não sobrecarregar a IA
        return cleaned_text[:15000]

    def _extract_with_scrapingant(self, url: str) -> Optional[str]:
        """
        Estratégia primária: usa a API da ScrapingAnt para obter o HTML,
        evitando bloqueios e lidando com páginas renderizadas por JavaScript.
        """
        if not self.scrapingant_key:
            logger.warning("⚠️ Chave da ScrapingAnt não configurada. A saltar esta estratégia.")
            return None
        
        try:
            api_url = f"https://api.scrapingant.com/v2/general"
            params = {'url': url, 'browser': 'false'} # 'browser': 'true' se precisar de renderização JS
            headers = {'x-api-key': self.scrapingant_key}
            
            response = requests.get(api_url, params=params, headers=headers, timeout=45)
            response.raise_for_status() # Lança um erro para códigos de status ruins (4xx ou 5xx)

            soup = BeautifulSoup(response.content, 'lxml')
            
            # Remove elementos de "ruído" (scripts, estilos, menus, rodapés, etc.)
            for element in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
                element.decompose()
            
            # Tenta encontrar o conteúdo principal da página
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|main|article|post|body'))
            
            text = main_content.get_text(separator='\n', strip=True) if main_content else soup.get_text(separator='\n', strip=True)
            
            logger.info(f"✅ Conteúdo extraído com sucesso de {url} via ScrapingAnt.")
            return self._clean_text(text)

        except requests.RequestException as e:
            logger.warning(f"⚠️ Falha na extração com ScrapingAnt para {url}: {e}")
            return None

    def _extract_direct(self, url: str) -> Optional[str]:
        """
        Estratégia de fallback: faz uma requisição HTTP direta para obter o HTML.
        Pode falhar em sites com proteção contra scraping.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=20)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')
            
            for element in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
                element.decompose()
            
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|main|article|post|body'))
            text = main_content.get_text(separator='\n', strip=True) if main_content else soup.get_text(separator='\n', strip=True)
            
            logger.info(f"✅ Conteúdo extraído com sucesso de {url} via requisição direta.")
            return self._clean_text(text)

        except requests.RequestException as e:
            logger.warning(f"⚠️ Falha na extração direta para {url}: {e}")
            return None

    def extract_content(self, url: str) -> Optional[str]:
        """
        Orquestra a extração de conteúdo, tentando a melhor estratégia primeiro.
        """
        if not url or not url.startswith('http'):
            logger.warning(f"URL inválida fornecida: {url}")
            return None

        logger.info(f"🚀 Iniciando extração de conteúdo para: {url}")
        
        # 1. Tenta a estratégia mais robusta primeiro (ScrapingAnt)
        content = self._extract_with_scrapingant(url)
        
        # 2. Se a primeira falhar, tenta a requisição direta como fallback
        if not content:
            logger.info(f"🔄 ScrapingAnt falhou. A tentar requisição direta como fallback...")
            content = self._extract_direct(url)
        
        if content and len(content) > 100: # Considera sucesso se o conteúdo for substancial
            logger.info(f"✅ Extração de conteúdo para {url} concluída com sucesso.")
            return content
        else:
            logger.error(f"❌ Todas as estratégias de extração falharam para {url}.")
            return None

# --- Instância Global ---
# Cria uma única instância para ser usada em toda a aplicação.
content_extractor = ContentExtractor()
