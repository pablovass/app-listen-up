# routes/frases.py
from flask import Blueprint, request, jsonify
from app.services.procesador import ProcesadorFrases

frases_bp = Blueprint('frases', __name__)
procesador = ProcesadorFrases()


# Endpoint: Recargar frases desde JSON
@frases_bp.route('/recargar', methods=['GET'])
def recargar_frases():
    procesador.cargar_frases_desde_json()
    return jsonify({"mensaje": "Frases recargadas desde JSON."})


# Endpoint: Obtener frase aleatoria
@frases_bp.route('/random', methods=['GET'])
def get_random_frase():
    frase = procesador.obtener_frase_aleatoria()
    return jsonify(frase)


# Endpoint: Verificar frase
@frases_bp.route('/verificar', methods=['POST'])
def verificar_frase():
    data = request.get_json()
    texto_usuario = data.get('texto_usuario')
    resultado = procesador.verificar_frase(texto_usuario)
    return jsonify(resultado)
