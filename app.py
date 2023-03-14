from flask import Flask, render_template, request
import openai
import os

openai.api_key = "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"
app = Flask(__name__, template_folder='/home/karun/PycharmProjects/AutoAtomS/templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = os.path.abspath('templates')

def generate_response(prompt):
    completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
    )
    return completion["choices"][0]["message"]["content"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)
        return render_template('output.html', prompt=prompt, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
