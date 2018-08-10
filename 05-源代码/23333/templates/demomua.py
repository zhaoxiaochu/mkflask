#-*coding:utf-8-*-
from flask import Flask
from flask import render_template
from flask.ext.wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:mysql@127.0.0.1:3306/ceshi1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
app.secret_key="kjjj"
class Append(FlaskForm):
    au_info = StringField(validators=[DataRequired()])
    bk_info = StringField(validators=[DataRequired()])
    submit = SubmitField(u'添加')
class Author(db.Model):
    __tablename__="tb_authors"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique=True)
    books=db.relationship("Book",backref="author")
class Book(db.Model):
    __tablename__="tb_books"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    author_id=db.Column(db.Integer,db.ForeignKey(Author.id))
@app.route("/",methods=['GET','POST'])
def index():
    authors= Author.query.all()
    return render_template("templ.html" ,authors=authors)
if __name__=="__main__":
    db.drop_all()
    db.create_all()
    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run(port=5664,debug=True)




