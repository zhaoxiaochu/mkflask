#-*coding:utf-8-*-
from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)
# class config(object):
#     DEBUG=True
# app.config.from_object(config)
#自定义正则转换器
class RegextConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegextConverter,self).__init__(url_map)
        self.regex=args[1]
app.url_map.converters['re']=RegextConverter
@app.route("/")
def index():
    return "index"
@app.route("/user/<re('[a-zA-Z][0-9]{4}'),:user_id>")
def demo1(user_id):
    return "当前 user_id = %s" %user_id


if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask
# from werkzeug.routing import BaseConverter
# app = Flask(__name__)
# class RegextConverter(BaseConverter):
#     def __init__(self,url_map,*args):
#         super(RegextConverter,self).__init__(url_map)
#         self.regex=args[0]
# app.url_map.converters["re"]=RegextConverter
# @app.route("/")
# def index():
#     return "index"
# @app.route("/user/<re('[a-zA-Z][0-9]{4}'):user_id>")
# def demo2(user_id):
#     return "当钱user_id=%s"%user_id
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask
# from flask import abort
# app = Flask(__name__)
# @app.route("/")
# def index():
#     abort(404)
#     return "index"
#
# @app.errorhandler(404)
# def page_note_found(error):
#     return "当前页面不见了"
# if __name__ == '__main__':
#     app.run(debug=True)