# #-*coding:utf-8-*-
# from flask import Flask
# from flask import render_template
#
# app = Flask(__name__)
# @app.route("/")
# def index():
#     return "index"
# @app.route("/demo1")
# def demo1():
#     my_int=10
#     my_str ="abc"
#     my_list =[1,6,5,4,8]
#     my_dict= {
#         "name":"laowang" ,
#         "age": 18
#     }
#
#
#
#
#     return render_template("html01.html",my_list=my_list,my_dict=my_dict,my_int=my_int,my_str=my_str)
#  #自定义翻转过滤器
# @app.template_filter("lireserve")
# def do_lireverse(value):
#     temp_li=list(value)
#     temp_li.reverse()
#     return temp_li
# #方式二
# app.add_template_filter(do_lireverse,"lireverse")
#
# if __name__=="__main__":
#      app.run(debug=True,port=5001)
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def index():
    return "index"
@app.route("/demo1")
def demo1():
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
         "id": 5,
          "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template("kkk.html",my_list=my_list)
if __name__ == '__main__':
    app.run(debug=True,port=5666)