from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Valadares Cafe"


@app.route("/about")
def about():
    return "Valadares Cafe is a neighborhood cafe in Miami serving coffee and fresh pastries."
