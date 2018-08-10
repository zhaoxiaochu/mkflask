from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "aaaa"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/booktest9"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class AppendForm(FlaskForm):
    """自定义类继承于 FlaskForm，用于书籍添加的表单"""
    authorname = StringField("作者：", validators=[DataRequired("请输入作者名")])
    bookname = StringField("书籍：", validators=[DataRequired("请输入书名")])
    submit = SubmitField("添加")


class Author(db.Model):
    __tablename__ = "tb_authors"
    # 定义主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义关系，以便多的一方和一的一方能够快速互相访问
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tb_books"
    # 定义主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/deleteauthor/<author_id>')
def delete_author(author_id):
    # 查询书籍
    author = Author.query.get(author_id)

    # 先删除书籍
    try:
        Book.query.filter(Book.author_id == author.id).delete()
        db.session.delete(author)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

    return redirect(url_for("index"))


@app.route('/deletebook/<book_id>')
def delete_book(book_id):
    # 1. 查询出来要删除的书籍
    book = Book.query.filter(Book.id == book_id).first()
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

    return redirect(url_for("index"))


@app.route('/', methods=["GET", "POST"])
def index():
    form = AppendForm()
    # 验证表单内数据是否满足我们的要求
    if form.validate_on_submit():
        # 也可以通过表单属性去取到 input 里面的值
        author_name = form.authorname.data
        book_name = form.bookname.data

        # 去通过作者名字查询作者对象
        author = Author.query.filter(Author.name == author_name).first()
        # if 作者存在：
        if author:
            # 0. 判断当前作者是否有同名的书籍，如果没有，再执行第1步
            book = Book.query.filter(Book.name == book_name, Book.author_id == author.id).first()
            if not book:
                # 1. 创建一本书，指定外键为作者的 id
                book = Book(name=book_name, author_id=author.id)
                # 2. 将该书添加到数据库
                try:
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    # 如果添加书籍失败，就回滚
                    db.session.rollback()
                    print(e)
                    flash("添加书籍失败")
            else:
                flash("当前作者已存在同名书籍")
        else:
            # 代表作者不存在
            # 1. 创建作者对象，添加到数据库
            author = Author(name=author_name)
            try:
                db.session.add(author)
                db.session.commit()

                # 2. 创建书的对象，指定外键为第1步的作者的 id，
                book = Book(name=book_name, author_id=author.id)
                try:
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    flash("添加数据失败")
            except Exception as e:
                print(e)
                db.session.rollback()
                flash("添加数据失败")

                # author = Author(name=author_name)
                # book = Book(name=book_name)
                # # 将 book 和 author 关联起来
                # book.author = author
                # try:
                #     db.session.add(author)
                #     db.session.add(book)
                #     db.session.commit()
                # except Exception as e:
                #     print(e)
                #     db.session.rollback()
                #     flash("添加数据失败")

    else:
        if request.method == "POST":
            flash("数据输入不完整")

    # 查询所有的作者数据，传入到模板中
    authors = Author.query.all()
    return render_template("temp1.html", authors=authors, form=form)


if __name__ == '__main__':
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

    app.run(debug=True)
