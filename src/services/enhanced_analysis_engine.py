# Ficheiro: src/services/enhanced_analysis_engine.py

import logging
import json
from typing import Dict, Any, Optional

from .deep_search_service import deep_search_service
from .ai_manager import ai_manager
from .psychological_analysis_engine import psychological_analysis_engine

logger = logging.getLogger(__name__)

class EnhancedAnalysisEngine:
    def __init__(self):
        logger.info("✅ Enhanced Analysis Engine (Modo Psicológico Avançado) inicializado.")

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
# MISSÃO: ANÁLISE DE MERCADO ESTRATÉGICA E PSICOLÓGICA PROFUNDA (NÍVEL MESTRE)

Você é um consultor de negócios de classe mundial especializado em psicologia de vendas e análise comportamental. 
Sua tarefa é gerar um relatório COMPLETO e ACIONÁVEL seguindo ESTRITAMENTE a estrutura JSON abaixo.

## 1. DADOS FORNECIDOS PELO UTILIZADOR:
```json
{json.dumps(user_data, indent=2, ensure_ascii=False)}
```

## 2. CONTEXTO RECOLHIDO DA WEB:
{web_context}

## 3. ESTRUTURA OBRIGATÓRIA DO RELATÓRIO JSON:

{{
  "resumo_executivo": "Parágrafo conciso com principais insights e recomendações estratégicas",
  
  "analise_mercado": {{
    "tamanho_mercado": "Estimativa do tamanho do mercado",
    "principais_tendencias": ["Tendência 1", "Tendência 2", "Tendência 3", "Tendência 4", "Tendência 5"],
    "oportunidades": ["Oportunidade 1", "Oportunidade 2", "Oportunidade 3", "Oportunidade 4"],
    "ameacas": ["Ameaça 1", "Ameaça 2", "Ameaça 3", "Ameaça 4"],
    "nivel_competitividade": "Alto/Médio/Baixo com justificativa"
  }},
  
  "analise_concorrencia": [
    {{
      "nome": "Nome do Concorrente",
      "pontos_fortes": ["Força 1", "Força 2", "Força 3"],
      "pontos_fracos": ["Fraqueza 1", "Fraqueza 2", "Fraqueza 3"],
      "posicionamento": "Como se posiciona no mercado",
      "preco_medio": "Faixa de preço praticada"
    }}
  ],
  
  "estrategia_posicionamento": {{
    "diferenciacao": "Principal diferencial competitivo",
    "proposta_valor_unica": "Proposta de valor única e clara",
    "publico_alvo_primario": "Definição precisa do público principal",
    "mensagem_central": "Mensagem principal para comunicação"
  }},
  
  "avatar_psicologico_profundo": {{
    "perfil_demografico": {{
      "idade_media": "Faixa etária",
      "genero_predominante": "Masculino/Feminino/Misto",
      "escolaridade": "Nível educacional",
      "renda_familiar": "Faixa de renda",
      "localizacao": "Região geográfica principal"
    }},
    "perfil_psicografico": {{
      "arquetipo_dominante": "Arquétipo psicológico principal",
      "nivel_ansiedade": "Alto/Médio/Baixo",
      "orientacao_temporal": "Passado/Presente/Futuro",
      "motivacao_primaria": "Principal motivação",
      "medo_primario": "Principal medo",
      "linguagem_preferida": "Tipo de linguagem que ressoa"
    }},
    "dores_viscerais": [
      "Dor emocional profunda 1",
      "Dor emocional profunda 2", 
      "Dor emocional profunda 3",
      "Dor emocional profunda 4",
      "Dor emocional profunda 5"
    ],
    "desejos_secretos": [
      "Desejo inconfessável 1",
      "Desejo inconfessável 2",
      "Desejo inconfessável 3",
      "Desejo inconfessável 4"
    ],
    "medos_paralisantes": [
      "Medo que impede ação 1",
      "Medo que impede ação 2",
      "Medo que impede ação 3",
      "Medo que impede ação 4"
    ],
    "objecoes_reais": [
      "Objeção real 1",
      "Objeção real 2",
      "Objeção real 3",
      "Objeção real 4",
      "Objeção real 5"
    ],
    "triggers_emocionais": [
      "Gatilho emocional 1",
      "Gatilho emocional 2",
      "Gatilho emocional 3"
    ]
  }},
  
  "drivers_mentais_customizados": [
    {{
      "nome": "Nome Impactante do Driver",
      "categoria": "Emocional/Racional",
      "gatilho_central": "Emoção ou lógica core que ativa",
      "mecanica_psicologica": "Como funciona no cérebro",
      "momento_instalacao": "Quando usar na jornada",
      "roteiro_ativacao": {{
        "pergunta_abertura": "Pergunta que expõe a ferida",
        "historia_analogia": "História ou analogia que ilustra",
        "metafora_visual": "Metáfora que ancora na memória",
        "comando_acao": "Comando que direciona comportamento"
      }},
      "frases_ancoragem": [
        "Frase memorável 1",
        "Frase memorável 2",
        "Frase memorável 3"
      ]
    }}
  ],
  
  "mapeamento_objecoes": {{
    "objecoes_universais": {{
      "tempo": {{
        "probabilidade": "Alta/Média/Baixa",
        "tratamento": "Como neutralizar",
        "script_neutralizacao": "Script específico"
      }},
      "dinheiro": {{
        "probabilidade": "Alta/Média/Baixa", 
        "tratamento": "Como neutralizar",
        "script_neutralizacao": "Script específico"
      }},
      "confianca": {{
        "probabilidade": "Alta/Média/Baixa",
        "tratamento": "Como neutralizar", 
        "script_neutralizacao": "Script específico"
      }}
    }},
    "objecoes_ocultas": {{
      "autossuficiencia": {{
        "probabilidade": "Alta/Média/Baixa",
        "sinais": ["Sinal 1", "Sinal 2"],
        "tratamento": "Como neutralizar"
      }},
      "medo_mudanca": {{
        "probabilidade": "Alta/Média/Baixa",
        "sinais": ["Sinal 1", "Sinal 2"],
        "tratamento": "Como neutralizar"
      }}
    }}
  }},
  
  "arsenal_provas_visuais": [
    {{
      "nome_impactante": "Nome da Prova Visual",
      "conceito_alvo": "Conceito que precisa ser provado",
      "categoria": "Destruidora de Objeção/Criadora de Urgência/Instaladora de Crença",
      "experimento_fisico": {{
        "materiais": ["Material 1", "Material 2"],
        "setup": "Como preparar",
        "execucao": "Passo a passo da demonstração",
        "climax": "Momento do impacto",
        "bridge": "Como conectar com a vida real"
      }},
      "analogia_perfeita": "Assim como X → Na sua vida Y",
      "momento_ideal": "Quando usar na apresentação"
    }}
  ],
  
  "estrategia_pre_pitch": {{
    "sequencia_psicologica": {{
      "fase_despertar": {{
        "duracao_minutos": "5-7",
        "objetivo": "Quebrar padrão e criar consciência",
        "drivers_usar": ["Driver 1", "Driver 2"],
        "tecnicas": ["Técnica 1", "Técnica 2"]
      }},
      "fase_amplificar": {{
        "duracao_minutos": "8-12", 
        "objetivo": "Amplificar desejo e criar tensão",
        "drivers_usar": ["Driver 3", "Driver 4"],
        "tecnicas": ["Técnica 3", "Técnica 4"]
      }},
      "fase_pressionar": {{
        "duracao_minutos": "5-8",
        "objetivo": "Criar urgência e necessidade", 
        "drivers_usar": ["Driver 5", "Driver 6"],
        "tecnicas": ["Técnica 5", "Técnica 6"]
      }},
      "fase_direcionar": {{
        "duracao_minutos": "3-5",
        "objetivo": "Apresentar caminho e forçar decisão",
        "drivers_usar": ["Driver 7"],
        "tecnicas": ["Técnica 7"]
      }}
    }},
    "pontes_transicao": {{
      "emocao_para_logica": "Script de transição",
      "problema_para_solucao": "Script de transição", 
      "urgencia_para_acao": "Script de transição"
    }}
  }},
  
  "plano_acao_90_dias": {{
    "primeiros_30_dias": {{
      "foco": "Foco principal do período",
      "objetivos": ["Objetivo 1", "Objetivo 2", "Objetivo 3"],
      "acoes_especificas": [
        "Ação específica 1",
        "Ação específica 2", 
        "Ação específica 3",
        "Ação específica 4"
      ],
      "metricas": ["Métrica 1", "Métrica 2"]
    }},
    "segundos_30_dias": {{
      "foco": "Foco principal do período",
      "objetivos": ["Objetivo 1", "Objetivo 2", "Objetivo 3"],
      "acoes_especificas": [
        "Ação específica 1",
        "Ação específica 2",
        "Ação específica 3", 
        "Ação específica 4"
      ],
      "metricas": ["Métrica 1", "Métrica 2"]
    }},
    "terceiros_30_dias": {{
      "foco": "Foco principal do período",
      "objetivos": ["Objetivo 1", "Objetivo 2", "Objetivo 3"],
      "acoes_especificas": [
        "Ação específica 1",
        "Ação específica 2",
        "Ação específica 3",
        "Ação específica 4"
      ],
      "metricas": ["Métrica 1", "Métrica 2"]
    }}
  }},
  
  "plano_implementacao": {{
    "cronograma_preparacao": {{
      "2_3_dias_antes": [
        "Atividade preparatória 1",
        "Atividade preparatória 2",
        "Atividade preparatória 3"
      ]
    }},
    "checkpoints_execucao": {{
      "minuto_5": "Primeiro driver instalado",
      "minuto_15": "Primeira prova visual executada", 
      "minuto_30": "Objeções antecipadas",
      "minuto_45": "Pré-pitch iniciado"
    }},
    "metricas_sucesso": {{
      "durante_apresentacao": [
        "Métrica 1",
        "Métrica 2",
        "Métrica 3"
      ],
      "pos_apresentacao": [
        "Métrica 1", 
        "Métrica 2",
        "Métrica 3"
      ]
    }},
    "kit_emergencia": {{
      "objecoes_inesperadas": "Como lidar",
      "falhas_tecnicas": "Plano B",
      "resistencia_alta": "Técnicas de recuperação"
    }}
  }}
}}

**REGRAS CRÍTICAS:**
- A resposta DEVE ser APENAS o JSON válido, começando com {{ e terminando com }}
- NÃO inclua ```json ou qualquer texto antes/depois
- PREENCHA TODAS as seções com conteúdo DETALHADO e ESPECÍFICO
- Use dados REAIS do contexto fornecido
- Seja PROFUNDO e ACIONÁVEL em cada seção
"""
        return prompt

    def generate_comprehensive_analysis(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        logger.info(f"🚀 Iniciando análise psicológica avançada para: {data.get('segmento')}")

        try:
            # Fase 1: Análise Psicológica Profunda
            logger.info("🧠 Executando análise psicológica profunda...")
            psychological_analysis = psychological_analysis_engine.generate_comprehensive_psychological_analysis(data)
            
            # Fase 2: Pesquisa Web Contextual
            logger.info("🔍 Realizando pesquisa web contextual...")
            search_query = self._generate_search_query(data)
            web_context = deep_search_service.perform_deep_search(search_query, data)
            
            # Fase 3: Geração do Relatório Final via IA
            logger.info("🤖 Gerando relatório final integrado...")
            
            # Combina análise psicológica com contexto web
            enhanced_data = data.copy()
            enhanced_data['analise_psicologica'] = psychological_analysis
            
            final_prompt = self._build_final_prompt(enhanced_data, web_context)
            analysis_text = ai_manager.generate_analysis(final_prompt, max_tokens=12000)

            if not analysis_text:
                logger.error("❌ Falha na geração do relatório pela IA.")
                # Retorna análise psicológica como fallback
                return {
                    "status": "partial_success",
                    "message": "Análise psicológica completa, mas falha na geração do relatório final",
                    **psychological_analysis
                }

            # Processa resposta da IA
            json_text = analysis_text.strip()
            if json_text.startswith("```json"):
                json_text = json_text[7:]
            if json_text.endswith("```"):
                json_text = json_text[:-3]
            
            analysis_json = json.loads(json_text)
            
            # Integra análise psicológica detalhada
            if 'avatar_psicologico_profundo' not in analysis_json:
                analysis_json['avatar_psicologico_profundo'] = psychological_analysis['avatar_psicologico_profundo']
            
            if 'drivers_mentais_customizados' not in analysis_json:
                analysis_json['drivers_mentais_customizados'] = psychological_analysis['drivers_mentais_customizados']
                
            if 'arsenal_provas_visuais' not in analysis_json:
                analysis_json['arsenal_provas_visuais'] = psychological_analysis['arsenal_provas_visuais']
            
            logger.info("✅ Análise psicológica avançada concluída com sucesso!")
            return analysis_json
            
        except json.JSONDecodeError:
            logger.error("❌ Resposta da IA não é JSON válido. Retornando análise psicológica.")
            return {
                "status": "fallback_success", 
                "message": "Análise psicológica completa (formato IA inválido)",
                **psychological_analysis
            }
        except Exception as e:
            logger.error(f"❌ Erro na análise: {e}")
            return {
                "error": "Erro na geração da análise",
                "details": str(e)
            }

enhanced_analysis_engine = EnhancedAnalysisEngine()
