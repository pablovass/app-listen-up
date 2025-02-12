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

    def verificar_frase(self, frase_id, texto_usuario):
        """Verifica si la frase del usuario coincide con la frase del JSON"""
        # Buscar la frase por ID
        frase_obj = next((f for f in self.frases if f.id == frase_id), None)
        if not frase_obj:
            return {"error": True, "mensaje": "ID de frase no encontrado"}

        # Divide ambas frases en listas de palabras
        palabras_originales = frase_obj.texto.lower().split()
        palabras_usuario = texto_usuario.lower().split()

        # Compara palabra por palabra
        resultado = []
        for original, usuario in zip(palabras_originales, palabras_usuario):
            resultado.append({
                "palabra": original,
                "correcta": original == usuario
            })

        # Identificar palabras faltantes o sobrantes
        if len(palabras_usuario) < len(palabras_originales):
            for original in palabras_originales[len(palabras_usuario):]:
                resultado.append({"palabra": original, "correcta": False, "mensaje": "Palabra no mencionada"})
        elif len(palabras_usuario) > len(palabras_originales):
            for usuario in palabras_usuario[len(palabras_originales):]:
                resultado.append({"palabra": usuario, "correcta": False, "mensaje": "Palabra no esperada"})

        # Retornar el resultado detallado
        return {
            "error": False,
            "mensaje": "Verificación completada",
            "detalles": resultado,
            "texto_original": frase_obj.texto,
            "texto_usuario": texto_usuario
        }
