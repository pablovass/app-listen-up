from flask_restx import Namespace, Resource
from app.services.procesador import ProcesadorFrases

# Namespace para los endpoints de frases relacionadas con audios
ns = Namespace("audio", description="Endpoints relacionados con los audios de frases")

procesador = ProcesadorFrases()


@ns.route("/random")
class RandomAudioFrase(Resource):
    def get(self):
        """Devuelve un audio de frase aleatoria"""
        frase = procesador.obtener_frase_aleatoria()
        if "error" in frase:
            ns.abort(404, frase["error"])
        # Solo devolvemos el audio
        return {"audio": frase["audio"]}, 200
