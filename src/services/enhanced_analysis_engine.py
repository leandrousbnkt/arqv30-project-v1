# Ficheiro: src/services/enhanced_analysis_engine.py

import logging
import json
from typing import Dict, Any, Optional

from .deep_search_service import deep_search_service
from .ai_manager import ai_manager

logger = logging.getLogger(__name__)

# --- INSTRUÇÕES DOS SEUS ANEXOS INTEGRADAS DIRETAMENTE ---
PROMPT_AVATAR_E_PSICOLOGIA = """
Você é o MESTRE DA PERSUASÃO VISCERAL. Sua missão é realizar uma "Engenharia Reversa Psicológica Profunda". Mergulhe nas DORES MAIS PROFUNDAS e INCONFESSÁVEIS dos leads, nos seus DESEJOS MAIS ARDENTES e SECRETOS, e nas suas OBJEÇÕES MAIS CÍNICAS. Crie um dossiê tão preciso que o utilizador sinta que pode LER A MENTE dos seus leads.
"""

PROMPT_DRIVERS_MENTAIS = """
Você é um Arquiteto de Drivers Mentais. Seu objetivo é projetar 5 a 7 dos drivers mentais mais poderosos (como Ferida Exposta, Custo Invisível, Diagnóstico Brutal, Ambição Expandida, Relógio Psicológico, Método vs Sorte, Decisão Binária) que sejam customizados para o avatar. Para cada driver, crie um NOME, um GATILHO CENTRAL e um ROTEIRO DE ATIVAÇÃO com uma pergunta de abertura e uma analogia.
"""

PROMPT_PROVAS_VISUAIS = """
Você é o DIRETOR SUPREMO DE EXPERIÊNCIAS TRANSFORMADORAS. Sua missão é criar um arsenal de PROVAS VISUAIS que transformem conceitos abstratos em experiências físicas inesquecíveis. Para cada conceito chave (uma dor, um desejo, uma objeção), crie uma PROVA VISUAL com um NOME IMPACTANTE, o CONCEITO-ALVO e um EXPERIMENTO FÍSICO claro que o demonstre.
"""

class EnhancedAnalysisEngine:
    def __init__(self):
        logger.info("✅ Enhanced Analysis Engine (Modo Robusto) inicializado.")

    def _generate_search_query(self, data: Dict[str, Any]) -> str:
        if data.get('query'):
            return data['query']
        
        segmento = data.get('segmento', '')
        produto = data.get('produto', '')
        publico = data.get('publico', '')
        
        query_parts = [
            "análise de mercado", segmento, produto,
            f"para {publico}" if publico else "",
            "tendências Brasil 2025", "oportunidades e desafios"
        ]
        return " ".join(filter(None, query_parts))

    def _build_final_prompt(self, user_data: Dict[str, Any], web_context: str) -> str:
        user_data.pop('query', None)

        prompt = f"""
# MISSÃO: ANÁLISE DE MERCADO ESTRATÉGICA E PSICOLÓGICA (NÍVEL DE ELITE)

Você é um consultor de negócios de classe mundial. A sua tarefa é gerar um relatório acionável e profundo, seguindo ESTRITAMENTE a estrutura JSON abaixo, com base nos dados fornecidos.

## 1. DADOS FORNECIDOS PELO UTILIZADOR:
```json
{json.dumps(user_data, indent=2, ensure_ascii=False)}
```

## 2. CONTEXTO RECOLHIDO DA WEB:
{web_context}

## 3. INSTRUÇÕES PARA A ANÁLISE (OBRIGATÓRIO):

Com base em AMBOS os conjuntos de dados, gere um relatório ESTRITAMENTE no formato JSON abaixo. SEJA PROFUNDO E ESPECÍFICO.

### PARTE A: ANÁLISE DE MERCADO GERAL
- **resumo_executivo**: Um parágrafo conciso com os principais insights e recomendações estratégicas.
- **analise_mercado**: Um objeto com "tamanho_mercado" (estimativa), "principais_tendencias" (lista de 3-5 tendências), "oportunidades" (lista de 3-5 oportunidades) e "ameacas" (lista de 3-5 ameaças).
- **analise_concorrencia**: Uma lista de objetos, cada um com "nome", "pontos_fortes" (lista) e "pontos_fracos" (lista).
- **estrategia_posicionamento**: Um objeto com "diferenciacao" e "proposta_valor_unica".
- **plano_acao_inicial**: Um objeto para os primeiros 90 dias, com chaves para cada fase (ex: "primeiros_30_dias") contendo "foco" e "passos" (lista).

### PARTE B: ANÁLISE PSICOLÓGICA PROFUNDA (Use as instruções abaixo)
- **avatar_psicologico**: {PROMPT_AVATAR_E_PSICOLOGIA} Crie um perfil como um objeto com "dores_secretas" (lista), "desejos_ardentes" (lista), "medos_paralisantes" (lista) e "objecoes_reais" (lista).
- **drivers_mentais**: {PROMPT_DRIVERS_MENTAIS} Crie uma lista de 5 objetos, cada um com "nome", "gatilho_central" e "roteiro_ativacao".
- **provas_visuais**: {PROMPT_PROVAS_VISUAIS} Crie uma lista de 3 objetos, cada um com "nome_impactante", "conceito_alvo" e "experimento".

**REGRAS CRÍTICAS:**
- A resposta DEVE ser um único bloco de código JSON válido, começando com `{{` e terminando com `}}`.
- NÃO inclua nenhum texto, explicação ou ```json antes ou depois do JSON.
- Preencha TODAS as secções com conteúdo detalhado e de alta qualidade.
"""
        return prompt

    def generate_comprehensive_analysis(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        logger.info(f"🚀 A iniciar análise abrangente para o segmento: {data.get('segmento')}")

        search_query = self._generate_search_query(data)
        logger.info(f"🔍 Query de pesquisa definida: '{search_query}'")

        web_context = deep_search_service.perform_deep_search(search_query, data)
        final_prompt = self._build_final_prompt(data, web_context)
        analysis_text = ai_manager.generate_analysis(final_prompt)

        if not analysis_text:
            logger.error("❌ A geração de análise pela IA falhou.")
            return {"error": "Falha na geração da análise. Todos os provedores de IA falharam."}

        try:
            json_text = analysis_text.strip()
            if json_text.startswith("```json"):
                json_text = json_text[7:]
            if json_text.endswith("```"):
                json_text = json_text[:-3]
            
            analysis_json = json.loads(json_text)
            logger.info("✅ Análise abrangente gerada e analisada com sucesso!")
            return analysis_json
        except json.JSONDecodeError:
            logger.error("❌ A IA retornou uma resposta que não é um JSON válido.")
            return {
                "error": "A resposta da IA não estava no formato JSON esperado.",
                "raw_response": analysis_text
            }

enhanced_analysis_engine = EnhancedAnalysisEngine()
