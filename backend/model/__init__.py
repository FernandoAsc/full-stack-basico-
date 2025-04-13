from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    CORS(app)
    Swagger(app)

    from .base import init_db
    from .comentario import comentario_bp

    init_db()
    app.register_blueprint(comentario_bp)

    return app
