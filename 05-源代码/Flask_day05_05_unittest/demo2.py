from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# 一个登录的接口，分为以下几种情况
# 1. 如果登录的时候，用户名和密码其中某一个没有传的话，就返回 errcode -2
# 2. 如果登录的时候，用户名和密码传错的话，就返回 errcode -1
# 3. 如果正确的话，就返回 errcode  0
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    a = 1 / 0
    # 判断参数是否为空
    if not all([username, password]):
        result = {
            "errcode": -2,
            "errmsg": "params error"
        }
        return jsonify(result)


    # 如果账号密码正确
    # 判断账号密码是否正确
    if username == 'itheima' and password == 'python':
        result = {
            "errcode": 0,
            "errmsg": "success"
        }
        return jsonify(result)
    else:
        result = {
            "errcode": -1,
            "errmsg": "wrong username or password"
        }
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
