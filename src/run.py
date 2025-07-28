# Ficheiro: src/run.py

import os
import sys
import logging
from datetime import datetime
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import traceback

# --- CORREÇÃO AQUI ---
# Adiciona o diretório raiz do projeto ao path do Python.
# Isto permite que o script encontre o ficheiro 'config.py' que está na pasta anterior.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora a importação do config vai funcionar
from config import Config

# --- Configuração de Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)

def create_app():
    """
    Cria e configura a instância principal da aplicação Flask.
    """
    # O Flask procura as pastas 'templates' e 'static' a partir da localização do 'run.py'
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(Config)
    
    CORS(app, origins=Config.CORS_ORIGINS.split(','))

    # --- Importação e Registo de Blueprints ---
    try:
        from routes.analysis import analysis_bp
        from routes.user import user_bp
        from routes.pdf_generator import pdf_bp

        app.register_blueprint(analysis_bp, url_prefix='/api')
        app.register_blueprint(user_bp, url_prefix='/api')
        app.register_blueprint(pdf_bp, url_prefix='/api')
        
        @app.route('/generate-pdf', methods=['POST'])
        def generate_pdf_compat():
            from routes.pdf_generator import generate_pdf
            return generate_pdf()

        logger.info("✅ Blueprints de rotas registados com sucesso.")
    except ImportError as e:
        logger.error(f"❌ Falha ao importar ou registar blueprints: {e}")

    # --- Rotas Principais ---
    @app.route('/')
    def index():
        return render_template('enhanced_index.html')

    @app.route('/api/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': '2.0.0'
        })

    # --- Handlers de Erro Globais ---
    @app.errorhandler(404)
    def not_found_error(error):
        logger.warning(f"Rota não encontrada: {error}")
        return jsonify({
            'error': 'Recurso não encontrado',
            'message': 'O endpoint solicitado não existe.'
        }), 404

    @app.errorhandler(Exception)
    def global_exception_handler(error):
        logger.error(f"Erro não tratado na aplicação: {error}")
        logger.error(traceback.format_exc())
        return jsonify({
            'error': 'Erro Interno do Servidor',
            'message': 'Ocorreu um erro inesperado.'
        }), 500

    return app

if __name__ == '__main__':
    try:
        app = create_app()
        
        host = os.getenv('HOST', '0.0.0.0')
        port = int(os.getenv('PORT', 5000))
        debug = Config.FLASK_ENV == 'development'
        
        logger.info(f"🚀 Iniciando servidor ARQV30 Enhanced v2.0")
        logger.info(f"   - Ambiente: {Config.FLASK_ENV}")
        logger.info(f"   - Servidor a correr em: http://{host}:{port}")
        logger.info(f"   - Modo Debug: {'Ativado' if debug else 'Desativado'}")
        
        app.run(host=host, port=port, debug=debug)
        
    except Exception as e:
        logger.critical(f"❌ Falha crítica ao iniciar a aplicação: {e}")
        logger.critical(traceback.format_exc())
