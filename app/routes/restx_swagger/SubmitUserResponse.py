from flask_restx import Namespace, Resource, fields
from app.services.procesador import ProcesadorFrases

# Crear namespace para las frases
ns = Namespace("frases", description="Endpoints relacionados con la gestión de frases")

procesador = ProcesadorFrases()

# Modelo de una frase para Swagger
frase_model = ns.model('Frase', {
    'id': fields.Integer(required=True, description='ID de la frase'),
    'texto': fields.String(required=True, description='Texto de la frase'),
    'audio': fields.String(required=True, description='Ruta del archivo de audio'),
    'nivel': fields.String(required=False, default="básico", description='Nivel de dificultad'),
    'tags': fields.List(fields.String, description='Listado de etiquetas asociadas')
})


@ns.route("/random")
class RandomFrase(Resource):
    @ns.doc("get_random_frase")
    @ns.response(200, "Success", frase_model)
    @ns.response(404, "No hay frases disponibles")
    def get(self):
        """Obtener una frase aleatoria"""
        frase = procesador.obtener_frase_aleatoria()
        if "error" in frase:
            ns.abort(404, frase["error"])
        return frase


@ns.route("/recargar")
class RecargarFrases(Resource):
    def get(self):
        """Recargar frases desde JSON"""
        procesador.cargar_frases_desde_json()
        return {"mensaje": "Frases recargadas desde JSON."}, 200


@ns.route("/")
class ListarFrases(Resource):
    @ns.marshal_with(frase_model, as_list=True)
    def get(self):
        """Listar todas las frases cargadas"""
        return [frase.to_dict() for frase in procesador.frases]
