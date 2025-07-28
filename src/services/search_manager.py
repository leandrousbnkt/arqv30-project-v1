# Ficheiro: src/services/search_manager.py

import logging
import requests
from typing import List, Dict
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# Importa a configuração centralizada para aceder às chaves de API
from config import Config

logger = logging.getLogger(__name__)

class SearchManager:
    """
    Gerenciador de buscas 100% gratuito com sistema de fallback em camadas.
    Prioridade: Jina AI -> Google Custom Search -> ScrapingAnt.
    """
    def __init__(self):
        """Inicializa os URLs das APIs e as chaves a partir da configuração."""
        self.jina_api_url = "https://s.jina.ai/"
        self.google_api_url = "https://www.googleapis.com/customsearch/v1"
        self.scrapingant_api_url = "https://api.scrapingant.com/v2/general"

        # As chaves são lidas de forma segura a partir do objeto Config
        self.google_key = Config.GOOGLE_SEARCH_KEY
        self.google_cx = Config.GOOGLE_CSE_ID
        self.scrapingant_key = Config.SCRAPINGANT_API_KEY
        self.jina_key = Config.JINA_API_KEY # Jina pode usar uma chave para limites mais altos

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        logger.info("✅ Search Manager (versão gratuita) inicializado.")

    def _search_jina(self, query: str) -> List[Dict]:
        """Busca usando Jina AI. Robusto e ideal para extrair conteúdo limpo."""
        try:
            url = f"{self.jina_api_url}{quote_plus(query)}"
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {self.jina_key}"
            }
            response = requests.get(url, headers=headers, timeout=25)
            
            if response.status_code == 200:
                data = response.json().get('data', [])
                results = [
                    {
                        "title": r.get("title", "Sem título"),
                        "url": r.get("url"),
                        "snippet": r.get("description", r.get("content", ""))[:300],
                        "source": "jina"
                    } for r in data if r.get('url')
                ]
                logger.info(f"✅ Jina AI encontrou {len(results)} resultados.")
                return results
        except requests.RequestException as e:
            logger.warning(f"⚠️ Jina AI falhou: {e}")
        return []

    def _search_google_cse(self, query: str, num_results: int) -> List[Dict]:
        """Busca usando Google Custom Search Engine (100/dia grátis)."""
        if not self.google_key or not self.google_cx:
            logger.warning("⚠️ Chaves do Google CSE não configuradas.")
            return []
        try:
            params = {"key": self.google_key, "cx": self.google_cx, "q": query, "num": num_results}
            response = requests.get(self.google_api_url, params=params, timeout=15)
            if response.status_code == 200:
                items = response.json().get("items", [])
                results = [
                    {"title": i.get("title"), "url": i.get("link"), "snippet": i.get("snippet"), "source": "google_cse"}
                    for i in items
                ]
                logger.info(f"✅ Google CSE encontrou {len(results)} resultados.")
                return results
        except requests.RequestException as e:
            logger.warning(f"⚠️ Google CSE falhou: {e}")
        return []

    def _search_scrapingant(self, query: str) -> List[Dict]:
        """Usa ScrapingAnt para fazer scraping da página de resultados do Google como fallback."""
        if not self.scrapingant_key:
            logger.warning("⚠️ Chave da ScrapingAnt não configurada.")
            return []
        try:
            google_search_url = f"https://www.google.com/search?q={quote_plus(query)}&hl=pt-BR"
            params = {'url': google_search_url, 'browser': 'false'}
            headers = {'x-api-key': self.scrapingant_key}
            
            response = requests.get(self.scrapingant_api_url, params=params, headers=headers, timeout=30)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []
                # Procura por divs que contêm os resultados de pesquisa do Google
                for g in soup.find_all('div', class_='g'):
                    a_tag = g.find('a')
                    h3_tag = g.find('h3')
                    snippet_div = g.find('div', style=lambda value: value and 'display: -webkit-box' in value)
                    
                    if a_tag and a_tag.get('href') and h3_tag:
                        results.append({
                            "title": h3_tag.text,
                            "url": a_tag['href'],
                            "snippet": snippet_div.text if snippet_div else "Sem snippet.",
                            "source": "scrapingant_google"
                        })
                logger.info(f"✅ ScrapingAnt encontrou {len(results)} resultados.")
                return results
        except Exception as e:
            logger.warning(f"⚠️ ScrapingAnt falhou: {e}")
        return []

    def multi_search(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Orquestra a busca em múltiplos provedores gratuitos com fallback.
        """
        logger.info(f"🚀 Iniciando multi-busca gratuita para: '{query}'")
        
        # 1. Tenta Jina AI (fonte primária)
        results = self._search_jina(query)

        # 2. Se não houver resultados suficientes, tenta Google CSE
        if len(results) < max_results:
            needed = max_results - len(results)
            results.extend(self._search_google_cse(query, needed))

        # 3. Se ainda não for suficiente, usa o fallback ScrapingAnt
        if len(results) < max_results:
             results.extend(self._search_scrapingant(query))

        # Remove duplicados pela URL e limita os resultados
        seen_urls = set()
        unique_results = []
        for res in results:
            if res.get('url') and res['url'] not in seen_urls:
                seen_urls.add(res['url'])
                unique_results.append(res)
        
        final_results = unique_results[:max_results]
        logger.info(f"✅ Multi-busca concluída. Total de {len(final_results)} resultados únicos.")
        return final_results

# --- Instância Global ---
# Cria uma única instância do SearchManager para ser usada em toda a aplicação.
search_manager = SearchManager()
