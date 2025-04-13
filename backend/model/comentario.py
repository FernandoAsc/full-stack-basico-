from flask import Blueprint, request, jsonify
import sqlite3

comentario_bp = Blueprint('comentario', __name__)

@comentario_bp.route('/comentarios', methods=['GET'])
def listar_comentarios():
    """
    Lista todos os comentários
    ---
    responses:
      200:
        description: Lista de comentários
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    comentarios = c.execute("SELECT * FROM comentarios").fetchall()
    conn.close()
    return jsonify([{'id': c[0], 'autor': c[1], 'mensagem': c[2]} for c in comentarios])

@comentario_bp.route('/comentarios', methods=['POST'])
def adicionar_comentario():
    """
    Adiciona um novo comentário
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            autor:
              type: string
            mensagem:
              type: string
    responses:
      201:
        description: Comentário adicionado
    """
    data = request.json
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO comentarios (autor, mensagem) VALUES (?, ?)",
              (data['autor'], data['mensagem']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Comentário adicionado!'}), 201
