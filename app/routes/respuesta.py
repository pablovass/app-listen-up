from flask_restx import Namespace, Resource, fields
from flask import request

# Crea un namespace para "respuesta"
ns = Namespace('respuesta', description='Operations related to user responses')

# Modelo para documentar y validar entradas en Swagger
respuesta_model = ns.model('Respuesta', {
    'frase_id': fields.Integer(required=True, description='ID of the phrase'),
    'respuesta': fields.String(required=True, description='User\'s response')
})


@ns.route('/')
class SubmitRespuesta(Resource):
    @ns.expect(respuesta_model)
    def post(self):
        """Submit a response and get feedback"""
        data = request.json
        if data['respuesta'].lower() == "this is a test":
            return {"correcto": True, "mensaje": "¡Respuesta correcta!"}
        return {"correcto": False, "mensaje": "Respuesta incorrecta."}
