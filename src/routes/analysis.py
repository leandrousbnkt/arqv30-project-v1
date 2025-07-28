# Ficheiro: src/routes/analysis.py

import logging
from flask import Blueprint, request, jsonify
import traceback

# Importa o motor de análise principal e o gestor do banco de dados
from services.enhanced_analysis_engine import enhanced_analysis_engine
from database import db_manager

logger = logging.getLogger(__name__)

# Cria um Blueprint para organizar as rotas relacionadas com a análise.
analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze', methods=['POST'])
def analyze_market():
    """
    Endpoint principal para receber os dados do formulário, iniciar o processo
    de análise e retornar o relatório completo em formato JSON.
    """
    logger.info("🚀 Recebido novo pedido de análise no endpoint /api/analyze.")
    
    try:
        # --- Passo 1: Obter e Validar os Dados de Entrada ---
        data = request.get_json()
        if not data:
            logger.warning("⚠️ Pedido recebido sem dados JSON.")
            return jsonify({'error': 'Corpo do pedido vazio. Envie os dados em formato JSON.'}), 400

        if not data.get('segmento'):
            logger.warning("⚠️ Pedido de análise sem o campo obrigatório 'segmento'.")
            return jsonify({'error': 'O campo "segmento" é obrigatório.'}), 400

        logger.info(f"Dados recebidos para análise: {data}")

        # --- Passo 2: Chamar o Motor de Análise ---
        analysis_result = enhanced_analysis_engine.generate_comprehensive_analysis(data)

        if not analysis_result or analysis_result.get("error"):
            logger.error(f"❌ O motor de análise retornou um erro: {analysis_result.get('error')}")
            return jsonify(analysis_result), 500

        # --- Passo 3: Preparar Dados e Guardar no Banco de Dados ---
        db_data_to_save = data.copy()
        db_data_to_save['comprehensive_analysis'] = analysis_result
        
        # --- CORREÇÃO AQUI ---
        # Converte campos de texto vazios para None para evitar erros de tipo numérico no banco de dados.
        if db_data_to_save.get('preco') == '':
            db_data_to_save['preco'] = None
        
        created_record = db_manager.create_analysis(db_data_to_save)
        
        if created_record and created_record.get('id'):
            analysis_result['database_id'] = created_record['id']
            logger.info(f"✅ Análise guardada com sucesso no banco de dados com ID: {created_record['id']}")
        else:
            logger.warning("⚠️ A análise foi gerada, mas falhou ao ser guardada no banco de dados.")
            analysis_result['database_status'] = "failed_to_save"

        # --- Passo 4: Retornar a Resposta de Sucesso ---
        logger.info("✅ Análise concluída e pronta para ser enviada ao cliente.")
        return jsonify(analysis_result), 200

    except Exception as e:
        logger.critical(f"❌ Erro inesperado no endpoint de análise: {e}")
        logger.critical(traceback.format_exc())
        return jsonify({'error': 'Ocorreu um erro inesperado no servidor.'}), 500
