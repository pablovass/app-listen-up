from app.models.frase import Frase
import random
import json
import os


class ProcesadorFrases:
    def __init__(self, json_file=None):
        self.frases = []  # Lista interna que contiene las frases cargadas.
        # Construir ruta dinámica para el archivo JSON
        base_path = os.path.dirname(os.path.abspath(__file__))  # Directorio de este archivo
        self.json_file = json_file or os.path.join(base_path, "..", "static", "frases_json", "frases.json")
        self.cargar_frases_desde_json()  # Cargar frases al iniciar.

    def cargar_frases_desde_json(self):
        """Carga frases desde un archivo JSON y las convierte a instancias de Frase"""
        if os.path.exists(self.json_file):  # Verifica que el archivo existe.
            with open(self.json_file, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for item in datos:
                    # Crear instancia de Frase con los datos del JSON
                    frase = Frase(
                        id=item["id"],
                        texto=item["texto"],
                        audio=item["audio"],
                        nivel=item.get("nivel", "básico"),
                        tags=item.get("tags", [])
                    )
                    self.frases.append(frase)
        else:
            print(f"El archivo {self.json_file} no existe. No se cargaron frases.")

    def agregar_frase(self, id, texto, audio, nivel="básico", tags=[]):
        """Agrega dinámicamente frases al sistema"""
        frase = Frase(id, texto, audio, nivel, tags)
        self.frases.append(frase)

    def obtener_frase_aleatoria(self):
        """Devuelve una frase aleatoria o vacío si no hay frases"""
        if not self.frases:
            return {"error": "No hay frases disponibles"}
        frase = random.choice(self.frases)
        return frase.to_dict()

    def verificar_frase(self, texto_usuario):
        """Verifica si la frase del usuario coincide con alguna de las originales"""
        for frase in self.frases:
            if frase.texto.lower() == texto_usuario.lower():
                return {"correcto": True, "mensaje": "¡Correcto!"}
        return {"correcto": False, "mensaje": "Respuesta incorrecta"}
