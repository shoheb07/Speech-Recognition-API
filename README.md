# Speech-Recognition-API
Below is a simple and complete Speech Recognition API using Python (Flask). It accepts an audio file and returns the transcribed text.

🎤 Speech Recognition API (Python + Flask)

📌 Overview

This project is a simple Speech Recognition API built using Python and Flask. It allows users to upload an audio file and receive the transcribed text using speech-to-text technology.


🚀 Features

- Convert speech (audio) to text
- REST API endpoint for easy integration
- Supports multiple audio formats (WAV, AIFF, FLAC)
- Error handling for invalid inputs
- Lightweight and easy to deploy


🛠️ Tech Stack

- Python
- Flask
- SpeechRecognition Library
- Pydub (for audio conversion)


📦 Installation

1. Clone the repository

git clone https://github.com/your-username/speech-recognition-api.git
cd speech-recognition-api

2. Install dependencies

pip install flask speechrecognition pydub

3. (Optional) Install offline recognition

pip install pocketsphinx


📁 Project Structure

speech_api/
│── app.py
│── uploads/
│── README.md


▶️ Running the Application

python app.py

Server will start at:

http://127.0.0.1:5000/


📡 API Endpoints

🔹 Home

GET /

Response:

Speech Recognition API is running


🔹 Recognize Speech

POST /recognize

Request:

- Form-data
  - key: "file"
  - value: audio file (WAV recommended)

Example using curl:

curl -X POST http://127.0.0.1:5000/recognize \
-F "file=@audio.wav"

Response:

{
  "success": true,
  "transcript": "Hello world"
}


🎧 Supported Audio Formats

- WAV (Recommended)
- AIFF
- FLAC

🔄 Audio Conversion (MP3 → WAV)

from pydub import AudioSegment

audio = AudioSegment.from_mp3("input.mp3")
audio.export("output.wav", format="wav")


⚠️ Error Handling

- No file uploaded → "400 Bad Request"
- Unrecognized speech → "Could not understand audio"
- API request failure → "500 Internal Server Error"

🧠 Future Improvements

- Real-time speech recognition (WebSockets)
- Language selection support
- Integration with advanced models (Whisper, Vosk)
- Frontend UI for recording audio
- Cloud deployment (AWS / Render / Railway)


📄 License

This project is open-source and available under the MIT License.


👨‍💻 Author
shoheb07
