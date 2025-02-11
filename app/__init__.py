from flask import Flask
from flask_restx import Api  # Importar Api de Flask-RESTx


def create_app():
    app = Flask(__name__)

    # Registrar tu blueprint existente
    from app.routes.frases import frases_bp
    app.register_blueprint(frases_bp, url_prefix="/api/frases")

    # Crear la instancia de Flask-RESTx
    api = Api(app, title="Listening Practice API", version="1.0", description="API for listening practice")

    # Registrar namespaces (vamos a definirlos más adelante)
    from app.routes.audio import ns as audio_ns
    from app.routes.respuesta import ns as respuesta_ns
    api.add_namespace(audio_ns, path="/api/audio")
    api.add_namespace(respuesta_ns, path="/api/respuestas")

    return app
