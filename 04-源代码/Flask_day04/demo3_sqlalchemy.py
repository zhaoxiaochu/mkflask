from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库链接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/test9"

# 是否跟踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

# 初始化数据库操作对象
db = SQLAlchemy(app)

# 角色
class Role(db.Model):


    __tablename__ = "roles"  # 指定表名，如果不指定会以类名的小写做为表名

    # 定义主键 id，默认会自增长
    id = db.Column(db.Integer, primary_key=True)

    # 角色的称呼
    name = db.Column(db.String(128), unique=True)


    # 可以直接通过当前类的对象.users 就可以访问到当前角色对应的所有用户
    # backref 反向引用，表示给其前面的类添加一个属性()
    # 在此表示给 User 这个类添加 role 的属性，以便能够直接通过 user.role 访问到一的这一方的数据

    # 定义 relationship 在一的这一方定义
    # 第一个参数写多的这一方的类名，backref 写一的这一方的类名小写
    users = db.relationship("User", backref="role")


# 用户
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # 用户名
    name = db.Column(db.String(128), unique=True)
    # 邮箱
    email = db.Column(db.String(128), unique=True)
    # 用户密码
    password = db.Column(db.String(128))
    # 外键，db.ForeignKey 就是设置外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    # # 新增数据
    # ro1 = Role(name="admin")
    # ro2 = Role(name="user")
    # db.session.add_all([ro1, ro2])
    # db.session.commit()
    #
    # # 直接修改类的属性，再提交，就可以更改数据
    # ro1.name = "哈哈"
    # db.session.commit()
    #
    # # 删除
    # db.session.delete(ro1)
    # db.session.commit()

    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()

    """
    查询所有用户数据
        User.query.all()
    查询有多少个用户
        User.query.count()
    查询第1个用户
        User.query.first()
    查询id为4的用户[3种方式]
        User.query.get(4)
        User.query.filter(User.id == 4).first()
        User.query.filter_by(id=4).first()
    查询名字结尾字符为g的所有数据[开始/包含]
        User.query.filter(User.name.endswith('g')).all()
        # 开始 startswith
        # 包含 contains
    查询名字不等于wang的所有数据[2种方式]
        User.query.filter(User.name != 'wang').all()
        from sqlalchemy import not_
        User.query.filter(not_(User.name == 'wang')).all()
    查询名字和邮箱都以 li 开头的所有数据[2种方式]
        User.query.filter(User.name.startswith('li'), User.email.startswith('li')).all()
        from sqlalchemy import and_
        User.query.filter(and_(User.name.startswith('li'), User.email.startswith('li'))).all()
    查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
        User.query.filter(User.password == '123456', User.email.endswith('itheima.com')).all()
    查询id为 [1, 3, 5, 7, 9] 的用户列表
        User.query.filter(User.id.in_([1,3,5,7,9])).all()
    查询name为liu的用户所对应的角色数据
        role_id = User.query.filter(User.name == "liu").first().role_id
        Role.query.get(role_id)
    查询所有用户数据，并以email排序
        # 默认是 asc() 顺序 倒序就是在属性后面调用 desc()
        User.query.order_by(User.email.desc()).all()
    每页3个，查询第2页的数据
        # paginate 函数有三个参数，
            第1个表示查询第几页数据
            第2个表示每页多少个
            第3个如果有错是否抛出错误
            该函数的返回值是一个 paginate 对象

        paginate = User.query.paginate(2, 3, False)
        获取总页数
        paginate.pages
        获取当前页数
        paginate.page
        获取当前页数据
        paginate.items


    查询name 为 admin这个角色所有的用户
        方式1：
            role = Role.query.filter(Role.name == "admin").first()
            User.query.filter(User.role_id == role.id).all()
        方式2：
            Role.query.filter(Role.name == "admin").first().users

    查询 id 为 3 所对应的角色
        方式1：
            role_id = User.query.filter(User.id == 3).first().role_id
            Role.query.get(role_id)
        方式2：
            User.query.filter(User.id == 3).first().role
    """

    app.run(debug=True)
