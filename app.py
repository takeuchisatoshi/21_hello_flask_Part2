from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", message="Hi! hachimantai!")


if __name__ == '__main__':
    app.run(debug=True)
