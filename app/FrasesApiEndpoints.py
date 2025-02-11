from flask import Blueprint, jsonify

frases_bp = Blueprint('frases', __name__)


@frases_bp.route("/", methods=["GET"])
def list_frases():
    frases = [
        {"id": 1, "texto": "Esta es una frase de ejemplo", "audio": "/static/audios/audio1.mp3"},
        {"id": 2, "texto": "Otra frase para practicar", "audio": "/static/audios/audio2.mp3"}
    ]
    return jsonify(frases)