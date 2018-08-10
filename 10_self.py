#-*coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:mysql@127.0.0.1:3306/test12"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False,
db=SQLAlchemy(app)
class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer,primary_key=True)
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
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123598', role_id=ro1.id)
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


    app.run(debug=True)
