
# Listening Practice API

This project offers an API to help users improve their **listening comprehension skills** in English. Users listen to audio files linked with specific sentences and submit text responses that are verified for accuracy.

---

## Features

- **Retrieve Sentences with Audio**: Access phrases along with their corresponding audio files for dictation exercises.
- **Automated Feedback**: Submit text responses to the API and receive feedback on whether the input matches the original phrase.
- **Difficulty Levels & Tags**: Phrases are categorized into difficulty levels (`básico`, `intermedio`, `avanzado`) and associated with specific tags for filtering or other contextual uses.

---

## Endpoints Overview

### **Phrase Management** (`/frases`)
1. `GET /frases/`: Retrieve a list of all available phrases from the system.
2. `GET /frases/random`: Get a random phrase, including its text, audio, and details.
3. `GET /frases/recargar`: Reload phrases from the JSON file located in the project.
4. `POST /frases/verificar`: Submit a text to verify against the original phrase.

### **Audio Retrieval** (`/audio`)
- `GET /audio/<filename>`: Retrieves the specified audio file from the static directory.

### **Response Validation** (`/respuesta`)
- `POST /respuesta`: Submit a user's response to a dictated sentence and receive validation feedback.

---

## Example Workflow
1. The user queries `/frases/random` to get a random phrase and its audio file.
2. After listening to the file, the user transcribes the sentence.
3. The text is submitted to `/frases/verificar` for evaluation or to `/respuesta` to evaluate whether it matches.

---

## Project Structure

```plaintext
project/
├── app/                     # Main application code
│   ├── __init__.py          # App initialization
│   ├── routes/              # Routes namespace
│   │   ├── AudioEndpointsNamespace.py
│   │   ├── FrasesEndpointsNamespace.py
│   │   └── SubmitUserResponse.py
│   ├── services/            # Business logic layer
│   │   └── procesador.py    # Sentence processor for evaluation and JSON handling
│   ├── models/              # Data models
│   │   ├── __init__.py
│   │   └── frase.py         # Frase class model
│   └── static/              # Static resources (e.g., audio files)
│       ├── audios/          # Directory containing audio files
│       └── frases_json/     # JSON file with phrase details
├── tests/                   # Unit tests
│   └── test_frases.py
├── config.py                # Project configurations (paths, environment variables)
├── requirements.txt         # Python dependencies
├── README.md                # Documentation (this file)
├── run.py                   # Entry point to run the application
└── AppLauncher.py           # Alternate app launcher
```

---

## Local Setup

### Prerequisites
Make sure your environment has the following:
- **Python** 3.13+
- **Flask** and additional required dependencies.

Install dependencies with:
```bash
pip install -r requirements.txt
```

### Running the App
Start the application locally:
```bash
python run.py
```

Access the API at: [http://127.0.0.1:5000](http://127.0.0.1:5000/)

---

## Example Requests

### **Retrieve Random Phrase**
- **Request**:
  ```bash
  GET /frases/random
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "texto": "What would you say is your greatest strength?",
    "audio": "03.mp3",
    "nivel": "intermedio",
    "tags": ["strength", "habilidades"]
  }
  ```

### **Verify User's Transcription**
- **Request**:
  ```bash
  POST /frases/verificar
  Content-Type: application/json

  {
      "id": 3,
      "texto": "What would you say is your greatest strength?"
  }
  ```
- **Response**:
  ```json
  {
      "error": false,
      "mensaje": "Verificación completada",
      "detalles": [
          {"palabra": "What", "correcta": true},
          {"palabra": "would", "correcta": true},
          {"palabra": "you", "correcta": true},
          {"palabra": "say", "correcta": true},
          {"palabra": "is", "correcta": true},
          {"palabra": "your", "correcta": true},
          {"palabra": "greatest", "correcta": true},
          {"palabra": "strength?", "correcta": true}
      ],
      "texto_original": "What would you say is your greatest strength?",
      "texto_usuario": "What would you say is your greatest strength?"
  }
  ```

---

## Testing
Run tests to verify functionality:
```bash
python -m unittest discover tests
```

---

## JSON Loading
The application uses a local JSON file (`frases.json`) to load the phrases and their associated metadata. Make sure to update the JSON file if new phrases or corrections are needed.

### Sample JSON Structure
```json
[
  {
    "id": 1,
    "texto": "Can you tell me about yourself and your professional background?",
    "audio": "01.mp3",
    "nivel": "intermedio",
    "tags": ["My speech", "introducción"]
  },
  {
    "id": 2,
    "texto": "What were your responsibilities?",
    "audio": "02.mp3",
    "nivel": "intermedio",
    "tags": ["Responsibilities", "experiencia"]
  }
]
```

---

## Future Improvements

- Enhance text verification to be more context-aware using NLP techniques.
- Add user tracking and profiles to save progress during the exercises.
- Implement advanced logging for better debugging in production environments.
- Migrate to a database for dynamic management of phrases and metadata.

---

## Authors
This project was designed to support English learners through improved listening practice and interactive feedback.

