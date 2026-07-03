# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="your-api-key-here"

conversation_history = [
    {
        "role": "system",
        "content": "You are Maya, a friendly AI assistant. Be helpful and kind. Keep responses short and natural. Never repeat previous conversation. Just answer the current question directly."
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    
    try:
        user_message = request.json["message"]
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=1000,
            messages=conversation_history
        )
        maya_response = response.choices[0].message.content
        conversation_history.append({
            "role": "assistant",
            "content": maya_response
        })
        return jsonify({"response": maya_response})
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"response": "Error: " + str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)