# Ficheiro: src/routes/user.py

import logging
import uuid
from datetime import datetime
from flask import Blueprint, request, jsonify, session

logger = logging.getLogger(__name__)

# Cria um Blueprint para organizar as rotas relacionadas com o utilizador.
user_bp = Blueprint('user', __name__)

@user_bp.route('/session/new', methods=['POST'])
def create_session():
    """
    Cria uma nova sessão de utilizador, gerando um ID de sessão único.
    Este endpoint pode ser chamado pelo frontend quando a página carrega.
    """
    try:
        # Gera um ID de sessão universalmente único (UUID).
        session_id = str(uuid.uuid4())
        
        # Guarda o ID na sessão do Flask, que é gerida por cookies no navegador.
        session['session_id'] = session_id
        session['created_at'] = datetime.now().isoformat()
        
        logger.info(f"✅ Nova sessão de utilizador criada: {session_id}")
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'created_at': session['created_at'],
            'message': 'Sessão criada com sucesso.'
        }), 201

    except Exception as e:
        logger.error(f"❌ Erro ao criar sessão: {e}")
        return jsonify({'error': 'Erro interno ao criar sessão.'}), 500

@user_bp.route('/session/info', methods=['GET'])
def get_session_info():
    """
    Retorna informações sobre a sessão ativa atual.
    """
    session_id = session.get('session_id')
    
    if not session_id:
        return jsonify({'error': 'Nenhuma sessão ativa encontrada.'}), 404
        
    session_info = {
        'session_id': session_id,
        'created_at': session.get('created_at'),
        'active': True
    }
    
    return jsonify(session_info), 200

