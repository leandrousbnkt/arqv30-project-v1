# Ficheiro: src/services/mental_drivers_architect.py

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class MentalDriversArchitect:
    """
    Arquiteto de Drivers Mentais.
    Este serviço contém uma base de conhecimento sobre gatilhos psicológicos
    usados em marketing e vendas. Na versão atual, ele fornece uma lista
    de drivers universais. No futuro, pode ser expandido com IA para
    personalizar os drivers com base nos dados do avatar.
    """
    def __init__(self):
        """
        Inicializa o arquiteto e carrega a base de conhecimento de drivers mentais universais.
        """
        self.universal_drivers = self._load_universal_drivers()
        logger.info("✅ Mental Drivers Architect inicializado com a base de conhecimento.")

    def _load_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """
        Define uma lista de 7 drivers mentais fundamentais.
        Cada driver inclui uma explicação e um exemplo de aplicação.
        """
        return {
            "urgencia": {
                "nome": "Urgência",
                "categoria": "Ação Imediata",
                "descricao": "Motiva a tomada de decisão rápida para evitar a perda de uma oportunidade com tempo limitado.",
                "exemplo_aplicacao": "Oferecer um bónus especial para as primeiras 10 pessoas que se inscreverem ou limitar a oferta a 24 horas."
            },
            "prova_social": {
                "nome": "Prova Social",
                "categoria": "Confiança e Validação",
                "descricao": "As pessoas tendem a seguir as ações da maioria. Mostrar que outros estão a usar e a aprovar o produto aumenta a confiança.",
                "exemplo_aplicacao": "Exibir depoimentos de clientes satisfeitos, estudos de caso com resultados, ou o número de pessoas que já compraram."
            },
            "escassez": {
                "nome": "Escassez",
                "categoria": "Ação Imediata",
                "descricao": "A percepção de que um produto é limitado em quantidade aumenta o seu valor percebido e o desejo de o possuir.",
                "exemplo_aplicacao": "Limitar o número de vagas disponíveis para um curso ou a quantidade de unidades de um produto com desconto."
            },
            "autoridade": {
                "nome": "Autoridade",
                "categoria": "Confiança e Credibilidade",
                "descricao": "As pessoas confiam mais em especialistas e figuras de autoridade. Posicionar-se como uma autoridade no nicho aumenta a credibilidade.",
                "exemplo_aplicacao": "Mencionar certificações, prémios, aparições na imprensa ou anos de experiência no mercado."
            },
            "reciprocidade": {
                "nome": "Reciprocidade",
                "categoria": "Criação de Relacionamento",
                "descricao": "Quando você oferece algo de valor gratuitamente, as pessoas sentem uma inclinação natural a retribuir.",
                "exemplo_aplicacao": "Oferecer um e-book gratuito, um webinar de alta qualidade ou uma amostra do produto antes de pedir a venda."
            },
            "porque": {
                "nome": "Justificativa (Porque)",
                "categoria": "Lógica e Racional",
                "descricao": "As pessoas são mais propensas a aceitar um pedido se lhes for dada uma razão. A palavra 'porque' é um gatilho poderoso.",
                "exemplo_aplicacao": "Explicar o porquê de uma promoção estar a acontecer: 'Estamos a oferecer este desconto porque queremos celebrar o nosso aniversário.'"
            },
            "antecipacao": {
                "nome": "Antecipação",
                "categoria": "Engajamento e Desejo",
                "descricao": "Criar expectativa e entusiasmo sobre um lançamento futuro aumenta o desejo e o engajamento do público.",
                "exemplo_aplicacao": "Anunciar um novo produto semanas antes do lançamento, revelando detalhes aos poucos para criar 'hype'."
            }
        }

    def get_universal_drivers(self) -> Dict[str, Dict[str, Any]]:
        """
        Retorna a lista completa de drivers mentais universais.
        """
        return self.universal_drivers

    def generate_custom_drivers_for_avatar(self, avatar_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        (Funcionalidade Futura) Analisa os dados do avatar para sugerir e
        personalizar os drivers mentais mais eficazes.
        
        Na versão atual, retorna uma seleção padrão.
        """
        logger.info("A gerar sugestões de drivers mentais para o avatar (lógica simplificada)...")
        
        # Lógica simplificada: por agora, retorna os 3 drivers mais comuns
        # No futuro, a IA poderia analisar as 'dores' e 'desejos' do avatar para fazer esta seleção.
        suggested_drivers = {
            "prova_social": self.universal_drivers["prova_social"],
            "urgencia": self.universal_drivers["urgencia"],
            "autoridade": self.universal_drivers["autoridade"]
        }
        
        return {
            "drivers_sugeridos": suggested_drivers,
            "justificativa": "Estes são os drivers mais eficazes para a maioria dos mercados. Uma futura versão com IA poderá personalizar esta seleção."
        }

# --- Instância Global ---
# Cria uma única instância para ser usada em toda a aplicação.
mental_drivers_architect = MentalDriversArchitect()
