class Chatbot:
    def __init__(self):
        self.responses = {
            'hello': 'Hello! How can I assist you?',
            'how are you?': 'I am doing well, thank you!',
            'goodbye': 'Goodbye! Have a nice day!',
        }

    def get_response(self, user_message):
        user_message = user_message.lower()

        if user_message in self.responses:
            return self.responses[user_message]
        else:
            return 'Sorry, I cannot understand your message. Please try again.'
