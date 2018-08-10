from flask import render_template

from . import cart_blu


# 3. 使用蓝图（注册路由）
@cart_blu.route('/list')
def cart_list():
    return render_template("cart.html")
