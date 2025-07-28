# Ficheiro: src/database.py

import logging
from typing import Dict, List, Optional, Any
from supabase.client import create_client, Client

# Importa a configuração centralizada
from config import Config

logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    Gerenciador de conexão e operações com o banco de dados Supabase.
    Esta classe centraliza toda a lógica de interação com o banco.
    """
    
    def __init__(self):
        """
        Inicializa a conexão com o Supabase usando as credenciais do ficheiro de configuração.
        """
        self.client: Optional[Client] = None
        
        # --- CORREÇÃO AQUI ---
        # Limpa as chaves para remover espaços em branco ou quebras de linha acidentais
        supabase_url = Config.SUPABASE_URL.strip() if Config.SUPABASE_URL else None
        supabase_key = Config.SUPABASE_ANON_KEY.strip() if Config.SUPABASE_ANON_KEY else None

        if supabase_url and supabase_key:
            try:
                self.client = create_client(supabase_url, supabase_key)
                logger.info("✅ Conexão com Supabase inicializada com sucesso.")
            except Exception as e:
                logger.error(f"❌ Falha ao inicializar o cliente Supabase: {e}")
        else:
            logger.warning("⚠️ Credenciais do Supabase não encontradas. O banco de dados está desativado.")

    def test_connection(self) -> bool:
        """
        Testa a conexão com o banco de dados fazendo uma consulta simples.
        Retorna True se a conexão for bem-sucedida, False caso contrário.
        """
        if not self.client:
            return False
        try:
            self.client.table('analyses').select('id').limit(1).execute()
            logger.info("✅ Teste de conexão com o banco de dados bem-sucedido.")
            return True
        except Exception as e:
            logger.error(f"❌ Erro ao testar a conexão com o banco de dados: {e}")
            return False

    def create_analysis(self, analysis_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Cria um novo registo de análise na tabela 'analyses'.
        """
        if not self.client:
            logger.error("❌ Não é possível criar análise: cliente do banco de dados não inicializado.")
            return None
        
        try:
            response = self.client.table('analyses').insert(analysis_data).execute()
            
            # A API v2 do Supabase pode não ter 'error' no objeto de resposta de sucesso
            if response.data and len(response.data) > 0:
                created_record = response.data[0]
                logger.info(f"💾 Análise guardada com sucesso no banco de dados. ID: {created_record.get('id')}")
                return created_record
            else:
                # Tenta obter o erro de uma forma compatível
                error_message = getattr(response, 'error', 'Nenhuma informação de erro disponível.')
                logger.error(f"❌ Falha ao guardar a análise. Resposta do Supabase: {error_message}")
                return None
        except Exception as e:
            logger.error(f"❌ Erro crítico ao criar análise no banco de dados: {e}")
            return None

    def get_analysis(self, analysis_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtém um registo de análise específico pelo seu ID.
        """
        if not self.client:
            return None
        try:
            response = self.client.table('analyses').select('*').eq('id', analysis_id).execute()
            if response.data:
                return response.data[0]
            return None
        except Exception as e:
            logger.error(f"❌ Erro ao obter análise ID {analysis_id}: {e}")
            return None

    def list_analyses(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Lista as análises mais recentes guardadas no banco de dados.
        """
        if not self.client:
            return []
        try:
            response = self.client.table('analyses').select('id, segmento, produto, created_at').order('created_at', desc=True).limit(limit).execute()
            return response.data if response.data else []
        except Exception as e:
            logger.error(f"❌ Erro ao listar análises: {e}")
            return []

# --- Instância Global ---
db_manager = DatabaseManager()
