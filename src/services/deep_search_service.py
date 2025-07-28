# Ficheiro: src/services/deep_search_service.py

import logging
from typing import Dict, Any
from datetime import datetime

# Importa os serviços que serão orquestrados
from .search_manager import search_manager
from .content_extractor import content_extractor

logger = logging.getLogger(__name__)

class DeepSearchService:
    """
    Serviço de busca profunda que orquestra o SearchManager e o ContentExtractor
    para recolher e consolidar informações da web de forma robusta.
    """
    def __init__(self):
        """Inicializa o serviço de busca profunda."""
        logger.info("✅ DeepSearch Service (orquestrador) inicializado.")

    def perform_deep_search(
        self,
        query: str,
        context_data: Dict[str, Any],
        max_results: int = 10
    ) -> str:
        """
        Executa o processo completo de busca profunda:
        1. Obtém URLs relevantes através do SearchManager.
        2. Extrai o conteúdo de cada URL através do ContentExtractor.
        3. Consolida todo o conteúdo num único texto formatado para a IA.
        
        Args:
            query: A consulta de pesquisa principal.
            context_data: Dados adicionais do formulário para dar contexto.
            max_results: O número máximo de resultados de pesquisa a processar.
        
        Returns:
            Uma string formatada com todo o conteúdo recolhido ou uma mensagem de erro.
        """
        logger.info(f"🚀 Iniciando busca profunda orquestrada para: '{query}'")
        
        # --- Passo 1: Obter URLs relevantes ---
        # Chama o search_manager para obter uma lista de links das melhores fontes.
        search_results = search_manager.multi_search(query, max_results=max_results)

        if not search_results:
            logger.warning("A busca profunda não retornou resultados. A análise pode ser limitada.")
            return "A pesquisa na web não encontrou fontes relevantes para a sua consulta. A análise será baseada apenas nos dados fornecidos."

        # --- Passo 2: Extrair conteúdo de cada URL ---
        # Itera sobre os resultados da busca e usa o content_extractor para obter o texto.
        combined_content = f"CONTEXTO DA PESQUISA NA WEB PARA A CONSULTA: '{query}'\n\n"
        pages_processed_count = 0

        for result in search_results:
            url = result.get('url')
            if not url:
                continue
            
            logger.info(f"📄 A extrair conteúdo de: {result.get('title', url)}")
            content = content_extractor.extract_content(url)
            
            # Apenas adiciona o conteúdo se for substancial
            if content and len(content) > 150: # Mínimo de ~30 palavras
                pages_processed_count += 1
                combined_content += f"--- INÍCIO DA FONTE ---\n"
                combined_content += f"Título: {result.get('title', 'Não disponível')}\n"
                combined_content += f"URL: {url}\n"
                combined_content += f"Conteúdo Extraído:\n{content}\n"
                combined_content += f"--- FIM DA FONTE ---\n\n"
        
        if pages_processed_count == 0:
            logger.error("❌ A busca encontrou fontes, mas a extração de conteúdo falhou para todas.")
            return "A pesquisa na web encontrou fontes, mas não foi possível extrair conteúdo detalhado. A análise pode ser limitada."
            
        # --- Passo 3: Adicionar metadados ao relatório final ---
        combined_content += f"--- RESUMO DA PESQUISA ---\n"
        combined_content += f"Data da Pesquisa: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        combined_content += f"Total de Fontes Encontradas: {len(search_results)}\n"
        combined_content += f"Páginas com Conteúdo Relevante Extraído: {pages_processed_count}\n"
        
        logger.info(f"✅ Busca profunda concluída. {pages_processed_count} páginas processadas.")
        return combined_content

# --- Instância Global ---
# Cria uma única instância para ser usada em toda a aplicação.
deep_search_service = DeepSearchService()
