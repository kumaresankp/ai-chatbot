from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'  # Replace with your actual OpenAI API key

def generate_chatbot_response(user_message):
    prompt = f'User: {user_message}\nChatbot:'

    response = openai.Completion.create(
        engine='text-davinci-003',  # Use the appropriate OpenAI model
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )

    bot_response = response.choices[0].text.strip().split('\n')[0].replace('Chatbot:', '')
    return bot_response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.form['msg']
    bot_response = generate_chatbot_response(user_message)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
