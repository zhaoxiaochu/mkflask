from flask import Flask
from flask import g
from flask import render_template
from flask import session
from flask import flash

app = Flask(__name__)
app.secret_key = "asdf"


@app.route('/')
def index():
    flash("我是一条闪现的消息")
    return 'index'


@app.route('/demo1')
def demo1():
    session["name"] = "xiaohua"
    g.user_name = "laowang"
    # 闪现一条消息
    return render_template("temp1.html")


if __name__ == '__main__':
    app.run(debug=True)
