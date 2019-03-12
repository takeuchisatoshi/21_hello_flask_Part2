import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", message="Hi! hachimantai!")


@app.route("/dice", methods=["GET"])
def dice():
    result = random.randint(1, 6)
    return render_template("dice.html", result=result)


@app.route("/greet/<username>", methods=["GET"])
def greet(username):
    return render_template("greet.html", name=username)


if __name__ == '__main__':
    app.run(debug=True)
