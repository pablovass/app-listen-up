
# API de Ejercicios de Listening

Este proyecto es una API para practicar **listening** en inglés mediante el dictado de frases. El sistema permite a los usuarios escuchar un audio asociado con una oración y, posteriormente, enviar su respuesta escrita. La API evalúa si la respuesta es correcta o incorrecta.

## Funcionalidades

- **GET /audio**: Obtiene un audio relacionado con una oración.
- **POST /respuesta**: Envía la respuesta para el dictado (texto escrito) y recibe una evaluación indicando si fue correcta o incorrecta.

### Ejemplo de uso
1. El usuario realiza un **GET** para obtener un audio.
2. Escucha el audio y escribe la frase asociada.
3. Realiza un **POST** para enviar su respuesta y obtiene un resultado sobre si fue correcta o no.

---

## Requisitos del Proyecto

Asegúrate de tener las siguientes dependencias instaladas:

- Python 3.13 o superior
- Flask
- [Cualquier otra dependencia listada en `requirements.txt`]

Instala las dependencias con:

```shell script
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```
/mi_proyecto
│
├── app/                    # Carpeta principal de la aplicación
│   ├── __init__.py         # Inicializa la app Flask
│   ├── routes/             # Rutas (endpoints) de la API
│   │   ├── __init__.py
│   │   └── frases.py       # Endpoints para manejar frases y audios
│   ├── services/           # Lógica de negocio (procesamiento de textos y comparación)
│   │   ├── __init__.py
│   │   └── procesador.py   # Métodos para evaluar respuestas del dictado
│   ├── models/             # Modelos de datos
│   │   ├── __init__.py
│   │   └── frase.py        # Modelo para manejar las "frases" y sus propiedades
│   ├── static/             # Archivos estáticos (audios)
│   │   └── audios/         # Audios utilizados para los ejercicios
│   └── templates/          # HTML templates (opcional, si usas Jinja2 para front-end)
│       └── index.html
│
├── tests/                  # Tests del proyecto
│   └── test_frases.py      # Tests para endpoints y lógica
│
├── requirements.txt        # Dependencias del proyecto
├── config.py               # Configuración (paths, variables de entorno)
└── run.py                  # Archivo principal para ejecutar la app
```

---

## Endpoints de la API

### **GET /audio**
- **Descripción**: Retorna un audio asociado con una oración.
- **Respuesta**:
```json
{
      "audio_url": "https://example.com/audio/audio1.mp3",
      "frase_id": 1
  }
```

### **POST /respuesta**
- **Descripción**: Envía la respuesta escrita para el dictado y recibe una evaluación.
- **Cuerpo del request**:
```json
{
      "frase_id": 1,
      "respuesta": "Texto que el usuario escribió"
  }
```
- **Respuesta**:
```json
{
      "correcto": true,
      "mensaje": "¡Respuesta correcta!"
  }
```

---

## Cómo correr el proyecto

1. Asegúrate de instalar las dependencias:
```shell script
pip install -r requirements.txt
```

2. Ejecuta la aplicación:
```shell script
python run.py
```

3. Accede a la API en: `http://127.0.0.1:5000`

---

## Tests

Para asegurarte de que todo funciona correctamente, puedes ejecutar los tests incluidos en el proyecto:

```shell script
python -m unittest discover tests
```

---

## Plan futuro

- Integrar lógica de IA para evaluar respuestas escritas de forma más flexible.
- Expandir las funcionalidades de la API con nuevos endpoints.
- Usar una base de datos para almacenar frases y usuarios.

