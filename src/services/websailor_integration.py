# Ficheiro: src/services/websailor_integration.py

import logging
from typing import Dict, Any

# Importa o cliente principal do Hugging Face e a configuração
from .huggingface_client import huggingface_client
from config import Config

logger = logging.getLogger(__name__)

class WebSailorIntegration:
    """
    Serviço de integração para o modelo WebSailor (Alibaba-NLP/WebSailor).
    
    Na arquitetura refatorizada, este serviço atua como um wrapper que utiliza
    o cliente principal do Hugging Face para aceder ao modelo WebSailor.
    A sua função é demonstrar como um modelo específico pode ser chamado,
    mantendo a lógica de comunicação centralizada no huggingface_client.
    """
    def __init__(self):
        """
        Inicializa a integração, verificando se o modelo WebSailor está configurado.
        """
        self.model_name = Config.WEBSAILOR_MODEL_NAME
        logger.info(f"✅ WebSailor Integration inicializado. Modelo configurado: {self.model_name}")

    def perform_web_analysis(self, prompt: str, max_tokens: int = 2048) -> str:
        """
        Executa uma análise utilizando o modelo WebSailor através da API do Hugging Face.
        
        Args:
            prompt: O prompt para a análise.
            max_tokens: O número máximo de tokens para a resposta.
            
        Returns:
            A resposta do modelo ou uma mensagem de erro.
        """
        logger.info(f"A iniciar análise com o modelo WebSailor: {self.model_name}")
        
        # Para usar este serviço, a lógica seria chamar o huggingface_client
        # forçando-o a usar o modelo WebSailor. No entanto, para manter a
        # simplicidade, a recomendação é configurar o WEBSAILOR_MODEL_NAME
        # como o HUGGINGFACE_MODEL_NAME principal no ficheiro .env.
        
        # Exemplo de como seria chamado (atualmente desativado para não duplicar lógica):
        # return huggingface_client.generate_content_with_specific_model(
        #     prompt=prompt,
        #     model_name=self.model_name,
        #     max_tokens=max_tokens
        # )
        
        return (
            "Funcionalidade Placeholder: A integração do WebSailor é gerida diretamente "
            "pelo HuggingFaceClient. Para usar o modelo WebSailor, defina a variável "
            "'HUGGINGFACE_MODEL_NAME' no seu ficheiro .env para 'Alibaba-NLP/WebSailor'."
        )

# --- Instância Global ---
# Cria uma única instância para ser usada em toda a aplicação, se necessário.
websailor_integration = WebSailorIntegration()
