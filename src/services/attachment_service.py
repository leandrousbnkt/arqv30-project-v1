# Ficheiro: src/services/attachment_service.py

import os
import logging
import mimetypes
from typing import Dict, Optional
from werkzeug.datastructures import FileStorage
import PyPDF2
import pandas as pd
from docx import Document
import json

logger = logging.getLogger(__name__)

class AttachmentService:
    """
    Serviço para processar ficheiros anexados (PDF, DOCX, XLSX, etc.)
    e extrair o seu conteúdo de texto para ser usado na análise.
    """
    
    def __init__(self):
        """Inicializa o serviço de anexos."""
        # Define a pasta para uploads temporários dentro da estrutura do projeto.
        self.upload_folder = os.path.join(os.path.dirname(__file__), '..', 'uploads')
        os.makedirs(self.upload_folder, exist_ok=True)
        
        # Mapeia os tipos MIME para os métodos de extração correspondentes.
        self.supported_types = {
            'application/pdf': self._extract_pdf_content,
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': self._extract_docx_content,
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': self._extract_excel_content,
            'text/csv': self._extract_csv_content,
            'text/plain': self._extract_text_content,
            'application/json': self._extract_json_content
        }
        logger.info("✅ Attachment Service inicializado.")

    def _extract_pdf_content(self, file_path: str) -> Optional[str]:
        """Extrai texto de um ficheiro PDF."""
        try:
            content = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    content += page.extract_text() + "\n"
            return content.strip()
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do PDF: {e}")
            return None

    def _extract_docx_content(self, file_path: str) -> Optional[str]:
        """Extrai texto de um ficheiro DOCX."""
        try:
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs]).strip()
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do DOCX: {e}")
            return None

    def _extract_excel_content(self, file_path: str) -> Optional[str]:
        """Extrai dados de um ficheiro Excel (XLSX) como texto."""
        try:
            excel_file = pd.ExcelFile(file_path)
            content = ""
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                content += f"--- Folha: {sheet_name} ---\n"
                content += df.to_string(index=False) + "\n\n"
            return content.strip()
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do Excel: {e}")
            return None

    def _extract_csv_content(self, file_path: str) -> Optional[str]:
        """Extrai dados de um ficheiro CSV como texto."""
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
            return df.to_string(index=False)
        except UnicodeDecodeError:
            # Tenta com um encoding diferente se o UTF-8 falhar
            df = pd.read_csv(file_path, encoding='latin-1')
            return df.to_string(index=False)
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do CSV: {e}")
            return None
            
    def _extract_text_content(self, file_path: str) -> Optional[str]:
        """Extrai conteúdo de um ficheiro de texto simples."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo de ficheiro de texto: {e}")
            return None

    def _extract_json_content(self, file_path: str) -> Optional[str]:
        """Lê e formata um ficheiro JSON como uma string de texto."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Converte o JSON para uma string formatada
                return json.dumps(data, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"❌ Erro ao extrair conteúdo do JSON: {e}")
            return None

    def process_attachment(self, file: FileStorage) -> Dict[str, any]:
        """
        Processa um ficheiro enviado, extraindo o seu conteúdo de texto.
        """
        if not file or not file.filename:
            return {'success': False, 'error': 'Ficheiro inválido.'}

        # Tenta adivinhar o tipo de ficheiro se não estiver presente
        mime_type = file.content_type or mimetypes.guess_type(file.filename)[0]
        
        if mime_type not in self.supported_types:
            return {'success': False, 'error': f'Tipo de ficheiro não suportado: {mime_type}'}

        # Guarda o ficheiro temporariamente para processamento
        temp_path = os.path.join(self.upload_folder, file.filename)
        file.save(temp_path)

        try:
            # Chama o método de extração correto com base no tipo de ficheiro
            extractor_method = self.supported_types[mime_type]
            content = extractor_method(temp_path)
            
            if content:
                logger.info(f"✅ Conteúdo extraído com sucesso de '{file.filename}'.")
                return {
                    'success': True,
                    'filename': file.filename,
                    'content_type': mime_type,
                    'content': content
                }
            else:
                return {'success': False, 'error': 'Falha ao extrair conteúdo do ficheiro.'}

        finally:
            # Garante que o ficheiro temporário é sempre removido após o processamento
            if os.path.exists(temp_path):
                os.remove(temp_path)

# --- Instância Global ---
attachment_service = AttachmentService()
