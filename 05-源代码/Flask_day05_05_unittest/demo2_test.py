# 导入单元测试的类
import unittest

from flask import json

from demo2 import app


# 自定义类继承于 unittest.TestCase
class LoginTest(unittest.TestCase):
    def setUp(self):
        """初始化，在所有的测试开始之后会调用 setUp方法，这个方法里面可以做：开启测试模式的操作，做测试配置的操作"""
        # 表示当前正在测试，开启测试模式
        app.testing = True

    def tearDown(self):
        """在所有的测试函数被执行之后会调用，可以在这里面做一些数据清理操作"""
        pass

    # 测试用户名和密码某一个为空的时候是否返回正确
    def test_empty_username_password(self):
        response = app.test_client().post("/login", data={})
        resp_dict = json.loads(response.data)

        # 1. 断言不为空
        self.assertIsNotNone(resp_dict, "返回数据为空")
        # 2. 断言字典中有 errcode
        self.assertIn("errcode", resp_dict, "返回的数据格式有误")
        # 3. 断言errcode 为 -2
        errcode = resp_dict.get("errcode")
        self.assertEqual(errcode, -2, "返回的错误码有误")



        # 测试用户名和密码输入错误的时候是否返回正确

        # 测试用户各和密码输入正确的时候是否返回正确
