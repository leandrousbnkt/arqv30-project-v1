# Ficheiro: src/services/future_prediction_engine.py

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class FuturePredictionEngine:
    """
    Motor de Predição do Futuro.
    Este serviço utiliza uma base de conhecimento de tendências de mercado para
    fornecer previsões e cenários futuros. Na versão atual, ele seleciona
    tendências relevantes com base no segmento do utilizador. Pode ser expandido
    no futuro para usar modelos de IA preditivos.
    """
    def __init__(self):
        """
        Inicializa o motor e carrega a base de conhecimento de tendências.
        """
        self.trend_database = self._load_trend_database()
        logger.info("✅ Future Prediction Engine inicializado com a base de conhecimento de tendências.")

    def _load_trend_database(self) -> Dict[str, Dict[str, Any]]:
        """
        Define uma base de conhecimento de tendências de mercado globais e tecnológicas.
        """
        return {
            "ia_generativa": {
                "nome": "Inteligência Artificial Generativa",
                "descricao": "A IA que cria conteúdo (texto, imagens, código) irá automatizar tarefas criativas e analíticas, tornando-se uma ferramenta essencial em quase todos os setores.",
                "impacto_esperado": "Disruptivo",
                "timeline": "2024-2027",
                "segmentos_chave": ["produtos digitais", "consultoria", "marketing", "educacao"]
            },
            "hiper_automacao": {
                "nome": "Hiper-Automação",
                "descricao": "A combinação de IA, Machine Learning e RPA (Robotic Process Automation) para automatizar processos de negócios cada vez mais complexos.",
                "impacto_esperado": "Transformacional",
                "timeline": "2024-2030",
                "segmentos_chave": ["e-commerce", "consultoria", "fintech", "saas"]
            },
            "sustentabilidade_esg": {
                "nome": "Sustentabilidade e ESG",
                "descricao": "Os consumidores e investidores exigem cada vez mais que as empresas demonstrem responsabilidade ambiental, social e de governança (ESG).",
                "impacto_esperado": "Obrigatório",
                "timeline": "2024-indefinido",
                "segmentos_chave": ["e-commerce", "consultoria", "qualquer negócio B2C"]
            },
            "economia_da_paixao": {
                "nome": "Economia da Paixão (Passion Economy)",
                "descricao": "Criadores de conteúdo, especialistas e artistas estão a monetizar as suas paixões e a construir negócios em torno de nichos de audiência.",
                "impacto_esperado": "Crescimento Exponencial",
                "timeline": "2024-2028",
                "segmentos_chave": ["produtos digitais", "educacao", "consultoria"]
            },
            "personalizacao_extrema": {
                "nome": "Personalização Extrema",
                "descricao": "Utilizar dados e IA para oferecer produtos, serviços e experiências totalmente personalizados para cada cliente individualmente.",
                "impacto_esperado": "Diferencial Competitivo Crítico",
                "timeline": "2024-2026",
                "segmentos_chave": ["e-commerce", "produtos digitais", "saas"]
            }
        }

    def predict_market_future(self, segmento: str) -> Dict[str, Any]:
        """
        Analisa o segmento de mercado e retorna as tendências futuras mais relevantes.
        
        Args:
            segmento: O segmento de mercado fornecido pelo utilizador.
        
        Returns:
            Um dicionário com as tendências, oportunidades e ameaças previstas.
        """
        logger.info(f"A gerar previsões futuras para o segmento: {segmento}")
        
        relevant_trends = []
        segmento_lower = segmento.lower()

        # Seleciona as tendências mais relevantes para o segmento do utilizador
        for key, trend in self.trend_database.items():
            if any(s in segmento_lower for s in trend["segmentos_chave"]):
                relevant_trends.append(trend)
        
        # Se nenhuma tendência específica for encontrada, retorna as mais genéricas
        if not relevant_trends:
            relevant_trends = [
                self.trend_database["ia_generativa"],
                self.trend_database["hiper_automacao"]
            ]
            
        # Gera oportunidades e ameaças com base nas tendências selecionadas
        opportunities = [
            f"Integrar '{trend['nome']}' para criar novos produtos ou otimizar operações."
            for trend in relevant_trends
        ]
        threats = [
            f"Concorrentes que adotarem '{trend['nome']}' mais rapidamente ganharão uma vantagem competitiva significativa."
            for trend in relevant_trends
        ]

        return {
            "tendencias_relevantes": relevant_trends,
            "oportunidades_identificadas": opportunities,
            "ameacas_potenciais": threats,
            "recomendacao_estrategica": "Focar na adoção gradual das tendências identificadas, começando pela que tem maior impacto no seu modelo de negócio atual."
        }

# --- Instância Global ---
# Cria uma única instância para ser usada em toda a aplicação.
future_prediction_engine = FuturePredictionEngine()
