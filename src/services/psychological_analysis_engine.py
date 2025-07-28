# Ficheiro: src/services/psychological_analysis_engine.py

import logging
from typing import Dict, Any, List
import json

logger = logging.getLogger(__name__)

class PsychologicalAnalysisEngine:
    """
    Motor de Análise Psicológica Profunda baseado nos documentos anexos.
    Implementa os sistemas de Drivers Mentais, Pré-Pitch Invisível, 
    Engenharia Anti-Objeção e Provas Visuais.
    """
    
    def __init__(self):
        self.drivers_mentais = self._load_drivers_mentais()
        self.objecoes_universais = self._load_objecoes_universais()
        self.provas_visuais = self._load_provas_visuais()
        logger.info("✅ Psychological Analysis Engine inicializado.")

    def _load_drivers_mentais(self) -> Dict[str, Dict[str, Any]]:
        """Carrega os 19 drivers mentais universais do documento anexo."""
        return {
            "ferida_exposta": {
                "nome": "Ferida Exposta",
                "categoria": "Emocional Primário",
                "gatilho": "Dor não resolvida",
                "mecanica": "Trazer à consciência o que foi reprimido",
                "ativacao": "Você ainda [comportamento doloroso] mesmo sabendo que [consequência]?",
                "momento_instalacao": "Abertura - Quebra de padrão"
            },
            "trofeu_secreto": {
                "nome": "Troféu Secreto",
                "categoria": "Emocional Primário",
                "gatilho": "Desejo inconfessável",
                "mecanica": "Validar ambições 'proibidas'",
                "ativacao": "Não é sobre dinheiro, é sobre [desejo real oculto]",
                "momento_instalacao": "Desenvolvimento - Amplificação"
            },
            "inveja_produtiva": {
                "nome": "Inveja Produtiva",
                "categoria": "Emocional Primário",
                "gatilho": "Comparação com pares",
                "mecanica": "Transformar inveja em combustível",
                "ativacao": "Enquanto você [situação atual], outros como você [resultado desejado]",
                "momento_instalacao": "Desenvolvimento - Tensão"
            },
            "relogio_psicologico": {
                "nome": "Relógio Psicológico",
                "categoria": "Emocional Primário",
                "gatilho": "Urgência existencial",
                "mecanica": "Tempo como recurso finito",
                "ativacao": "Quantos [período] você ainda vai [desperdício]?",
                "momento_instalacao": "Pré-pitch - Urgência"
            },
            "identidade_aprisionada": {
                "nome": "Identidade Aprisionada",
                "categoria": "Emocional Primário",
                "gatilho": "Conflito entre quem é e quem poderia ser",
                "mecanica": "Expor a máscara social",
                "ativacao": "Você não é [rótulo limitante], você é [potencial real]",
                "momento_instalacao": "Desenvolvimento - Transformação"
            },
            "custo_invisivel": {
                "nome": "Custo Invisível",
                "categoria": "Emocional Primário",
                "gatilho": "Perda não percebida",
                "mecanica": "Quantificar o preço da inação",
                "ativacao": "Cada dia sem [solução] custa [perda específica]",
                "momento_instalacao": "Pré-pitch - Pressão"
            },
            "ambicao_expandida": {
                "nome": "Ambição Expandida",
                "categoria": "Emocional Primário",
                "gatilho": "Sonhos pequenos demais",
                "mecanica": "Elevar o teto mental de possibilidades",
                "ativacao": "Se o esforço é o mesmo, por que você está pedindo tão pouco?",
                "momento_instalacao": "Desenvolvimento - Visão"
            },
            "diagnostico_brutal": {
                "nome": "Diagnóstico Brutal",
                "categoria": "Emocional Primário",
                "gatilho": "Confronto com a realidade atual",
                "mecanica": "Criar indignação produtiva com status quo",
                "ativacao": "Olhe seus números/situação. Até quando você vai aceitar isso?",
                "momento_instalacao": "Abertura - Consciência"
            },
            "ambiente_vampiro": {
                "nome": "Ambiente Vampiro",
                "categoria": "Emocional Primário",
                "gatilho": "Consciência do entorno tóxico",
                "mecanica": "Revelar como ambiente atual suga energia/potencial",
                "ativacao": "Seu ambiente te impulsiona ou te mantém pequeno?",
                "momento_instalacao": "Desenvolvimento - Justificativa"
            },
            "mentor_salvador": {
                "nome": "Mentor Salvador",
                "categoria": "Emocional Primário",
                "gatilho": "Necessidade de orientação externa",
                "mecanica": "Ativar desejo por figura de autoridade que acredita neles",
                "ativacao": "Você precisa de alguém que veja seu potencial quando você não consegue",
                "momento_instalacao": "Pré-pitch - Solução"
            },
            "coragem_necessaria": {
                "nome": "Coragem Necessária",
                "categoria": "Emocional Primário",
                "gatilho": "Medo paralisante disfarçado",
                "mecanica": "Transformar desculpas em decisões corajosas",
                "ativacao": "Não é sobre condições perfeitas, é sobre decidir apesar do medo",
                "momento_instalacao": "Fechamento - Ação"
            },
            "mecanismo_revelado": {
                "nome": "Mecanismo Revelado",
                "categoria": "Racional Complementar",
                "gatilho": "Compreensão do 'como'",
                "mecanica": "Desmistificar o complexo",
                "ativacao": "É simplesmente [analogia simples], não [complicação percebida]",
                "momento_instalacao": "Desenvolvimento - Clareza"
            },
            "prova_matematica": {
                "nome": "Prova Matemática",
                "categoria": "Racional Complementar",
                "gatilho": "Certeza numérica",
                "mecanica": "Equação irrefutável",
                "ativacao": "Se você fizer X por Y dias = Resultado Z garantido",
                "momento_instalacao": "Desenvolvimento - Lógica"
            },
            "padrao_oculto": {
                "nome": "Padrão Oculto",
                "categoria": "Racional Complementar",
                "gatilho": "Insight revelador",
                "mecanica": "Mostrar o que sempre esteve lá",
                "ativacao": "Todos que conseguiram [resultado] fizeram [padrão específico]",
                "momento_instalacao": "Desenvolvimento - Revelação"
            },
            "excecao_possivel": {
                "nome": "Exceção Possível",
                "categoria": "Racional Complementar",
                "gatilho": "Quebra de limitação",
                "mecanica": "Provar que regras podem ser quebradas",
                "ativacao": "Diziam que [limitação], mas [prova contrária]",
                "momento_instalacao": "Desenvolvimento - Possibilidade"
            },
            "atalho_etico": {
                "nome": "Atalho Ético",
                "categoria": "Racional Complementar",
                "gatilho": "Eficiência sem culpa",
                "mecanica": "Validar o caminho mais rápido",
                "ativacao": "Por que sofrer [tempo longo] se existe [atalho comprovado]?",
                "momento_instalacao": "Desenvolvimento - Eficiência"
            },
            "decisao_binaria": {
                "nome": "Decisão Binária",
                "categoria": "Racional Complementar",
                "gatilho": "Simplificação radical",
                "mecanica": "Eliminar zona cinzenta",
                "ativacao": "Ou você [ação desejada] ou aceita [consequência dolorosa]",
                "momento_instalacao": "Fechamento - Escolha"
            },
            "oportunidade_oculta": {
                "nome": "Oportunidade Oculta",
                "categoria": "Racional Complementar",
                "gatilho": "Vantagem não percebida",
                "mecanica": "Revelar demanda/chance óbvia mas ignorada",
                "ativacao": "O mercado está gritando por [solução] e ninguém está ouvindo",
                "momento_instalacao": "Abertura - Despertar"
            },
            "metodo_vs_sorte": {
                "nome": "Método vs Sorte",
                "categoria": "Racional Complementar",
                "gatilho": "Caos vs sistema",
                "mecanica": "Contrastar tentativa aleatória com caminho estruturado",
                "ativacao": "Sem método você está cortando mata com foice. Com método, está na autoestrada",
                "momento_instalacao": "Pré-pitch - Caminho"
            }
        }

    def _load_objecoes_universais(self) -> Dict[str, Dict[str, Any]]:
        """Carrega as objeções universais e ocultas do documento."""
        return {
            "universais": {
                "tempo": {
                    "descricao": "Isso não é prioridade para mim",
                    "raiz_emocional": "Medo de comprometimento",
                    "tratamento": "Drives de elevação de prioridade"
                },
                "dinheiro": {
                    "descricao": "Minha vida não está tão ruim que precise investir",
                    "raiz_emocional": "Desvalorização do problema",
                    "tratamento": "Drives de justificação de investimento"
                },
                "confianca": {
                    "descricao": "Me dê uma razão para acreditar",
                    "raiz_emocional": "Experiências passadas negativas",
                    "tratamento": "Drives de construção de confiança"
                }
            },
            "ocultas": {
                "autossuficiencia": {
                    "descricao": "Acho que consigo sozinho",
                    "raiz_emocional": "Orgulho/individualismo",
                    "sinais": ["tentar sozinho", "resistência a ajuda", "linguagem técnica excessiva"],
                    "tratamento": "Histórias de experts que precisaram de mentoria"
                },
                "sinal_fraqueza": {
                    "descricao": "Aceitar ajuda é admitir fracasso",
                    "raiz_emocional": "Medo de julgamento",
                    "sinais": ["minimização de problemas", "resistência a expor vulnerabilidade"],
                    "tratamento": "Reposicionamento de ajuda como aceleração"
                },
                "medo_novo": {
                    "descricao": "Não tenho pressa",
                    "raiz_emocional": "Conforto com mediocridade",
                    "sinais": ["quando for a hora certa", "procrastinação disfarçada"],
                    "tratamento": "Histórias de arrependimento por não agir"
                },
                "prioridades_desequilibradas": {
                    "descricao": "Não é dinheiro",
                    "raiz_emocional": "Hierarquia de valores distorcida",
                    "sinais": ["gastos em outras áreas", "justificativas contraditórias"],
                    "tratamento": "Comparação cruel entre investimentos"
                },
                "autoestima_destruida": {
                    "descricao": "Não confio em mim",
                    "raiz_emocional": "Histórico de fracassos",
                    "sinais": ["já tentei antes", "autodesqualificação"],
                    "tratamento": "Cases de pessoas piores que conseguiram"
                }
            }
        }

    def _load_provas_visuais(self) -> Dict[str, Dict[str, Any]]:
        """Carrega templates de provas visuais do documento."""
        return {
            "destruidoras_objecao": {
                "tempo": [
                    {
                        "nome": "Ampulheta do Dinheiro",
                        "conceito": "Tempo perdido = dinheiro perdido",
                        "experimento": "Ampulheta com moedas caindo representando perda diária",
                        "analogia": "Cada grão que cai é uma oportunidade perdida"
                    },
                    {
                        "nome": "Agenda dos 47 Apps",
                        "conceito": "Tempo existe, está sendo desperdiçado",
                        "experimento": "Mostrar celular com dezenas de apps de distração",
                        "analogia": "Você tem tempo para 47 apps mas não para mudar sua vida?"
                    }
                ],
                "dinheiro": [
                    {
                        "nome": "Cofrinho Furado",
                        "conceito": "Gastos invisíveis vs investimento",
                        "experimento": "Cofrinho com furos vs cofre lacrado",
                        "analogia": "Sua vida financeira é o cofrinho furado"
                    },
                    {
                        "nome": "Calculadora da Verdade",
                        "conceito": "Custo real da inação",
                        "experimento": "Calcular gastos supérfluos vs investimento em educação",
                        "analogia": "R$200/mês em streaming vs R$2000 uma vez para transformar sua vida"
                    }
                ]
            },
            "criadoras_urgencia": [
                {
                    "nome": "Vela da Oportunidade",
                    "conceito": "Tempo limitado real",
                    "experimento": "Vela acesa que vai se apagando durante apresentação",
                    "analogia": "Quando a vela apagar, a oportunidade se foi"
                },
                {
                    "nome": "Trem da Estação",
                    "conceito": "Momento único que não volta",
                    "experimento": "Som de trem partindo + imagem de estação vazia",
                    "analogia": "O trem da transformação está partindo. Você embarca ou fica na plataforma?"
                }
            ],
            "instaladoras_crenca": [
                {
                    "nome": "Metamorfose da Lagarta",
                    "conceito": "Transformação é possível e natural",
                    "experimento": "Sequência visual lagarta → casulo → borboleta",
                    "analogia": "Você está no casulo. A borboleta está esperando para sair"
                },
                {
                    "nome": "Diamante do Carvão",
                    "conceito": "Pressão certa gera transformação",
                    "experimento": "Carvão + pressão = diamante (visual/metáfora)",
                    "analogia": "A pressão que você sente é o que vai te transformar em diamante"
                }
            ]
        }

    def analyze_avatar_psychology(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Realiza análise psicológica profunda do avatar baseada nos dados fornecidos.
        Implementa a metodologia do documento 'Arquiteto de Drivers Mentais'.
        """
        segmento = data.get('segmento', '')
        produto = data.get('produto', '')
        publico = data.get('publico', '')
        preco = data.get('preco', 0)
        
        # Análise psicográfica baseada no segmento
        perfil_psicologico = self._analyze_psychographic_profile(segmento, publico, preco)
        
        # Identificação de dores viscerais
        dores_secretas = self._identify_visceral_pains(segmento, publico)
        
        # Mapeamento de desejos ocultos
        desejos_ardentes = self._map_hidden_desires(segmento, produto, preco)
        
        # Identificação de medos paralisantes
        medos_paralisantes = self._identify_paralyzing_fears(segmento, publico)
        
        # Mapeamento de objeções reais
        objecoes_reais = self._map_real_objections(segmento, preco)
        
        return {
            "perfil_psicologico": perfil_psicologico,
            "dores_secretas": dores_secretas,
            "desejos_ardentes": desejos_ardentes,
            "medos_paralisantes": medos_paralisantes,
            "objecoes_reais": objecoes_reais,
            "nivel_sofisticacao": self._assess_sophistication_level(segmento, preco),
            "triggers_emocionais": self._identify_emotional_triggers(segmento, publico)
        }

    def _analyze_psychographic_profile(self, segmento: str, publico: str, preco: float) -> Dict[str, Any]:
        """Analisa o perfil psicográfico baseado no segmento e público."""
        segmento_lower = segmento.lower()
        
        if any(term in segmento_lower for term in ['digital', 'online', 'marketing', 'vendas']):
            return {
                "arquetipo_dominante": "Empreendedor Digital",
                "nivel_ansiedade": "Alto",
                "orientacao_temporal": "Futuro",
                "motivacao_primaria": "Liberdade financeira e reconhecimento",
                "medo_primario": "Fracasso público e perda de status",
                "linguagem_preferida": "Resultados, métricas, escalabilidade",
                "referencias_culturais": "Gurus digitais, cases de sucesso, lifestyle"
            }
        elif any(term in segmento_lower for term in ['consultoria', 'coaching', 'mentoria']):
            return {
                "arquetipo_dominante": "Especialista/Mentor",
                "nivel_ansiedade": "Médio-Alto",
                "orientacao_temporal": "Presente-Futuro",
                "motivacao_primaria": "Impacto e autoridade",
                "medo_primario": "Perda de credibilidade",
                "linguagem_preferida": "Transformação, metodologia, expertise",
                "referencias_culturais": "Autoridades do nicho, certificações"
            }
        elif any(term in segmento_lower for term in ['ecommerce', 'loja', 'vendas']):
            return {
                "arquetipo_dominante": "Comerciante",
                "nivel_ansiedade": "Alto",
                "orientacao_temporal": "Presente",
                "motivacao_primaria": "Lucro e crescimento",
                "medo_primario": "Falência e perda de clientes",
                "linguagem_preferida": "ROI, conversão, faturamento",
                "referencias_culturais": "Cases de vendas, números de faturamento"
            }
        else:
            return {
                "arquetipo_dominante": "Profissional em Transição",
                "nivel_ansiedade": "Médio",
                "orientacao_temporal": "Presente-Futuro",
                "motivacao_primaria": "Estabilidade e crescimento",
                "medo_primario": "Estagnação e irrelevância",
                "linguagem_preferida": "Oportunidade, desenvolvimento, segurança",
                "referencias_culturais": "Histórias de transformação profissional"
            }

    def _identify_visceral_pains(self, segmento: str, publico: str) -> List[str]:
        """Identifica as dores mais viscerais e inconfessáveis do avatar."""
        segmento_lower = segmento.lower()
        
        dores_base = [
            "Acordar todos os dias sabendo que está desperdiçando seu potencial",
            "Ver pessoas menos qualificadas conseguindo resultados melhores",
            "Sentir que está enganando a si mesmo sobre estar 'bem assim mesmo'"
        ]
        
        if 'digital' in segmento_lower or 'online' in segmento_lower:
            dores_base.extend([
                "Trabalhar 12 horas por dia para ganhar o que um funcionário ganha em 8",
                "Ter que fingir sucesso nas redes sociais enquanto passa aperto financeiro",
                "Ver ex-colegas de trabalho ganhando mais como CLT do que você como 'empreendedor'"
            ])
        
        if 'consultoria' in segmento_lower or 'coaching' in segmento_lower:
            dores_base.extend([
                "Cobrar barato porque não acredita no próprio valor",
                "Ter conhecimento mas não conseguir monetizar adequadamente",
                "Ser visto como 'coach de Instagram' em vez de especialista sério"
            ])
        
        return dores_base[:5]  # Retorna as 5 mais relevantes

    def _map_hidden_desires(self, segmento: str, produto: str, preco: float) -> List[str]:
        """Mapeia os desejos mais profundos e inconfessáveis."""
        desejos_base = [
            "Ser reconhecido como autoridade máxima no seu nicho",
            "Ter liberdade financeira real, não apenas 'se virar'",
            "Provar para quem duvidou que você estava certo"
        ]
        
        if preco and preco > 1000:
            desejos_base.extend([
                "Fazer parte de um grupo seleto de pessoas de sucesso",
                "Ter acesso a informações que a maioria não tem",
                "Ser visto como alguém que 'chegou lá'"
            ])
        
        segmento_lower = segmento.lower()
        if 'digital' in segmento_lower:
            desejos_base.extend([
                "Trabalhar de qualquer lugar do mundo",
                "Ter um negócio que funciona sem você",
                "Ser exemplo de sucesso para outros empreendedores"
            ])
        
        return desejos_base[:5]

    def _identify_paralyzing_fears(self, segmento: str, publico: str) -> List[str]:
        """Identifica os medos que paralisam a ação."""
        medos_base = [
            "Investir e não dar certo, confirmando que você é um fracasso",
            "Descobrir que o problema é você, não as circunstâncias",
            "Ter que admitir que desperdiçou anos fazendo tudo errado"
        ]
        
        segmento_lower = segmento.lower()
        if any(term in segmento_lower for term in ['empreendedor', 'negócio', 'empresa']):
            medos_base.extend([
                "Falir e ter que voltar a ser empregado",
                "Ser julgado pela família como 'sonhador irresponsável'",
                "Descobrir que não tem o que é preciso para ser empresário"
            ])
        
        return medos_base[:4]

    def _map_real_objections(self, segmento: str, preco: float) -> List[str]:
        """Mapeia as objeções reais que surgirão."""
        objecoes = [
            "Não tenho tempo para mais uma coisa agora",
            "Preciso pensar melhor / conversar com minha esposa",
            "Já tentei coisas parecidas antes e não funcionou"
        ]
        
        if preco and preco > 500:
            objecoes.extend([
                "Está muito caro para o meu momento atual",
                "Não tenho certeza se vai funcionar para o meu caso específico"
            ])
        
        if preco and preco > 2000:
            objecoes.extend([
                "Preciso ver se consigo um financiamento",
                "Vou esperar uma promoção ou desconto"
            ])
        
        return objecoes

    def _assess_sophistication_level(self, segmento: str, preco: float) -> str:
        """Avalia o nível de sofisticação do mercado."""
        if preco and preco > 5000:
            return "Alto - Mercado sofisticado, precisa de abordagem consultiva"
        elif preco and preco > 1000:
            return "Médio-Alto - Conhece o mercado, precisa de diferenciação clara"
        elif preco and preco > 500:
            return "Médio - Tem alguma experiência, precisa de prova de valor"
        else:
            return "Iniciante - Pouca experiência, precisa de educação básica"

    def _identify_emotional_triggers(self, segmento: str, publico: str) -> List[str]:
        """Identifica os gatilhos emocionais mais eficazes."""
        triggers = [
            "Comparação com pares que conseguiram sucesso",
            "Urgência temporal (oportunidades perdidas)",
            "Medo de arrependimento futuro"
        ]
        
        segmento_lower = segmento.lower()
        if 'digital' in segmento_lower:
            triggers.extend([
                "FOMO de tendências digitais",
                "Medo de ficar para trás na tecnologia",
                "Desejo de lifestyle digital"
            ])
        
        return triggers

    def create_mental_drivers_sequence(self, avatar_analysis: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria uma sequência otimizada de drivers mentais baseada na análise do avatar.
        Implementa a metodologia do documento 'Arquiteto do Pré-Pitch Invisível'.
        """
        # Seleciona os 7 drivers mais poderosos para este contexto
        selected_drivers = self._select_optimal_drivers(avatar_analysis, context)
        
        # Organiza em sequência psicológica
        sequenced_drivers = self._sequence_drivers_psychologically(selected_drivers)
        
        # Cria roteiros de ativação personalizados
        activation_scripts = self._create_activation_scripts(sequenced_drivers, avatar_analysis)
        
        return {
            "drivers_selecionados": sequenced_drivers,
            "roteiros_ativacao": activation_scripts,
            "sequencia_psicologica": self._create_psychological_sequence(sequenced_drivers),
            "momentos_criticos": self._identify_critical_moments(sequenced_drivers)
        }

    def _select_optimal_drivers(self, avatar_analysis: Dict[str, Any], context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Seleciona os drivers mais eficazes para o contexto específico."""
        arquetipo = avatar_analysis.get("perfil_psicologico", {}).get("arquetipo_dominante", "")
        nivel_ansiedade = avatar_analysis.get("perfil_psicologico", {}).get("nivel_ansiedade", "")
        
        # Drivers essenciais para todos os contextos
        essential_drivers = ["diagnostico_brutal", "ambicao_expandida", "relogio_psicologico", "metodo_vs_sorte"]
        
        # Drivers específicos por arquétipo
        if "Empreendedor Digital" in arquetipo:
            specific_drivers = ["custo_invisivel", "ambiente_vampiro", "decisao_binaria"]
        elif "Especialista" in arquetipo:
            specific_drivers = ["identidade_aprisionada", "mentor_salvador", "coragem_necessaria"]
        else:
            specific_drivers = ["ferida_exposta", "oportunidade_oculta", "excecao_possivel"]
        
        # Combina e retorna os drivers selecionados
        selected_keys = essential_drivers + specific_drivers[:3]
        return [{"key": key, **self.drivers_mentais[key]} for key in selected_keys if key in self.drivers_mentais]

    def _sequence_drivers_psychologically(self, drivers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Organiza os drivers na sequência psicológica ideal."""
        # Ordem psicológica: Consciência → Desejo → Tensão → Solução → Ação
        sequence_order = {
            "Abertura - Consciência": 1,
            "Abertura - Despertar": 1,
            "Abertura - Quebra de padrão": 1,
            "Desenvolvimento - Amplificação": 2,
            "Desenvolvimento - Visão": 2,
            "Desenvolvimento - Tensão": 3,
            "Pré-pitch - Pressão": 4,
            "Pré-pitch - Urgência": 4,
            "Pré-pitch - Solução": 5,
            "Pré-pitch - Caminho": 5,
            "Fechamento - Ação": 6,
            "Fechamento - Escolha": 6
        }
        
        return sorted(drivers, key=lambda d: sequence_order.get(d.get("momento_instalacao", ""), 999))

    def _create_activation_scripts(self, drivers: List[Dict[str, Any]], avatar_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Cria roteiros de ativação personalizados para cada driver."""
        scripts = {}
        linguagem = avatar_analysis.get("perfil_psicologico", {}).get("linguagem_preferida", "")
        
        for driver in drivers:
            key = driver["key"]
            scripts[key] = {
                "abertura_emocional": self._create_emotional_opening(driver, avatar_analysis),
                "historia_analogia": self._create_story_analogy(driver, avatar_analysis),
                "metafora_visual": self._create_visual_metaphor(driver, avatar_analysis),
                "comando_comportamental": self._create_behavioral_command(driver, avatar_analysis),
                "frases_ancoragem": self._create_anchoring_phrases(driver, avatar_analysis)
            }
        
        return scripts

    def _create_emotional_opening(self, driver: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Cria abertura emocional personalizada para o driver."""
        dores = avatar_analysis.get("dores_secretas", [])
        if not dores:
            return driver.get("ativacao", "")
        
        dor_principal = dores[0] if dores else "sua situação atual"
        
        templates = {
            "ferida_exposta": f"Você ainda acorda todos os dias sabendo que {dor_principal.lower()}?",
            "diagnostico_brutal": f"Olhe para sua situação atual. Até quando você vai aceitar {dor_principal.lower()}?",
            "relogio_psicologico": f"Quantos anos você ainda vai desperdiçar {dor_principal.lower()}?",
            "custo_invisivel": f"Cada dia que passa sem resolver isso, você está perdendo mais do que imagina. {dor_principal}",
            "ambicao_expandida": f"Se você vai ter o trabalho de mudar, por que não mirar mais alto que apenas 'resolver' {dor_principal.lower()}?"
        }
        
        return templates.get(driver["key"], driver.get("ativacao", ""))

    def _create_story_analogy(self, driver: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Cria história/analogia personalizada."""
        arquetipo = avatar_analysis.get("perfil_psicologico", {}).get("arquetipo_dominante", "")
        
        if "Empreendedor Digital" in arquetipo:
            base_context = "negócio online"
            references = "outros empreendedores digitais"
        elif "Especialista" in arquetipo:
            base_context = "consultoria"
            references = "outros especialistas"
        else:
            base_context = "carreira"
            references = "outros profissionais"
        
        analogies = {
            "metodo_vs_sorte": f"É como a diferença entre ter um GPS e tentar chegar ao destino perguntando para estranhos na rua. No {base_context}, quem tem método chega primeiro.",
            "ambiente_vampiro": f"É como tentar encher um balde furado. Seu {base_context} pode estar vazando energia pelos furos que você nem vê.",
            "diagnostico_brutal": f"É como olhar no espelho pela primeira vez em anos. Dói, mas é o primeiro passo para a transformação."
        }
        
        return analogies.get(driver["key"], f"É como {driver.get('mecanica', '')} aplicado ao seu {base_context}.")

    def _create_visual_metaphor(self, driver: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Cria metáfora visual impactante."""
        metaphors = {
            "relogio_psicologico": "Imagine um relógio gigante na sua frente, onde cada segundo que passa é uma oportunidade perdida de transformar sua vida.",
            "custo_invisivel": "Visualize dinheiro literalmente voando da sua carteira a cada dia que você adia essa decisão.",
            "ambicao_expandida": "Imagine-se daqui a 2 anos, não apenas tendo resolvido seus problemas, mas sendo referência para outros.",
            "metodo_vs_sorte": "Visualize duas pessoas: uma com um mapa detalhado, outra perdida na floresta. Qual chegará primeiro ao tesouro?"
        }
        
        return metaphors.get(driver["key"], "Imagine a transformação que isso pode gerar na sua vida.")

    def _create_behavioral_command(self, driver: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> str:
        """Cria comando comportamental específico."""
        commands = {
            "diagnostico_brutal": "Pare de se enganar. Olhe os números reais da sua situação.",
            "relogio_psicologico": "Decida agora. Cada minuto de hesitação é um minuto perdido.",
            "ambicao_expandida": "Mire mais alto. Se vai mudar, mude para valer.",
            "metodo_vs_sorte": "Escolha o caminho estruturado. Pare de tentar na sorte.",
            "decisao_binaria": "Ou você age agora ou aceita ficar onde está para sempre."
        }
        
        return commands.get(driver["key"], "Tome a decisão que seu futuro eu agradecerá.")

    def _create_anchoring_phrases(self, driver: Dict[str, Any], avatar_analysis: Dict[str, Any]) -> List[str]:
        """Cria frases de ancoragem memoráveis."""
        phrases = {
            "diagnostico_brutal": [
                "A verdade dói, mas a mentira mata",
                "Números não mentem, pessoas se enganam",
                "Sua situação atual é o resultado das suas decisões passadas"
            ],
            "relogio_psicologico": [
                "Tempo perdido não volta, oportunidade perdida não retorna",
                "Cada dia que passa é um dia a menos para sua transformação",
                "O relógio não para para ninguém"
            ],
            "metodo_vs_sorte": [
                "Método é GPS, sorte é andar perdido",
                "Quem tem sistema vence quem tem sorte",
                "Tentativa e erro é luxo de quem tem tempo infinito"
            ]
        }
        
        return phrases.get(driver["key"], ["Essa é a decisão que muda tudo"])

    def _create_psychological_sequence(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria a sequência psicológica completa."""
        return {
            "fase_1_consciencia": [d for d in drivers if "Abertura" in d.get("momento_instalacao", "")],
            "fase_2_desejo": [d for d in drivers if "Desenvolvimento" in d.get("momento_instalacao", "")],
            "fase_3_pressao": [d for d in drivers if "Pré-pitch" in d.get("momento_instalacao", "")],
            "fase_4_acao": [d for d in drivers if "Fechamento" in d.get("momento_instalacao", "")]
        }

    def _identify_critical_moments(self, drivers: List[Dict[str, Any]]) -> List[str]:
        """Identifica os momentos críticos da apresentação."""
        return [
            "Primeiros 3 minutos - Quebra de padrão com Diagnóstico Brutal",
            "Minuto 15-20 - Amplificação do desejo com Ambição Expandida",
            "Minuto 35-40 - Criação de urgência com Relógio Psicológico",
            "Minuto 50-55 - Apresentação da solução com Método vs Sorte",
            "Últimos 5 minutos - Fechamento com Decisão Binária"
        ]

    def create_visual_proofs_arsenal(self, context: Dict[str, Any], drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Cria arsenal completo de provas visuais baseado no documento anexo.
        """
        # Identifica conceitos que precisam de demonstração
        concepts_to_prove = self._identify_concepts_to_prove(context, drivers)
        
        # Cria PROVIs para cada conceito
        visual_proofs = {}
        for concept in concepts_to_prove:
            visual_proofs[concept["key"]] = self._create_provi(concept, context)
        
        # Organiza em sequência estratégica
        sequenced_proofs = self._sequence_visual_proofs(visual_proofs, drivers)
        
        return {
            "arsenal_completo": visual_proofs,
            "sequencia_otimizada": sequenced_proofs,
            "momentos_estrategicos": self._map_strategic_moments(sequenced_proofs),
            "kit_implementacao": self._create_implementation_kit(visual_proofs)
        }

    def _identify_concepts_to_prove(self, context: Dict[str, Any], drivers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identifica todos os conceitos que precisam de demonstração visual."""
        concepts = []
        
        # Conceitos dos drivers mentais
        for driver in drivers:
            concepts.append({
                "key": f"driver_{driver['key']}",
                "name": driver["nome"],
                "concept": driver["mecanica"],
                "category": "driver_mental",
                "priority": "alta"
            })
        
        # Conceitos de objeções universais
        for objecao_key, objecao in self.objecoes_universais["universais"].items():
            concepts.append({
                "key": f"objecao_{objecao_key}",
                "name": f"Destruir Objeção: {objecao_key.title()}",
                "concept": objecao["descricao"],
                "category": "destruir_objecao",
                "priority": "critica"
            })
        
        # Conceitos do produto/método
        if context.get("produto"):
            concepts.append({
                "key": "metodo_produto",
                "name": "Demonstração do Método",
                "concept": f"Como {context['produto']} funciona na prática",
                "category": "prova_metodo",
                "priority": "critica"
            })
        
        return concepts

    def _create_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria uma PROVI completa para um conceito específico."""
        concept_key = concept["key"]
        
        # Templates específicos por tipo de conceito
        if "objecao_tempo" in concept_key:
            return self._create_time_objection_provi(concept, context)
        elif "objecao_dinheiro" in concept_key:
            return self._create_money_objection_provi(concept, context)
        elif "driver_relogio" in concept_key:
            return self._create_urgency_provi(concept, context)
        elif "driver_metodo" in concept_key:
            return self._create_method_provi(concept, context)
        else:
            return self._create_generic_provi(concept, context)

    def _create_time_objection_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria PROVI específica para objeção de tempo."""
        return {
            "nome_impactante": "A Agenda dos 47 Apps",
            "conceito_alvo": "Tempo existe, está sendo desperdiçado",
            "categoria": "Destruidora de Objeção",
            "prioridade": "Crítica",
            "momento_ideal": "Quando surgir objeção de tempo",
            "objetivo_psicologico": "Mostrar que tempo existe, mas está sendo mal usado",
            "experimento": {
                "setup": "Pegue seu celular e abra a tela de apps instalados",
                "execucao": [
                    "Conte quantos apps você tem instalados",
                    "Mostre apps de entretenimento, jogos, redes sociais",
                    "Calcule tempo médio gasto por dia em cada um"
                ],
                "climax": "Revelação: 'Você tem tempo para 47 apps mas não para mudar sua vida?'",
                "bridge": "O problema não é falta de tempo, é prioridade errada"
            },
            "analogia_perfeita": "Assim como você encontra tempo para 47 apps → Você pode encontrar tempo para sua transformação",
            "materiais": ["Smartphone", "Calculadora", "Cronômetro"],
            "variacoes": {
                "online": "Compartilhamento de tela mostrando apps",
                "presencial": "Pedir para plateia verificar próprios celulares",
                "intimista": "Análise individual personalizada"
            },
            "frases_impacto": [
                "Durante: 'Vamos contar juntos quantos apps você tem...'",
                "Revelação: 'Você tem tempo para 47 apps mas não para mudar sua vida?'",
                "Ancoragem: 'Tempo não falta, prioridade que está errada'"
            ],
            "gestao_riscos": {
                "pode_falhar_se": "Pessoa tem poucos apps ou usa pouco o celular",
                "plano_b": "Usar exemplo de TV, Netflix, redes sociais",
                "transformar_erro": "'Parabéns, você é exceção. Mas e as outras distrações?'"
            }
        }

    def _create_money_objection_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria PROVI específica para objeção de dinheiro."""
        preco = context.get("preco", 1000)
        return {
            "nome_impactante": "O Cofrinho Furado",
            "conceito_alvo": "Gastos invisíveis vs investimento consciente",
            "categoria": "Destruidora de Objeção",
            "prioridade": "Crítica",
            "momento_ideal": "Quando surgir objeção de preço",
            "objetivo_psicologico": "Mostrar que dinheiro existe, mas está vazando",
            "experimento": {
                "setup": "Dois recipientes: um cofrinho com furos, outro cofre lacrado",
                "execucao": [
                    "Coloque moedas no cofrinho furado - elas caem",
                    "Coloque moedas no cofre lacrado - ficam seguras",
                    "Calcule gastos mensais supérfluos vs investimento único"
                ],
                "climax": "Revelação: 'Sua vida financeira é o cofrinho furado'",
                "bridge": "Investimento é trocar o cofrinho furado pelo cofre lacrado"
            },
            "analogia_perfeita": "Assim como moedas caem do cofrinho furado → Seu dinheiro vaza em gastos desnecessários",
            "materiais": ["Cofrinho com furos", "Cofre pequeno", "Moedas", "Calculadora"],
            "calculo_brutal": f"R$200/mês em supérfluos = R$2.400/ano. Investimento de R${preco} se paga em {round(preco/200)} meses",
            "variacoes": {
                "online": "Demonstração com recipientes transparentes na câmera",
                "presencial": "Plateia pode ver moedas caindo",
                "intimista": "Cálculo personalizado dos gastos da pessoa"
            },
            "frases_impacto": [
                "Durante: 'Vamos ver onde seu dinheiro está vazando...'",
                "Revelação: 'Sua vida financeira é este cofrinho furado'",
                "Ancoragem: 'Pare de vazar dinheiro, comece a investir'"
            ]
        }

    def _create_urgency_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria PROVI para criar urgência temporal."""
        return {
            "nome_impactante": "A Vela da Oportunidade",
            "conceito_alvo": "Tempo limitado real e irreversível",
            "categoria": "Criadora de Urgência",
            "prioridade": "Alta",
            "momento_ideal": "Pré-pitch - Criação de urgência",
            "objetivo_psicologico": "Instalar urgência visceral sobre tempo limitado",
            "experimento": {
                "setup": "Acenda uma vela no início da apresentação",
                "execucao": [
                    "Vela queima durante toda apresentação",
                    "Periodicamente mencione: 'A vela está diminuindo'",
                    "No final: vela quase apagada"
                ],
                "climax": "Revelação: 'Quando esta vela apagar, a oportunidade se vai'",
                "bridge": "Oportunidades têm prazo de validade, como esta vela"
            },
            "analogia_perfeita": "Assim como a vela se consome → Oportunidades têm tempo limitado",
            "materiais": ["Vela grande", "Isqueiro", "Prato de segurança"],
            "variacoes": {
                "online": "Vela bem visível na câmera, timer na tela",
                "presencial": "Vela grande que todos vejam",
                "intimista": "Vela pequena na mesa entre vocês"
            },
            "dramatizacao_extra": "Som de relógio fazendo tique-taque de fundo",
            "frases_impacto": [
                "Durante: 'Vejam como a vela está diminuindo...'",
                "Revelação: 'Quando esta vela apagar, a oportunidade se vai'",
                "Ancoragem: 'Oportunidades se consomem como velas'"
            ]
        }

    def _create_method_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria PROVI para demonstrar eficácia do método."""
        return {
            "nome_impactante": "GPS vs Mapa Rasgado",
            "conceito_alvo": "Método estruturado vs tentativa e erro",
            "categoria": "Prova de Método",
            "prioridade": "Crítica",
            "momento_ideal": "Apresentação da solução",
            "objetivo_psicologico": "Mostrar superioridade do método estruturado",
            "experimento": {
                "setup": "GPS funcionando vs mapa de papel rasgado",
                "execucao": [
                    "Mostre GPS com rota clara para destino",
                    "Mostre mapa rasgado, ilegível, sem direção",
                    "Simule tentativa de chegar ao destino com cada um"
                ],
                "climax": "Revelação: 'Com qual você chegaria primeiro?'",
                "bridge": "Meu método é seu GPS para o sucesso"
            },
            "analogia_perfeita": "Assim como GPS te leva direto ao destino → Método te leva direto ao resultado",
            "materiais": ["Smartphone com GPS", "Mapa de papel rasgado", "Marcador"],
            "variacoes": {
                "online": "Compartilhamento de tela com GPS vs imagem de mapa rasgado",
                "presencial": "Props físicos que todos vejam",
                "intimista": "Demonstração no celular da pessoa"
            },
            "frases_impacto": [
                "Durante: 'Vamos ver a diferença entre ter direção e andar perdido...'",
                "Revelação: 'Com qual você chegaria primeiro ao seu objetivo?'",
                "Ancoragem: 'Método é GPS, tentativa e erro é mapa rasgado'"
            ]
        }

    def _create_generic_provi(self, concept: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria PROVI genérica para conceitos não específicos."""
        return {
            "nome_impactante": f"Demonstração: {concept['name']}",
            "conceito_alvo": concept["concept"],
            "categoria": concept["category"],
            "prioridade": concept["priority"],
            "momento_ideal": "A definir baseado no contexto",
            "objetivo_psicologico": f"Tornar tangível: {concept['concept']}",
            "experimento": {
                "setup": "Preparar demonstração visual do conceito",
                "execucao": ["Passo 1: Mostrar situação atual", "Passo 2: Aplicar conceito", "Passo 3: Mostrar resultado"],
                "climax": "Revelação do impacto da transformação",
                "bridge": "Conectar com a vida real da audiência"
            },
            "analogia_perfeita": f"Assim como na demonstração → Na sua vida real",
            "materiais": ["A definir baseado no conceito específico"],
            "frases_impacto": ["Durante: 'Vejam o que acontece quando...'", "Revelação: 'Esta é a diferença que faz'", "Ancoragem: 'Isso pode ser sua realidade'"]
        }

    def generate_comprehensive_psychological_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Método principal que orquestra toda a análise psicológica completa.
        """
        logger.info("🧠 Iniciando análise psicológica profunda...")
        
        # Fase 1: Análise do Avatar
        avatar_analysis = self.analyze_avatar_psychology(data)
        
        # Fase 2: Criação de Drivers Mentais
        drivers_sequence = self.create_mental_drivers_sequence(avatar_analysis, data)
        
        # Fase 3: Mapeamento de Objeções
        objections_map = self._create_objections_map(avatar_analysis, data)
        
        # Fase 4: Arsenal de Provas Visuais
        visual_proofs = self.create_visual_proofs_arsenal(data, drivers_sequence["drivers_selecionados"])
        
        # Fase 5: Estratégia de Pré-Pitch
        pre_pitch_strategy = self._create_pre_pitch_strategy(drivers_sequence, objections_map)
        
        return {
            "avatar_psicologico_profundo": avatar_analysis,
            "drivers_mentais_customizados": drivers_sequence,
            "mapeamento_objecoes": objections_map,
            "arsenal_provas_visuais": visual_proofs,
            "estrategia_pre_pitch": pre_pitch_strategy,
            "plano_implementacao": self._create_implementation_plan(drivers_sequence, objections_map, visual_proofs)
        }

    def _create_objections_map(self, avatar_analysis: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Cria mapeamento completo de objeções baseado na análise."""
        objecoes_identificadas = avatar_analysis.get("objecoes_reais", [])
        
        return {
            "objecoes_universais_detectadas": {
                "tempo": {
                    "probabilidade": "Alta",
                    "sinais": ["agenda cheia", "muitas responsabilidades"],
                    "tratamento": "Driver do Relógio Psicológico + PROVI da Agenda dos 47 Apps",
                    "momento_critico": "Após apresentação do investimento de tempo"
                },
                "dinheiro": {
                    "probabilidade": "Média-Alta",
                    "sinais": ["preocupação com preço", "comparação com gastos"],
                    "tratamento": "Driver do Custo Invisível + PROVI do Cofrinho Furado",
                    "momento_critico": "Revelação do preço"
                },
                "confianca": {
                    "probabilidade": "Média",
                    "sinais": ["ceticismo", "pedidos de prova"],
                    "tratamento": "Driver da Prova Matemática + Cases específicos",
                    "momento_critico": "Apresentação da metodologia"
                }
            },
            "objecoes_ocultas_previstas": {
                "autossuficiencia": {
                    "probabilidade": self._assess_objection_probability("autossuficiencia", avatar_analysis),
                    "tratamento": "História do Expert que Precisou de Expert",
                    "sinais_alerta": ["linguagem técnica", "minimização da dificuldade"]
                },
                "medo_mudanca": {
                    "probabilidade": self._assess_objection_probability("medo_mudanca", avatar_analysis),
                    "tratamento": "Driver da Coragem Necessária + Histórias de arrependimento",
                    "sinais_alerta": ["procrastinação", "condições perfeitas"]
                }
            },
            "arsenal_neutralizacao": self._create_neutralization_arsenal(objecoes_identificadas)
        }

    def _assess_objection_probability(self, objection_type: str, avatar_analysis: Dict[str, Any]) -> str:
        """Avalia probabilidade de uma objeção específica surgir."""
        arquetipo = avatar_analysis.get("perfil_psicologico", {}).get("arquetipo_dominante", "")
        
        if objection_type == "autossuficiencia" and "Especialista" in arquetipo:
            return "Alta"
        elif objection_type == "medo_mudanca" and "Transição" in arquetipo:
            return "Alta"
        else:
            return "Média"

    def _create_neutralization_arsenal(self, objecoes: List[str]) -> Dict[str, Any]:
        """Cria arsenal específico para neutralizar objeções identificadas."""
        arsenal = {}
        
        for objecao in objecoes:
            if "tempo" in objecao.lower():
                arsenal["tempo"] = {
                    "tecnica": "Concordar + Valorizar + Apresentar",
                    "script": "Você tem razão, tempo é seu recurso mais valioso. Por isso criei um método que economiza anos de tentativa e erro.",
                    "follow_up": "PROVI da Agenda dos 47 Apps"
                }
            elif "dinheiro" in objecao.lower() or "caro" in objecao.lower():
                arsenal["dinheiro"] = {
                    "tecnica": "Inversão de Perspectiva",
                    "script": "Na verdade, é o oposto. Não investir é que está custando caro. Deixe-me mostrar...",
                    "follow_up": "Cálculo do Custo de Oportunidade"
                }
            elif "tentei" in objecao.lower():
                arsenal["tentativas_passadas"] = {
                    "tecnica": "Nova Crença",
                    "script": "Isso é uma crença limitante baseada em experiências com métodos incompletos. Vou te mostrar a diferença...",
                    "follow_up": "PROVI GPS vs Mapa Rasgado"
                }
        
        return arsenal

    def _create_pre_pitch_strategy(self, drivers_sequence: Dict[str, Any], objections_map: Dict[str, Any]) -> Dict[str, Any]:
        """Cria estratégia completa de pré-pitch invisível."""
        return {
            "sequencia_psicologica": {
                "fase_1_despertar": {
                    "duracao": "5-7 minutos",
                    "objetivo": "Quebrar padrão e criar consciência",
                    "drivers": drivers_sequence["sequencia_psicologica"]["fase_1_consciencia"],
                    "tecnicas": ["Diagnóstico Brutal", "Oportunidade Oculta"]
                },
                "fase_2_amplificar": {
                    "duracao": "8-12 minutos",
                    "objetivo": "Amplificar desejo e criar tensão",
                    "drivers": drivers_sequence["sequencia_psicologica"]["fase_2_desejo"],
                    "tecnicas": ["Ambição Expandida", "Inveja Produtiva"]
                },
                "fase_3_pressionar": {
                    "duracao": "5-8 minutos",
                    "objetivo": "Criar urgência e necessidade",
                    "drivers": drivers_sequence["sequencia_psicologica"]["fase_3_pressao"],
                    "tecnicas": ["Relógio Psicológico", "Custo Invisível"]
                },
                "fase_4_direcionar": {
                    "duracao": "3-5 minutos",
                    "objetivo": "Apresentar caminho e forçar decisão",
                    "drivers": drivers_sequence["sequencia_psicologica"]["fase_4_acao"],
                    "tecnicas": ["Método vs Sorte", "Decisão Binária"]
                }
            },
            "pontes_transicao": {
                "emocao_para_logica": "Eu sei que você está sentindo isso agora... Mas seu cérebro racional está perguntando: 'Será que funciona?' Então deixe-me mostrar os números...",
                "problema_para_solucao": "Agora que você viu onde está o problema, deixe-me mostrar exatamente como resolver...",
                "urgencia_para_acao": "O tempo está passando enquanto falamos. A pergunta é: você vai agir ou vai deixar passar mais uma oportunidade?"
            },
            "momentos_criticos": drivers_sequence["momentos_criticos"]
        }

    def _create_implementation_plan(self, drivers: Dict[str, Any], objections: Dict[str, Any], proofs: Dict[str, Any]) -> Dict[str, Any]:
        """Cria plano completo de implementação."""
        return {
            "cronograma_execucao": {
                "preparacao": {
                    "tempo": "2-3 dias antes",
                    "atividades": [
                        "Ensaiar sequência de drivers",
                        "Preparar materiais para PROVIs",
                        "Testar equipamentos técnicos",
                        "Revisar scripts de neutralização"
                    ]
                },
                "execucao": {
                    "tempo": "Durante evento",
                    "checkpoints": [
                        "Minuto 5: Primeiro driver instalado",
                        "Minuto 15: Primeira PROVI executada",
                        "Minuto 30: Objeções antecipadas",
                        "Minuto 45: Pré-pitch iniciado"
                    ]
                }
            },
            "metricas_sucesso": {
                "durante_apresentacao": [
                    "Silêncio absoluto durante drivers",
                    "Reações emocionais visíveis",
                    "Perguntas sobre 'quando abre'",
                    "Comentários de identificação"
                ],
                "pos_apresentacao": [
                    "Ansiedade para oferta",
                    "Objeções minimizadas",
                    "Perguntas sobre preço/formato",
                    "Decisões rápidas"
                ]
            },
            "kit_emergencia": {
                "objecoes_inesperadas": "Scripts de concordância + virada",
                "falhas_tecnicas": "Versões simplificadas das PROVIs",
                "resistencia_alta": "Drivers de confronto controlado",
                "energia_baixa": "Técnicas de reativação da audiência"
            }
        }

# Instância global
psychological_analysis_engine = PsychologicalAnalysisEngine()