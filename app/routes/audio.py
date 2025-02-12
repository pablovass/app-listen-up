from flask import url_for
from flask_restx import Namespace, Resource

# Definir Namespace
ns = Namespace("audio", description="Operations related to audio files")


@ns.route("/<string:filename>")
class GetAudio(Resource):
    def get(self, filename):
        """Return the URL of the audio file"""
        audio_url = url_for("static", filename=f"audios/{filename}", _external=True)
        return {"audio_url": audio_url}
