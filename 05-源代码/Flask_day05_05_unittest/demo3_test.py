import unittest

from demo3 import app, db, Author


class DataBaseTest(unittest.TestCase):
    # 目标：测试 Author 能不能添加到数据库
    def setUp(self):
        # 配置为设置准备的数据库
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/booktest999"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.testing = True
        # 创建所有的表
        db.create_all()

    def tearDown(self):
        # 关闭数据库链接
        db.session.remove()
        # 移除所有的表
        db.drop_all()

    def test_add_author(self):
        # 初始化模型对象
        author = Author(name="老王")
        # 添加到数据库
        db.session.add(author)
        db.session.commit()

        author = Author.query.filter(Author.name == "老王").first()
        self.assertIsNotNone(author, "数据添加失败")

    def test_add_book(self):
        print("aaa")


if __name__ == '__main__':
    unittest.main()
