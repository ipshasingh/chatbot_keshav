from flask import Flask, request, jsonify, send_file
import google.generativeai as genai
import os
from gtts import gTTS

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

with open("prompt.txt", "r", encoding="utf-8") as file:
    SYSTEM_PROMPT = file.read()

model = genai.GenerativeModel("gemini-pro")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question")

    chat = model.start_chat(history=[])
    response = chat.send_message(f"{SYSTEM_PROMPT}\n\nUser Question: {question}")

    reply = response.text

    return jsonify({"response": reply})

@app.route('/recite', methods=['POST'])
def recite():
    data = request.json
    verse = data.get("verse")

    tts = gTTS(verse, lang="hi")
    tts.save("verse.mp3")

    return send_file("verse.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)