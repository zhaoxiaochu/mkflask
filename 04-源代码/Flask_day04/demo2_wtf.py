from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
app.secret_key = "aaaa"


class RegisterForm(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired("请输入用户名")], render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码：", validators=[DataRequired("请输入密码")])
    password2 = PasswordField("确认密码：", validators=[DataRequired("请输入确认密码"), EqualTo('password', '密码与确认密码不一致')])
    submit = SubmitField("注册")


@app.route('/demo2', methods=["get", "post"])
def demo2():
    register_form = RegisterForm()
    if register_form.validate_on_submit():  # 验证表单的内容是否符合我们的要求，如果符合，那么会返回 True
        # 1. 取到注册所对应的数据
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # 2. 执行注册操作
        # 可能执行注册操作，往我们的数据库里面添加一个用户的数据
        print("%s %s %s" % (username, password, password2))
        return "注册成功"
    else:
        if request.method == "POST":
            return render_template('temp2_wtf.html', form=register_form)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1', methods=["GET", "POST"])
def demo1():
    # 判断如果请求方式是 POST 的话，代表是注册请求
    if request.method == "POST":
        # 1. 取到注册所对应的数据
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # 2. 判断取出来的变量是否有值
        if not all([username, password, password2]):
            flash("请填写所有的数据")
            return render_template("temp2.html")

        # 3. 判断密码和确认密码是否一致
        if password != password2:
            flash("密码与确认密码不一致")
            return render_template("temp2.html")

        # 可能执行注册操作，往我们的数据库里面添加一个用户的数据
        print("%s %s %s" % (username, password, password2))
        return "注册成功"

    # 如果是 get 的话，代表是加载注册页面
    return render_template("temp2.html")


if __name__ == '__main__':
    app.run(debug=True)
