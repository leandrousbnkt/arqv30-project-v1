# Ficheiro: config.py

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do ficheiro .env
load_dotenv()

class Config:
    """
    Classe de configuração central para a aplicação ARQV30.
    Lê todas as chaves de API e configurações a partir de variáveis de ambiente,
    garantindo que nenhuma informação sensível esteja no código.
    """
    # --- Configurações Gerais da Aplicação Flask ---
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY")
    # --- CORREÇÃO AQUI ---
    # Adiciona a variável CORS_ORIGINS que estava em falta.
    # O valor "*" permite que qualquer origem aceda à sua API (bom para desenvolvimento).
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

    # --- Configurações do Banco de Dados (Supabase) ---
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")

    # --- Chaves de API de Inteligência Artificial ---
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    
    # --- Modelos de IA (pode ser configurado via .env se necessário) ---
    HUGGINGFACE_MODEL_NAME = os.getenv("HUGGINGFACE_MODEL_NAME", "meta-llama/Meta-Llama-3-8B")
    WEBSAILOR_MODEL_NAME = os.getenv("WEBSAILOR_MODEL_NAME", "Alibaba-NLP/WebSailor")

    # --- Chaves de API dos Serviços de Busca (Fontes de Dados Gratuitas) ---
    GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_KEY")
    GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
    JINA_API_KEY = os.getenv("JINA_API_KEY")
    SCRAPINGANT_API_KEY = os.getenv("SCRAPINGANT_API_KEY")
