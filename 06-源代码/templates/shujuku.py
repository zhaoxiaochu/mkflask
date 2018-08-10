#-*coding:utf-8-*-
from flask import Flask
import flask_sqlalchemy import SQLAl
app = Flask(__name__)
@app.route("/")
def index():
    return "index"
if __name__=="__main__":
     app.run(debug=True)
