import os
from flask import send_from_directory, abort
from flask_restx import Namespace, Resource

# Namespace
ns = Namespace("audio", description="Operations related to audio files")

# Directorio de archivos de audio
AUDIO_FOLDER = os.path.join(os.getcwd(), "app/static/audios")


@ns.route("/<string:filename>")
class GetAudio(Resource):
    def get(self, filename):
        """Serve an audio file from the static directory."""
        file_path = os.path.join(AUDIO_FOLDER, filename)
        print(f"Intentando servir archivo: {file_path}")  # Log para debug

        # Verifica si el archivo existe
        if not os.path.exists(file_path):
            print(f"Archivo no encontrado: {file_path}")  # Mostrar si el archivo no está
            abort(404, description=f"Archivo no encontrado: {filename}")

        # Si existe, sirve el archivo usando send_from_directory
        return send_from_directory(AUDIO_FOLDER, filename)
