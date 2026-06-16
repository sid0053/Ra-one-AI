from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data['messages']
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000)