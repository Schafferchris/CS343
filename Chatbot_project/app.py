from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    
    #TODO: Implement response logic below
    # Placeholder for chatbot response logic, you can replace this with actual logic
    bot_response = generate_bot_response(user_message)
    
    return jsonify({'response': bot_response})

def generate_bot_response(message):
    #TODO: implement chatbot logic here
    # Placeholder for chatbot logic (e.g., calling an AI model, a rule-based system, etc.)
    return f"Bot: I received your message: {message}"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
