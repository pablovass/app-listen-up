from flask_restx import Namespace, Resource, fields
from flask import request

# Crea un namespace para manejar las respuestas del usuario
ns = Namespace("respuesta", description="Operations related to user responses")

# Modelo para la documentación y validación Swagger
respuesta_model = ns.model('Respuesta', {
    'frase_id': fields.Integer(required=True, description='ID of the phrase'),
    'respuesta': fields.String(required=True, description='User\'s response text')
})


@ns.route("/")
class SubmitRespuesta(Resource):
    @ns.expect(respuesta_model)
    def post(self):
        """Submit a user response"""
        data = request.json
        if data['respuesta'].lower() == "this is a test":
            return {"correcto": True, "mensaje": "¡Respuesta correcta!"}
        return {"correcto": False, "mensaje": "Respuesta incorrecta."}