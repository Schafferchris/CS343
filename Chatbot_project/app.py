from flask import Flask, render_template, request, jsonify
import re
import random

app = Flask(__name__)

class SimpleBot:
    def __init__(self):
        self.pattern_responses = [
            (r"hi|hello|hey there|good (morning|afternoon|evening)", "Hello! How can I assist you today?"),
            (r"bye|goodbye|see you|catch you later", "Goodbye! Feel free to reach out if you need anything!"),
            (r"how are you|how have you been|what's up", "I'm just a bot, but thanks for asking! How about you?"),
            (r"(what is|what's) your name|who are you", "I’m SimpleBot, your virtual assistant. What can I help with?"),
            (r"can you help me with (.*)", "I'd be happy to help with {0}! Tell me more."),
            (r"what can you do|what services do you provide", "I can assist with general questions, information lookup, and basic tasks. What do you need help with?"),
            (r"what is the time|current time|do you know the time", "I don't have access to a clock, but your device should have the current time."),
            (r"(what is|what's) today('s)? date", "I'm not equipped to check the date, but your calendar can tell you."),
            (r"(what is|what's) the weather|is it (raining|sunny|cold)", "I can’t check the weather, but a weather app should have the latest info."),
            (r"tell me (a|another) joke", "Why don’t robots get mad? Because they have too many bytes to process!"),
            (r"where are you from|where do you live", "I live in the digital world, always here when you need me!"),
            (r"do you (like|love) (.*)", "I don’t have feelings, but I imagine {1} is pretty interesting! Do you like {1}?"),
            (r"how does (.*) work", "{0} works by following specific rules or principles. I can help explain more if you want!"),
            (r"who (created|made) you", "I was created by a talented developer to assist you!"),
            (r"thank you|thanks a lot|appreciate it", "You're welcome! Happy to help anytime."),
            (r"exit|see you later|goodbye", "Goodbye!"),
            (r"I am well|fine|Great", "I am glad to hear that"),
            (r"Can you help me|help|I have a question", "Sure what do you need?"),
        ]
        self.generic_responses = [
            "I'm not sure I understand. Can you clarify?",
            "Could you rephrase that?",
            "Sorry, I didn't catch that. Try asking in a different way.",
            "Hmm, I'm not sure how to respond to that.",
            "That's an interesting question! I'm not sure how to answer."
            "Please ask again, I do not understand."
        ]

        self.value_error = [
            "Please enter in words not random numbers..."
        ]

    def respond(self, message):
        if any(char.isdigit() for char in message):
            return self.value_error
    
        for pattern, response in self.pattern_responses:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                if match.groups():
                    return response.format(*match.groups())
                else:
                    return response
        return random.choice(self.generic_responses)
   
start_bot = SimpleBot()

@app.route('/')
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    render_template('404.html'), 404

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    bot_response = start_bot.respond(user_message)
    
    return jsonify({'response': bot_response})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False)
