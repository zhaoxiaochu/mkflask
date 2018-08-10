# 1. 导入蓝图
from flask import Blueprint


# 2. 初始化蓝图
order_blu = Blueprint("order", __name__)


# 3. 使用蓝图去注册路由
@order_blu.route('/order/<order_id>')
def order_info(order_id):
    return "查询订单信息 %s" % order_id