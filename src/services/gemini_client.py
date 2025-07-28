# Ficheiro: src/services/gemini_client.py

import logging
import google.generativeai as genai
from typing import Optional

# Importa a configuração centralizada para aceder à chave de API
from config import Config

logger = logging.getLogger(__name__)

class GeminiClient:
    """
    Cliente robusto para interagir com a API do Google Gemini.
    Centraliza a configuração e a lógica de geração de conteúdo.
    """
    def __init__(self):
        """
        Configura o cliente Gemini ao ser inicializado.
        """
        self.model = None
        if Config.GEMINI_API_KEY:
            try:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                # Utiliza o modelo 'gemini-1.5-flash', que é rápido e eficiente para tarefas de texto.
                self.model = genai.GenerativeModel("gemini-1.5-flash")
                logger.info("✅ Cliente Gemini inicializado com sucesso.")
            except Exception as e:
                logger.error(f"❌ Falha ao configurar a API do Gemini: {e}")
        else:
            logger.warning("⚠️ Chave de API do Gemini não foi encontrada. O serviço Gemini está desativado.")

    def generate_content(self, prompt: str, max_tokens: int = 8192) -> Optional[str]:
        """
        Envia um prompt para o modelo Gemini e retorna a resposta de texto.

        Args:
            prompt: O texto de entrada para a IA.
            max_tokens: O número máximo de tokens na resposta.

        Returns:
            A resposta de texto gerada pela IA ou None em caso de falha.
        """
        if not self.model:
            logger.error("❌ Não é possível gerar conteúdo: o modelo Gemini não foi inicializado.")
            return None

        try:
            # Configurações de geração para obter respostas criativas e detalhadas
            generation_config = {
                'temperature': 0.7,
                'top_p': 0.95,
                'top_k': 64,
                'max_output_tokens': max_tokens,
            }
            
            # Configurações de segurança para evitar bloqueios por conteúdo sensível
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
            ]

            logger.info("🤖 A enviar pedido para a API do Gemini...")
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config,
                safety_settings=safety_settings
            )
            
            if response.text:
                logger.info("✅ Resposta recebida com sucesso do Gemini.")
                return response.text
            else:
                logger.warning(f"⚠️ Gemini retornou uma resposta vazia. Feedback de segurança: {response.prompt_feedback}")
                return None

        except Exception as e:
            logger.error(f"❌ Ocorreu um erro na chamada à API do Gemini: {e}")
            return None

# --- Instância Global ---
# Cria uma única instância do GeminiClient para ser usada em toda a aplicação.
gemini_client = GeminiClient()
