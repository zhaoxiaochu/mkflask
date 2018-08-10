#-*coding:utf-8-*-
from flaskone import Flask,json,jsonify
from flaskone import redirect
from flaskone import url_for
app = Flask(__name__)
@app.route("/")
def index():
    return "index"
# @app.route("/json")
# def demo4():
#     temp_dict={
#         "name":"laowang",
#         "age":18
#     }
#     return jsonify(temp_dict)
#重定向
@app.route("/redirect")
def demo5():
    return redirect("http://ntlias-stu.boxuegu.com")
@app.route("/demo6")
def demo6():
    return redirect(url_for("index"))
@app.route("/code")
def demo7():
    return "自定义状态码666"


if __name__ == '__main__':
    app.run(debug=True)
