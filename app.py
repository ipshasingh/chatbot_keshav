
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("gita_data.json", "r", encoding="utf-8") as file:
    gita_data = json.load(file)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").lower()

    response = "I am still learning. Please ask a question related to the Gita."

    if "who are you" in question:
        response = "I am Keshav, your spiritual guide based on the Shrimad Bhagavad Gita."

    return jsonify({"response": response})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request"}), 400

    question = data["question"]
    chat = model.start_chat(history=[])
    response = chat.send_message(f"{SYSTEM_PROMPT}\n\nUser Question: {question}")

    reply = response.text
    return jsonify({"response": reply})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Default 10000 if not set
    app.run(host='0.0.0.0', port=port)


@app.route('/')
def home():
    return "KeshavAI backend is running!"
