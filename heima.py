#-*coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:mysql@127.0.0.1:3306/test6"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class Role(db.Model):
    __tablename__="roles"
    idss=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique=True)
    user=db.relationship("User",backref="role")
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique=True)
    password=db.Column(db.String(128))
    email=db.Column(db.String(128),unique=True)
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))

@app.route("/")
def index():

    return "index"
if __name__=="__main__":
     db.create_all()
     # print(User.query.all)
     app.run(port=5999)


"""
    查询所有用户数据
        User.query.all()
        User.query.all（）
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
            第1个表示查询第几页数据W
            第2个表示每页多少个
            第3个如果有错是否抛出错误
            该函数的返回值是一个 paginate 对象"""