from flask import Flask, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

recognizer = sr.Recognizer()

@app.route('/')
def home():
    return "Speech Recognition API is running"

@app.route('/recognize', methods=['POST'])
def recognize_speech():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return jsonify({
            "success": True,
            "transcript": text
        })

    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400

    except sr.RequestError as e:
        return jsonify({"error": str(e)}), 500

    finally:
        os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)
