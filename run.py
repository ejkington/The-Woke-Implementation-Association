import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/confirmation")
def confirmation():
    return render_template("donate-confirmation.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
