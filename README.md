
# Listening Practice API

This project is an API designed to help users practice **listening skills** in English through phrase dictation. The system allows users to listen to an audio file associated with a sentence and then submit their written response. The API evaluates whether the response is correct or incorrect.

## Features

- **GET /audio**: Retrieve an audio file associated with a sentence.
- **POST /respuesta**: Submit a response for the dictation (written text) and receive feedback indicating if it was correct or not.

### Use Case Example
1. The user performs a **GET** request to retrieve an audio file.
2. Listens to the audio and writes down the associated phrase.
3. Submits the written response via a **POST** request and receives feedback on its correctness.

---

## Project Requirements

Ensure you have the following dependencies installed:

- Python 3.13 or higher
- Flask
- [Any other dependencies listed in `requirements.txt`]

Install the dependencies with:

```shell script
pip install -r requirements.txt
```

---

## Project Structure

```
/mi_proyecto
│
├── app/                    # Main application directory
│   ├── __init__.py         # Initializes the Flask app
│   ├── routes/             # API routes (endpoints)
│   │   ├── __init__.py
│   │   └── frases.py       # Endpoints for handling phrases and audio
│   ├── services/           # Business logic (process texts, comparisons)
│   │   ├── __init__.py
│   │   └── procesador.py   # Methods to evaluate responses to dictation
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   └── frase.py        # Model for handling phrases and their properties
│   ├── static/             # Static files (audio)
│   │   └── audios/         # Audio files used for the exercises
│   └── templates/          # HTML templates (optional, if rendering with Jinja2)
│       └── index.html
│
├── tests/                  # Project tests
│   └── test_frases.py      # Tests for endpoints and logic
│
├── requirements.txt        # Project dependencies
├── config.py               # Configuration (paths, environment variables)
└── run.py                  # Main file to run the app
```

---

## API Endpoints

### **GET /audio**
- **Description**: Returns an audio file associated with a sentence.
- **Response**:
```json
{
      "audio_url": "https://example.com/audio/audio1.mp3",
      "frase_id": 1
  }
```

### **POST /respuesta**
- **Description**: Submits the written response for the dictation and receives an evaluation.
- **Request Body**:
```json
{
      "frase_id": 1,
      "respuesta": "Text submitted by the user"
  }
```
- **Response**:
```json
{
      "correcto": true,
      "mensaje": "Correct answer!"
  }
```

---

## How to Run the Project

1. Make sure to install the dependencies:
```shell script
pip install -r requirements.txt
```

2. Run the application:
```shell script
python run.py
```

3. Access the API at: `http://127.0.0.1:5000`

---

## Tests

To ensure everything works correctly, run the included project tests:

```shell script
python -m unittest discover tests
```

---

## Future Plans

- Integrate AI-based logic to evaluate written responses more flexibly.
- Expand the API with additional endpoints.
- Use a database for managing phrases and users.

---