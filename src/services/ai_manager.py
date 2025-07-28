# Ficheiro: src/services/ai_manager.py

import logging
import requests
import google.generativeai as genai
from typing import Optional, Dict, Any

# Importa a configuração centralizada para aceder às chaves de API
from config import Config

logger = logging.getLogger(__name__)

class AIManager:
    """
    Gerenciador de IAs com sistema de fallback automático.
    Prioridade: Google Gemini -> Hugging Face.
    """
    def __init__(self):
        """Inicializa os clientes para os provedores de IA disponíveis."""
        self.providers = {
            'gemini': {'available': False, 'client': None},
            'huggingface': {'available': False}
        }
        
        # --- Inicialização do Google Gemini ---
        if Config.GEMINI_API_KEY:
            try:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                # Usamos um modelo mais recente e eficiente
                self.providers['gemini']['client'] = genai.GenerativeModel("gemini-1.5-flash")
                self.providers['gemini']['available'] = True
                logger.info("✅ Provedor de IA Gemini inicializado com sucesso.")
            except Exception as e:
                logger.error(f"❌ Falha ao inicializar o Gemini: {e}")
        else:
            logger.warning("⚠️ Chave de API do Gemini não configurada.")

        # --- Verificação do Hugging Face ---
        if Config.HUGGINGFACE_API_KEY:
            self.providers['huggingface']['available'] = True
            logger.info("✅ Provedor de IA Hugging Face configurado com sucesso.")
        else:
            logger.warning("⚠️ Chave de API do Hugging Face não configurada.")

    def _generate_with_gemini(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando o Google Gemini como provedor principal."""
        try:
            client = self.providers['gemini']['client']
            
            # Configurações de geração para análises detalhadas
            generation_config = {
                'temperature': 0.7,
                'top_p': 0.95,
                'top_k': 64,
                'max_output_tokens': max_tokens,
            }
            
            # Configurações de segurança para evitar bloqueios desnecessários
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
            ]

            response = client.generate_content(
                prompt,
                generation_config=generation_config,
                safety_settings=safety_settings
            )
            
            if response.text:
                logger.info(f"✅ Análise gerada com sucesso pelo Gemini.")
                return response.text
            else:
                # Se a resposta estiver bloqueada, o motivo estará em 'prompt_feedback'
                logger.warning(f"⚠️ Gemini retornou uma resposta vazia. Feedback: {response.prompt_feedback}")
                return None

        except Exception as e:
            logger.error(f"❌ Erro ao gerar análise com o Gemini: {e}")
            return None

    def _generate_with_huggingface(self, prompt: str, max_tokens: int) -> Optional[str]:
        """Gera conteúdo usando a Hugging Face Inference API como fallback."""
        try:
            # Usa o modelo definido na configuração, com um fallback padrão
            model_name = Config.HUGGINGFACE_MODEL_NAME or "mistralai/Mistral-7B-Instruct-v0.2"
            api_url = f"https://api-inference.huggingface.co/models/{model_name}"
            headers = {"Authorization": f"Bearer {Config.HUGGINGFACE_API_KEY}"}

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": max_tokens,
                    "temperature": 0.7,
                    "return_full_text": False,
                }
            }
            
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                content = result[0]['generated_text']
                logger.info(f"✅ Análise gerada com sucesso pelo Hugging Face ({model_name}).")
                return content
            else:
                logger.error(f"❌ Erro na API do Hugging Face: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            logger.error(f"❌ Erro ao gerar análise com o Hugging Face: {e}")
            return None

    def generate_analysis(self, prompt: str, max_tokens: int = 8192) -> Optional[str]:
        """
        Orquestra a geração da análise, tentando o provedor primário (Gemini)
        e recorrendo ao fallback (Hugging Face) se necessário.
        """
        logger.info("🚀 Iniciando geração de análise com o AI Manager...")
        
        # 1. Tenta o provedor primário: Gemini
        if self.providers['gemini']['available']:
            logger.info("🧠 A tentar provedor primário: Gemini...")
            result = self._generate_with_gemini(prompt, max_tokens)
            if result:
                return result
            logger.warning("⚠️ Gemini falhou ou retornou resposta vazia. A tentar fallback...")

        # 2. Se o primário falhar, tenta o fallback: Hugging Face
        if self.providers['huggingface']['available']:
            logger.info("🧠 A tentar provedor de fallback: Hugging Face...")
            result = self._generate_with_huggingface(prompt, max_tokens)
            if result:
                return result
            logger.error("❌ Fallback com Hugging Face também falhou.")

        # 3. Se todos falharem
        logger.critical("❌ Todos os provedores de IA falharam. Não foi possível gerar a análise.")
        return None

# --- Instância Global ---
# Cria uma única instância do AIManager para ser usada em toda a aplicação.
ai_manager = AIManager()
