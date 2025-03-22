from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200577097"})

@app.route('/webhook', methods=['POST'])
def webhook():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why don’t scientists trust atoms? Because they make up everything!"
    ]
    response = {
        "fulfillmentText": random.choice(jokes)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
