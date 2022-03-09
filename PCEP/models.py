
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique= True)
    pwd = db.Column(db.String(32), nullable = False )
    token = db.Column(db.String(16), unique =True, nullable = False)
    grades = db.Column(db.String(100), nullable= False) # nullable is True


# t_q = db.Table('Test_question',
#     db.Column('question_id', db.String(32), db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('question_id', db.Integer(32), db.ForeignKey('page.id'), primary_key=True)
# ) 

class Test(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.String(32), ForeignKey("user.id"))
    grade = db.Column(db.Float, nullable=True)

    questions = db.relationship("Questions", secondary="test_question", viewonly=True, backref=db.backref("test_question", lazy=True))
    answers = db.relationship("Test_question", backref=db.backref("test", lazy=True))

class Test_question(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    test_id = db.Column(db.String(32), ForeignKey("test.id"))
    question_id = db.Column(db.String(32), ForeignKey("questions.id"))
    user_choice =  db.Column(db.String(32), nullable = True)



class Questions(db.Model):
    id = db.Column(db.String(32), primary_key = True)
    question = db.Column(db.Text, nullable = False, unique=True)
    answer_id = db.Column(db.String(32))
    
    options = db.relationship("Options", backref= db.backref("questions", lazy=True))

    @classmethod
    def dict_q_a(cls):
        return {question.id : question.answer_id for question in cls.query.all()}
    # @property
    # def options(self):
    #     return Options.query.filter_by(questions_id=self.id).all()
    def __repr__(self):
        return f"ID: {self.id}  Question {self.question}"

class Options(db.Model):
    id = db.Column(db.String(32), primary_key = True)
    option = db.Column(db.Text, nullable = False)
    question_id = db.Column(db.String(32), ForeignKey("questions.id"))




# options= Options.query.filter_by(question_id="1").all()
# question = Questions.query.filter_by(id=id).all()
# options = question.options



