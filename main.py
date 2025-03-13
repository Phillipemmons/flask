from flask import Flask, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from my new route!"})

@app.route('/gpt')
def call_gpt():
    prompt = "Hello, GPT! How are you today?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    text_output = response.choices[0].text.strip()
    return jsonify({"GPT Response": text_output})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
