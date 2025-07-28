# Ficheiro: src/services/huggingface_client.py

import logging
import requests
from typing import Optional

# Importa a configuração centralizada para aceder à chave de API e nomes de modelos
from config import Config

logger = logging.getLogger(__name__)

class HuggingFaceClient:
    """
    Cliente para interagir com a Hugging Face Inference API.
    Funciona como um fallback robusto para a geração de texto.
    """
    def __init__(self):
        """
        Verifica se a chave de API do Hugging Face está disponível.
        """
        self.api_key = Config.HUGGINGFACE_API_KEY
        if self.api_key:
            logger.info("✅ Cliente Hugging Face inicializado com sucesso.")
        else:
            logger.warning("⚠️ Chave de API do Hugging Face não foi encontrada. O serviço está desativado.")

    def generate_content(self, prompt: str, max_tokens: int = 4096) -> Optional[str]:
        """
        Envia um prompt para um modelo na Hugging Face Inference API.

        Args:
            prompt: O texto de entrada para a IA.
            max_tokens: O número máximo de novos tokens a serem gerados.

        Returns:
            A resposta de texto gerada pela IA ou None em caso de falha.
        """
        if not self.api_key:
            logger.error("❌ Não é possível gerar conteúdo: a chave da API do Hugging Face não está configurada.")
            return None

        # Usa o modelo definido na configuração, com um fallback para um modelo popular e gratuito.
        model_name = Config.HUGGINGFACE_MODEL_NAME or "mistralai/Mistral-7B-Instruct-v0.2"
        api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        # Payload para a API
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "temperature": 0.7,
                "top_p": 0.95,
                "return_full_text": False, # Retorna apenas o texto gerado, não o prompt
            }
        }

        logger.info(f"🤖 A enviar pedido para a API do Hugging Face (Modelo: {model_name})...")
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=90) # Timeout mais longo para modelos maiores

            if response.status_code == 200:
                result = response.json()
                # A resposta é uma lista, o texto está no primeiro elemento
                content = result[0]['generated_text']
                logger.info(f"✅ Resposta recebida com sucesso do Hugging Face.")
                return content.strip()
            elif response.status_code == 503:
                 logger.error(f"❌ Erro na API do Hugging Face: Modelo '{model_name}' está a carregar. Tente novamente mais tarde.")
                 return None
            else:
                logger.error(f"❌ Erro na API do Hugging Face: {response.status_code} - {response.text}")
                return None

        except requests.RequestException as e:
            logger.error(f"❌ Ocorreu um erro de rede na chamada à API do Hugging Face: {e}")
            return None
        except Exception as e:
            logger.error(f"❌ Ocorreu um erro inesperado ao processar a resposta do Hugging Face: {e}")
            return None

# --- Instância Global ---
# Cria uma única instância do HuggingFaceClient para ser usada em toda a aplicação.
huggingface_client = HuggingFaceClient()
