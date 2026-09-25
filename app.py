
import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are Pio, a helpful personal AI chatbot.
Be clear, thoughtful, curious, and honest. Explain difficult ideas step by step.
Do not pretend to know things you do not know."""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    response = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-5.6"),
        instructions=SYSTEM_PROMPT,
        input=messages,
    )
    return jsonify({"reply": response.output_text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
