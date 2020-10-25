from flask import Flask, render_template
import random

app = Flask(__name__)

messages = [
    "Hello!",
    "Welcome to my test site",
    "What's up!?",
    "Playing with Flask, Docker and Nginx",
    "Thanks for taking a look~"]


@app.route('/')
def index():
    message = random.choice(messages)
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
