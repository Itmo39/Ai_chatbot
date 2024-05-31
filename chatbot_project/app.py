from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Initialize the conversational pipeline with the DialoGPT model
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

# Predefined responses
predefined_responses = {
    "what's your name": "My name is MO AI.",
    "hello": "Hello! Welcome to MO AI. What can I help you with today?",
    "hi": "Hi there! Welcome to MO AI. How can I assist you?",
    "how are you": "I'm just a bunch of code, but I'm here to help you!"
}

# Function to get a response from the bot
def get_response(user_input):
    user_input_lower = user_input.lower()
    for question, answer in predefined_responses.items():
        if question in user_input_lower:
            return answer
    # If no predefined response, use the model
    response = chatbot(user_input)[0]["generated_text"]
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
