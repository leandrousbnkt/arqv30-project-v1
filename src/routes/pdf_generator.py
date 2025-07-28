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
            title=f"Analise de Mercado - {self.data.get('segmento', 'Relatorio')}"
        )

    def _setup_styles(self) -> dict:
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='TitleStyle', fontSize=22, leading=28, alignment=TA_CENTER, spaceAfter=20, textColor=colors.HexColor('#1a1a2e')))
        styles.add(ParagraphStyle(name='HeaderStyle', fontSize=16, leading=20, alignment=TA_LEFT, spaceAfter=16, textColor=colors.HexColor('#00d4ff'), fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='SubHeaderStyle', fontSize=12, leading=16, alignment=TA_LEFT, spaceAfter=12, textColor=colors.HexColor('#7c3aed'), fontName='Helvetica-Bold'))
        styles.add(ParagraphStyle(name='BodyStyle', fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=10))
        styles.add(ParagraphStyle(name='BulletStyle', parent=styles['BodyStyle'], firstLineIndent=0, leftIndent=18, bulletIndent=6))
        return styles

    def _add_cover_page(self):
        self.story.append(Spacer(1, 2 * inch))
        self.story.append(Paragraph("Relatório de Análise de Mercado", self.styles['TitleStyle']))
        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(Paragraph(f"Segmento: {self.data.get('segmento', 'N/A')}", self.styles['HeaderStyle']))
        if self.data.get('produto'):
            self.story.append(Paragraph(f"Produto/Serviço: {self.data.get('produto')}", self.styles['HeaderStyle']))
        self.story.append(Spacer(1, 3 * inch))
        self.story.append(Paragraph(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", self.styles['BodyStyle']))
        self.story.append(Paragraph("ARQV30 Enhanced v2.0", self.styles['BodyStyle']))
        self.story.append(PageBreak())

    def _add_section(self, title: str, content):
        if not content: return
        self.story.append(Paragraph(title, self.styles['HeaderStyle']))
        if isinstance(content, str):
            self.story.append(Paragraph(content, self.styles['BodyStyle']))
        elif isinstance(content, dict):
            for key, value in content.items():
                formatted_key = key.replace('_', ' ').capitalize()
                self.story.append(Paragraph(formatted_key, self.styles['SubHeaderStyle']))
                if isinstance(value, list):
                    for item in value:
                        self.story.append(Paragraph(f"• {item}", self.styles['BulletStyle']))
                else:
                    self.story.append(Paragraph(str(value), self.styles['BodyStyle']))
        elif isinstance(content, list):
             for item in content:
                if isinstance(item, dict):
                    for key, value in item.items():
                         self.story.append(Paragraph(f"<b>{key.replace('_', ' ').capitalize()}:</b> {value}", self.styles['BodyStyle']))
                    self.story.append(Spacer(1, 0.1 * inch))
                else:
                    self.story.append(Paragraph(f"• {item}", self.styles['BulletStyle']))
        self.story.append(Spacer(1, 0.2 * inch))

    def build_report(self):
        self._add_cover_page()
        
        self._add_section("Resumo Executivo", self.data.get('resumo_executivo'))
        self._add_section("Avatar Psicológico Profundo", self.data.get('avatar_psicologico'))
        self._add_section("Drivers Mentais", self.data.get('drivers_mentais'))
        self._add_section("Provas Visuais", self.data.get('provas_visuais'))
        self._add_section("Análise de Mercado", self.data.get('analise_mercado'))
        self._add_section("Análise da Concorrência", self.data.get('analise_concorrencia'))
        self._add_section("Estratégia de Posicionamento", self.data.get('estrategia_posicionamento'))
        self._add_section("Plano de Ação (90 Dias)", self.data.get('plano_acao_inicial'))
        
        self.doc.build(self.story)
        logger.info("✅ Relatório PDF construído com sucesso na memória.")

@pdf_bp.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    logger.info("📄 Recebido pedido para gerar relatório PDF.")
    try:
        analysis_data = request.get_json()
        if not analysis_data:
            return jsonify({'error': 'Dados da análise não fornecidos.'}), 400

        buffer = BytesIO()
        pdf_generator = PDFGenerator(analysis_data, buffer)
        pdf_generator.build_report()
        buffer.seek(0)
        
        filename = f"Analise_{analysis_data.get('segmento', 'Mercado').replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        return send_file(
            buffer, as_attachment=True, download_name=filename, mimetype='application/pdf'
        )
    except Exception as e:
        logger.error(f"❌ Erro ao gerar PDF: {e}")
        return jsonify({'error': 'Ocorreu um erro interno ao gerar o PDF.'}), 500
