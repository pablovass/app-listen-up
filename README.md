/mi_proyecto
│
├── app/                    # Carpeta principal de la app
│   ├── __init__.py         # Inicializa la app Flask
│   ├── routes/             # Rutas (endpoints) de la API
│   │   ├── __init__.py
│   │   └── frases.py       # Endpoints para manejar frases y audios
│   ├── services/           # Lógica de negocio (procesar textos, IA en el futuro)
│   │   ├── __init__.py
│   │   └── procesador.py   # Lógica para comparar textos y más adelante integrar Llama
│   ├── models/             # Modelos de datos (si necesitás trabajar con DB más adelante)
│   │   ├── __init__.py
│   │   └── frase.py
│   ├── static/             # Archivos estáticos (audios, imágenes si necesitás)
│   │   └── audios/
│   └── templates/          # HTML templates (si usás Jinja2 o querés renderizar desde Flask)
│       └── index.html
│
├── tests/                  # Tests del proyecto
│   └── test_frases.py
│
├── requirements.txt        # Dependencias del proyecto
├── config.py               # Configuración de la app (paths, settings)
└── run.py                  # Archivo principal para correr la app
