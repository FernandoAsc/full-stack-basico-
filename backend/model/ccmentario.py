from flask import Blueprint, request, jsonify
from base import get_db_connection
from logger import logger

comentario_bp = Blueprint('comentario', __name__)

@comentario_bp.route('/comentarios', methods=['POST'])
def adicionar_comentario():
    """
    Adiciona um comentário sobre um pet
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            pet_id:
              type: integer
            texto:
              type: string
    responses:
      201:
        description: Comentário adicionado
    """
    data = request.json
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO comentarios (pet_id, texto) VALUES (?, ?)", (data['pet_id'], data['texto']))
    conn.commit()
    conn.close()
    logger.info(f"Comentário adicionado para o pet {data['pet_id']}")
    return jsonify({'message': 'Comentário adicionado com sucesso!'}), 201
