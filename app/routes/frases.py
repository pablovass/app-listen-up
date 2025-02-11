from flask import Blueprint, request, jsonify
from app.services.procesador import ProcesadorFrases

frases_bp = Blueprint('frases', __name__)
procesador = ProcesadorFrases()

@frases_bp.route('/random', methods=['GET'])
def get_random_frase():
    frase = procesador.obtener_frase_aleatoria()
    return jsonify(frase)

@frases_bp.route('/verificar', methods=['POST'])
def verificar_frase():
    data = request.get_json()
    texto_usuario = data.get('texto_usuario')
    resultado = procesador.verificar_frase(texto_usuario)
    return jsonify(resultado)
