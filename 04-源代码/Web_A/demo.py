import base64
import os

from flaskone import Flask
from flaskone import flash
from flaskone import make_response
from flaskone import redirect
from flaskone import render_template
from flaskone import request
from flaskone import url_for

app = Flask(__name__)
app.secret_key = "aaaaa"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 发起登录请求
        # 获取表单提交的参数
        username = request.form.get("username")
        password = request.form.get("password")

        if not all([username, password]):
            flash("请输入用户名和密码")
            return render_template("login.html")

        # 判断用户名和密码是否正确
        if username != "laowang" or password != "123456":
            flash("用户名和密码错误")
            return render_template("login.html")

        # 生成一个响应
        resp = make_response(redirect(url_for('transfer')))
        # 因为要保持登录状态，所以需要向 cookie 写入数据
        resp.set_cookie("username", username)

        return resp

    return render_template("login.html")


@app.route('/transfer', methods=["get", "post"])
def transfer():
    # if 没有登录：
    #     重定向到登录页
    # 先去 cookie 中去取，如果没有登录，取不到
    username = request.cookies.get("username", None)
    if not username:
        return redirect(url_for('index'))

    if request.method == "POST":
        # 去做转账的逻辑
        # 取出参数
        to_account = request.form.get("to_account")
        money = request.form.get("money")
        # 从表单中取出来隐藏随机值
        form_token = request.form.get("token")
        # 再从 cookie 中取出随机值
        cookie_token = request.cookies.get("cookie_token")

        if form_token != cookie_token:
            return "非法请求"

        # 判断参数是否有值
        if not all([to_account, money]):
            flash("请完整输入参数")
            return render_template("transfer.html")

        # 执行转账操作
        print("假装执行转账操作，转给 %s, 转 %s" % (to_account, money))
        return "假装执行转账操作，转给 %s, 转 %s" % (to_account, money)

    # 生成随机值
    token = generate_token()
    # 将渲染模板的操作封装成响应
    resp = make_response(render_template("transfer.html", token=token))
    # 再存一份到 webB 不能取到的地方
    resp.set_cookie("cookie_token", token)
    return resp


# 生成随机值的函数
def generate_token():
    return base64.b64encode(os.urandom(48)).decode()

if __name__ == '__main__':
    app.run(debug=True)
