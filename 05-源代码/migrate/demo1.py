from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# 配置数据库链接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/test9"
# 是否跟踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

# 初始化数据库操作对象
db = SQLAlchemy(app)

manager = Manager(app)
# 1. 先将 app 与 db 关联
Migrate(app, db)
# 2. 将数据库的迁移命令添加到 flask-script 里面
manager.add_command('db', MigrateCommand)


# 步骤：
# 1. 生成迁移所需要的文件夹  python xxx.py aaa init (一个项目只需要做一次)
# 2. 生成指定版本的迁移文件  python xxx.py aaa migrate -m "注释" （迁移一次执行一次）
# 3. 执行迁移 将当前模型映射到表中 python xxx.py aaa upgrade

# 4. python xxx.py db upgrade/downgrade [版本号]
# 5. 查看当前项目所有的迁移版本 　 python xxx.py db history
# 6. 可看项目当前处于哪一个迁移版本 python xxx.py db current


# 角色
class Role(db.Model):
    __tablename__ = "roles"  # 指定表名，如果不指定会以类名的小写做为表名

    # 定义主键 id，默认会自增长
    id = db.Column(db.Integer, primary_key=True)
    # 角色的称呼
    name = db.Column(db.String(128), unique=True)

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
    # 添加了一个字段
    # nickname = db.Column(db.String(128))
    # 再添加一个字段
    # bbb = db.Column(db.String(128), unique=True)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()
