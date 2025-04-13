from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import sqlite3

app = Flask(__name__)
CORS(app)
Swagger(app)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS pets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    idade INTEGER
                )""")
    conn.commit()
    conn.close()

init_db()

@app.route('/pets', methods=['GET'])
def listar_pets():
    """
    Lista todos os pets cadastrados
    ---
    responses:
      200:
        description: Lista de pets
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    pets = c.execute("SELECT * FROM pets").fetchall()
    conn.close()
    return jsonify([{'id': p[0], 'nome': p[1], 'tipo': p[2], 'idade': p[3]} for p in pets])

@app.route('/pets', methods=['POST'])
def cadastrar_pet():
    """
    Cadastra um novo pet
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            nome:
              type: string
            tipo:
              type: string
            idade:
              type: integer
    responses:
      201:
        description: Pet criado com sucesso
    """
    data = request.json
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO pets (nome, tipo, idade) VALUES (?, ?, ?)",
              (data['nome'], data['tipo'], data['idade']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Pet cadastrado!'}), 201

@app.route('/pets/<int:id>', methods=['DELETE'])
def deletar_pet():
    """
    Deleta um pet pelo ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Pet deletado
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM pets WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Pet deletado.'})

if __name__ == '__main__':
    app.run(debug=True)
