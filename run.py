from flask import Flask
from flask_restx import Api
from flask_cors import CORS  # Ensure you have the flask-cors package installed



from app.routes.restx_swagger.AudioEndpointsNamespace import ns as audio_namespace
from app.routes.restx_swagger.SubmitUserResponse import ns as respuesta_namespace
from app.routes.restx_swagger.FrasesEndpointsNamespace import ns as frases_namespace


def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para todas las rutas. Ensure flask-cors is installed.
    api = Api(
        app,
        version="1.0",
        title="Frases API",
        description="Documentación Swagger de la API de Frases",
    )

    # Registrar namespaces
    api.add_namespace(audio_namespace, path="/audio")
    api.add_namespace(respuesta_namespace, path="/respuesta")
    api.add_namespace(frases_namespace, path="/frases")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
