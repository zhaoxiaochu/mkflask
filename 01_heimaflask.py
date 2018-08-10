#-*coding:utf-8-*-
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def index():
#     return "index"
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/")
def index():
    return "index"
# #指定路由地址
# @app.route("/demo1")
# def demo1():
#     return "demo1"
# #指定路由参数类型
# @app.route("/demo2/<int:user_id>")
# def demo2(user_id):
#     return "demo2 user_id=%s" %user_id
# #指定路由请求方式
@app.route("/demo3", methods=["get","post"])
def demo3():
    return "demo3 当前请求方式是%s" %request.method
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True,port=5001,)