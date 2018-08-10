# -*coding:utf-8-*-
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/demo1")
def demo1():
    return render_template("03.hong.html")


if __name__ == "__main__":
    app.run(debug=True, port=5667)
