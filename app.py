
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
