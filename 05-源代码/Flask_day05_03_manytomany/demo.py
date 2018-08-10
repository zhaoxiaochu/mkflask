from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库链接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/manytomany9"
# 是否跟踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

# 初始化数据库操作对象
db = SQLAlchemy(app)

# 学生与课程的对应表关系
# 一张表里面可以有多个主键，表示多个主键联结起来在当前这张表里面不能有重复数据，定义方式就是在多个字段后面添加  primary_key=True
tb_student_course = db.Table("tb_student_course",
                             db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
                             db.Column("course_id", db.Integer, db.ForeignKey("course.id"))
                             )


# 定义学生的模型
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    # 表示当前学生选择的所有课程
    # secondary 指定多对多关联关系中的中间表
    courses = db.relationship("Course", lazy="dynamic", secondary=tb_student_course, backref=db.backref("students", lazy="dynamic"))


class Course(db.Model):
    # 主键 id
    id = db.Column(db.Integer, primary_key=True)
    # 课程名字
    name = db.Column(db.String(64))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    db.session.add_all([stu1, stu2, stu3])
    db.session.add_all([cou1, cou2, cou3])

    # 设置他们的关联关系
    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.commit()
    app.run(debug=True)
