
# 1. 导入蓝图
from flask import Blueprint

# 2. 初始化蓝图
# 蓝图默认没有设置静态文件夹和模板文件夹，需要自己手动指定
# 一般蓝图在使用的时候都可以加上前缀
# 如果蓝图模块下的模板文件名与项目根目录下的模板文件存在同名的话，那么在渲染的时候，会使用项目根目录下的模板文件
cart_blu = Blueprint("cart", __name__, template_folder="templates", static_folder="static", url_prefix="/cart")

from .views import *

