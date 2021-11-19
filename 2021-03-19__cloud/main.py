from flask import Flask, request
from transformers import pipeline

# set up flask app and model
app = Flask(__name__)
model = pipeline("sentiment-analysis")


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/sentiment")
def sentiment():
    phrase = request.args.get("phrase")
    print("Here is a phrase!", phrase)
    return model(phrase)[0]
