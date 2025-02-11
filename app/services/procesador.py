import random
from app.models.frase import FRASES

class ProcesadorFrases:
    def obtener_frase_aleatoria(self):
        return random.choice(FRASES)
    
    def verificar_frase(self, texto_usuario):
        frase_correcta = self.obtener_frase_aleatoria()['texto']
        errores = self._comparar_texto(frase_correcta, texto_usuario)
        return {
            "correcta": len(errores) == 0,
            "errores": errores
        }
    
    def _comparar_texto(self, correcta, usuario):
        correcta_palabras = correcta.lower().split()
        usuario_palabras = usuario.lower().split()
        errores = []
        
        for idx, palabra in enumerate(correcta_palabras):
            if idx >= len(usuario_palabras) or palabra != usuario_palabras[idx]:
                errores.append(palabra)
        
        return errores
