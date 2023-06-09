import sys
import openai
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit

# Set OpenAI API key
openai.api_key = "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"

class GPT3Tester(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create widgets
        self.message_label = QLabel("Message:")
        self.message_edit = QTextEdit()
        self.submit_button = QPushButton("Submit")
        self.response_label = QLabel("Response:")
        self.response_text = QTextEdit()

        # Create layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.message_label)
        vbox.addWidget(self.message_edit)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.response_label)
        vbox.addWidget(self.response_text)

        # Set layout
        self.setLayout(vbox)

        # Connect signal to slot
        self.submit_button.clicked.connect(self.submit)

        # Set window properties
        self.setWindowTitle("GPT-3 Tester")
        self.setGeometry(100, 100, 500, 500)

    def submit(self):
        # Get input values
        message = self.message_edit.toPlainText()

        # Send request to OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )

        print(completion)
        # Get generated text from response
        generated_text = completion["choices"][0]["message"]["content"]
        # Print response
        self.response_text.setText(generated_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GPT3Tester()
    ex.show()
    sys.exit(app.exec_())
