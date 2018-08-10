# #-*coding:utf-8-*-
# from flask import Flask
# from flask import make_response
# from flask import request
#
# app = Flask(__name__)
# @app.route("/")
# def index():
#     name=request.cookies.get("name")
#     print("name=%s" % name)
#     return "index"
# @app.route("/setcookie")
# def set_cookie():
#     resp= make_response("hahah")
#     resp.set_cookie("name","laowang")
#     return resp

# if __name__=="__main__":
#      app.run(debug=True,port=5001)

# from flask import Flask
# from flask import make_response
# from flask import request
#
# app = Flask(__name__)
# @app.route("/")
# def index():
#     name=request.cookies.get("name")
#     print("name=%s" % name)
#     return "index"
# @app.route("/setcookie")
# def set_cookie():
#     resp=make_response("haha")
#     resp.set_cookie("name", "laowang")
#     resp.set_cookie('class', "python9", max_age=3600)
#     return resp
# if __name__=="__main__":
#      app.run(debug=True,port=5001)
#session
# from flask import Flask
# from flask import request
# from flask import session
#
# app = Flask(__name__)
# app.config["SECRET_KEY"]="jdnfjsdjsdjkf"
# @app.route("/")
# def index():
#     return "index"
# @app.route("/login")
# def login():
#     session["username"] = "laowang"
#     session["userid"]= 18
#     return "登陆成功"
# @app.route("/userinfo")
# def user_info():
#     username=session.get("username")
#     userid=session.get("userid")
#     print("username=%s" % username)
#     print("userid=%s" % userid)
#     return "用户信息"
#
#
# if __name__=="__main__":
#      app.run(debug=True)
# from flask import Flask
# from flask import session
#
# app = Flask(__name__)
# app.config["SECRET_KEY"]="jdnfjsdjsdjkf"
#
# @app.route("/")
# def index():
#     return "index"
# @app.route("/login")
# def login():
#     session["username"]="laowang"
#     session["userid"]= "18"
#     return "登陆成功"
# @app.route("/userinfo")
# def user_info():
#     username=session.get("username")
#     userid=session.get("userid")
#     print("username=%s"%username)
#     print("userid=%s"%userid)
#     return "客户信息"
# if __name__=="__main__":
#      app.run(debug=True)
# from flask import Flask
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route("/")
# def index():
#     return "index"
# if __name__=="__main__":
#      app.run()

#模版



