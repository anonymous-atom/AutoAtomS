import requests
from flask import Flask, render_template, request
import openai
import os


openai.api_key = "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"
app = Flask(__name__, template_folder='/home/karun/PycharmProjects/AutoAtomS/templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = os.path.abspath('templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        # Get the user's input from the form
        user_input = request.form['user_input']

        # Make the API call
        prompt = f'User input: {user_input}\nAI response:'

        completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ],
        )

        # Extract the response text from the API response
        result = completion["choices"][0]["message"]["content"]

        # Render the result to the user
        return render_template('index.html', result=result)

    # If the request method is GET, display the input form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
