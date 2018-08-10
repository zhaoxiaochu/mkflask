from flaskone import Flask
from flaskone import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("temp1.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
