# Ficheiro: src/routes/pdf_generator.py

import logging
from flask import Blueprint, request, jsonify, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from io import BytesIO
from datetime import datetime
import json

logger = logging.getLogger(__name__)

pdf_bp = Blueprint('pdf', __name__)

class PDFGenerator:
    def __init__(self, analysis_data: dict, buffer: BytesIO):
        self.buffer = buffer
        self.data = analysis_data
        self.story = []
        self.styles = self._setup_styles()
        self.doc = SimpleDocTemplate(
            self.buffer, pagesize=A4, rightMargin=inch, leftMargin=inch,
            topMargin=inch, bottomMargin=inch,
            title=f"Análise Psicológica Profunda - {self.data.get('segmento', 'Relatório')}"
        )

    def _setup_styles(self) -> dict:
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='TitleStyle', fontSize=24, leading=30, alignment=TA_CENTER, spaceAfter=24, textColor=colors.HexColor('#0f0f1a'), fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='HeaderStyle', fontSize=18, leading=22, alignment=TA_LEFT, spaceAfter=18, textColor=colors.HexColor('#00d4ff'), fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='SubHeaderStyle', fontSize=14, leading=18, alignment=TA_LEFT, spaceAfter=14, textColor=colors.HexColor('#7c3aed'), fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='BodyStyle', fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=10))
        styles.add(ParagraphStyle(name='BulletStyle', parent=styles['BodyStyle'], firstLineIndent=0, leftIndent=18, bulletIndent=6))
        styles.add(ParagraphStyle(name='CodeStyle', fontSize=9, leading=12, alignment=TA_LEFT, spaceAfter=8, textColor=colors.HexColor('#666666'), fontName='Courier'))
        styles.add(ParagraphStyle(name='QuoteStyle', fontSize=11, leading=15, alignment=TA_LEFT, spaceAfter=12, textColor=colors.HexColor('#444444'), leftIndent=20, rightIndent=20))
        return styles

    def _add_cover_page(self):
        self.story.append(Spacer(1, 2 * inch))
        self.story.append(Paragraph("Relatório de Análise Psicológica Profunda", self.styles['TitleStyle']))
        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(Paragraph(f"Segmento: {self.data.get('segmento', 'N/A')}", self.styles['HeaderStyle']))
        if self.data.get('produto'):
            self.story.append(Paragraph(f"Produto/Serviço: {self.data.get('produto')}", self.styles['HeaderStyle']))
        if self.data.get('preco'):
            self.story.append(Paragraph(f"Preço: R$ {self.data.get('preco')}", self.styles['HeaderStyle']))
        self.story.append(Spacer(1, 3 * inch))
        self.story.append(Paragraph(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", self.styles['BodyStyle']))
        self.story.append(Paragraph("ARQV30 Enhanced v2.0", self.styles['BodyStyle']))
        self.story.append(Paragraph("Sistema de Análise Psicológica Avançada", self.styles['BodyStyle']))
        self.story.append(PageBreak())

    def _add_section(self, title: str, content, level=1):
        if not content: return
        
        style = self.styles['HeaderStyle'] if level == 1 else self.styles['SubHeaderStyle']
        self.story.append(Paragraph(title, style))
        
        if isinstance(content, str):
            self.story.append(Paragraph(content, self.styles['BodyStyle']))
        elif isinstance(content, dict):
            self._add_dict_content(content)
        elif isinstance(content, list):
            self._add_list_content(content)
            
        self.story.append(Spacer(1, 0.2 * inch))

    def _add_dict_content(self, content_dict):
        """Adiciona conteúdo de dicionário de forma estruturada."""
        for key, value in content_dict.items():
            formatted_key = key.replace('_', ' ').title()
            
            if isinstance(value, dict):
                self.story.append(Paragraph(formatted_key, self.styles['SubHeaderStyle']))
                self._add_dict_content(value)
            elif isinstance(value, list):
                self.story.append(Paragraph(formatted_key, self.styles['SubHeaderStyle']))
                self._add_list_content(value)
            else:
                self.story.append(Paragraph(f"<b>{formatted_key}:</b> {value}", self.styles['BodyStyle']))

    def _add_list_content(self, content_list):
        """Adiciona conteúdo de lista de forma estruturada."""
        for item in content_list:
            if isinstance(item, dict):
                for key, value in item.items():
                    formatted_key = key.replace('_', ' ').title()
                    if isinstance(value, (list, dict)):
                        self.story.append(Paragraph(f"<b>{formatted_key}:</b>", self.styles['BodyStyle']))
                        if isinstance(value, list):
                            self._add_list_content(value)
                        else:
                            self._add_dict_content(value)
                    else:
                        self.story.append(Paragraph(f"<b>{formatted_key}:</b> {value}", self.styles['BodyStyle']))
                self.story.append(Spacer(1, 0.1 * inch))
            else:
                self.story.append(Paragraph(f"• {item}", self.styles['BulletStyle']))

    def build_report(self):
        self._add_cover_page()
        
        # Resumo Executivo
        self._add_section("Resumo Executivo", self.data.get('resumo_executivo'))
        
        # Avatar Psicológico Profundo
        avatar_data = self.data.get('avatar_psicologico_profundo') or self.data.get('avatar_psicologico')
        if avatar_data:
            self._add_section("Avatar Psicológico Profundo", avatar_data)
        
        # Drivers Mentais Customizados
        drivers_data = self.data.get('drivers_mentais_customizados') or self.data.get('drivers_mentais')
        if drivers_data:
            self._add_section("Drivers Mentais Customizados", drivers_data)
        
        # Mapeamento de Objeções
        self._add_section("Mapeamento de Objeções", self.data.get('mapeamento_objecoes'))
        
        # Arsenal de Provas Visuais
        provas_data = self.data.get('arsenal_provas_visuais') or self.data.get('provas_visuais')
        if provas_data:
            self._add_section("Arsenal de Provas Visuais", provas_data)
        
        # Estratégia de Pré-Pitch
        self._add_section("Estratégia de Pré-Pitch", self.data.get('estrategia_pre_pitch'))
        
        # Análise de Mercado
        self._add_section("Análise de Mercado", self.data.get('analise_mercado'))
        
        # Análise da Concorrência
        self._add_section("Análise da Concorrência", self.data.get('analise_concorrencia'))
        
        # Estratégia de Posicionamento
        self._add_section("Estratégia de Posicionamento", self.data.get('estrategia_posicionamento'))
        
        # Plano de Ação (90 Dias)
        plano_data = self.data.get('plano_acao_90_dias') or self.data.get('plano_acao_inicial')
        if plano_data:
            self._add_section("Plano de Ação (90 Dias)", plano_data)
        
        # Plano de Implementação
        self._add_section("Plano de Implementação", self.data.get('plano_implementacao'))
        
        # Adiciona página com dados técnicos (opcional)
        if self.data.get('database_id'):
            self.story.append(PageBreak())
            self.story.append(Paragraph("Informações Técnicas", self.styles['HeaderStyle']))
            self.story.append(Paragraph(f"ID da Análise: {self.data.get('database_id')}", self.styles['BodyStyle']))
            self.story.append(Paragraph(f"Data de Geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", self.styles['BodyStyle']))
        
        self.doc.build(self.story)
        logger.info("✅ Relatório PDF psicológico construído com sucesso.")

@pdf_bp.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    logger.info("📄 Recebido pedido para gerar relatório PDF psicológico.")
    try:
        analysis_data = request.get_json()
        if not analysis_data:
            return jsonify({'error': 'Dados da análise não fornecidos.'}), 400

        buffer = BytesIO()
        pdf_generator = PDFGenerator(analysis_data, buffer)
        pdf_generator.build_report()
        buffer.seek(0)
        
        segmento = analysis_data.get('segmento', 'Mercado').replace(' ', '_').replace('/', '_')
        filename = f"Analise_Psicologica_{segmento}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        
        return send_file(
            buffer, as_attachment=True, download_name=filename, mimetype='application/pdf'
        )
    except Exception as e:
        logger.error(f"❌ Erro ao gerar PDF psicológico: {e}")
        return jsonify({'error': 'Ocorreu um erro interno ao gerar o PDF.'}), 500
