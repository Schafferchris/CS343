from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import re
import spacy

app = Flask(__name__)

class SimpleBot:
    def __init__(self):
        # Load SpaCy for text processing
        self.nlp = spacy.load("en_core_web_sm")
        
        # Predefined patterns and responses
        self.pattern_responses = [
            ("greet", "Hello! How can I assist you today?"),
            ("farewell", "Goodbye! Feel free to reach out if you need anything!"),
            ("ask_how_bot_is", "I'm just a bot, but thanks for asking! How about you?"),
            ("ask_bot_name", "I’m SimpleBot, your virtual assistant. What can I help with?"),
            ("ask_help_with", "I'd be happy to help with {0}! Tell me more."),
            ("ask_services", "I can assist with general questions, information lookup, and basic tasks. What do you need help with?"),
            ("ask_joke", "Why don’t robots get mad? Because they have too many bytes to process!"),
            ("ask_bot_origin", "I live in the digital world, always here when you need me!"),
        ]
        
        
        self.known_questions = [
            "What is your name?",
            "Can you help me?",
            "What services do you provide?",
            "How are you?",
            "Tell me a joke."
        ]
        self.responses = {
            "What is your name?": "I am SimpleBot, your assistant!",
            "Can you help me?": "Of course! What do you need help with?",
            "What services do you provide?": "I can answer questions, give information, and help with tasks.",
            "How are you?": "I'm just a bot, but I'm doing great! How about you?",
            "Tell me a joke.": "Why don’t robots get tired? They’re powered by duracells!",
        }
        
        self.fallback_responses = [
            "I'm not sure I understand. Can you clarify?",
            "Could you rephrase that?",
            "Sorry, I didn't catch that. Try asking in a different way.",
            "Hmm, I'm not sure how to respond to that.",
            "That's an interesting question! I'm not sure how to answer.",
        ]
        
        # Patterns for detecting user intent
        self.intents = {
            "greeting": r"hi|hello|hey",
            "goodbye": r"bye|goodbye|see you",
            "question": r"(what|how|can you|tell me).*",
        }
        self.intent_responses = {
            "greeting": "Hello! How can I assist you?",
            "goodbye": "Goodbye! Have a great day!",
        }
        
        # Train TF-IDF on known patterns and questions
        self.vectorizer = TfidfVectorizer().fit([pattern for pattern, _ in self.pattern_responses] + self.known_questions)

    def preprocess(self, text):
        """Clean and process text."""
        doc = self.nlp(text)
        return " ".join([token.lemma_.lower() for token in doc if not token.is_stop])

    def calculate_similarity(self, user_input):
        """Find the most similar question or pattern."""
        tfidf_matrix = self.vectorizer.transform(self.known_questions + [user_input])
        cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        max_sim_index = cosine_sim.argmax()
        return max_sim_index, cosine_sim.max()

    def identify_intent(self, message):
        """Figure out the user's intent."""
        for intent, pattern in self.intents.items():
            if re.search(pattern, message, re.IGNORECASE):
                return intent
        return "unknown"

    def respond(self, message):
        """Generate a response for the user."""
        # Check if it matches an intent
        intent = self.identify_intent(message)
        if intent in self.intent_responses:
            return self.intent_responses[intent]

        # Try to match patterns directly
        for pattern, response in self.pattern_responses:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                if match.groups():
                    return response.format(*match.groups())
                return response

        # Check for similarity with known questions
        idx, similarity_score = self.calculate_similarity(message)
        if similarity_score > 0.5:  # Similarity threshold
            return self.responses[self.known_questions[idx]]

        # Fallback response
        return random.choice(self.fallback_responses)

# Flask routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    """Get user input and return bot response."""
    user_message = request.json['message']
    bot = SimpleBot()
    bot_response = bot.respond(user_message)
    return jsonify({'response': bot_response})

@app.route('/about', methods = ['GET'])
def about():
    return render_template("about.html")

@app.route('/part2', methods=['GET'])
def part2():
    return render_template("part2.html")
# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
