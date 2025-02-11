from flask_restx import Namespace, Resource

# Crea un namespace para los endpoints relacionados con audio:
ns = Namespace("audio", description="Operations related to audio files")


@ns.route("/")
class GetAudio(Resource):
    def get(self):
        """Get an audio file and associated phrase"""
        return {"audio_url": "/static/audios/audio1.mp3", "frase_id": 1}
