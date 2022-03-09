from flask import render_template, Blueprint,request,session
from database import db
from uuid import uuid4
from random import shuffle
from sqlalchemy import ForeignKey
import json
from views.users.routes import User

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



tests = Blueprint('tests', __name__)

@tests.route("/exam", methods = ["GET","POST"])
def make_quiz():
    verb = request.method
    questions = Questions.query.all()
    shuffle(questions)
    (shuffle(question.options) for question in questions[0:10])
    options = Options.query.all()
    result = 0
    if verb == "POST":
        for k, v in request.form.items():
            question = Questions.query.filter_by(id=k).first()
            if v == question.answer_id:
                result += 1
        return {"result": result}
    return render_template("quiz.html", questions = questions[0:10], options = options)
        
        
@tests.route("/to_database")
def to_database():
    def get_data():
        with open ("pcep.json") as file:
            return json.load(file)
    
    q_total = get_data()
    for block in list(q_total.values())[1:]:
        for quizz in block:
            q_id= uuid4().hex
            q = quizz["question"]
            the_answer_index = quizz["answer"]
            id_ans= None
            for i , opt in enumerate(quizz["options"]):
                op_id = uuid4().hex
                options_inser =  Options(id=op_id, option=opt, question_id = q_id)
                db.session.add(options_inser)
                if i == the_answer_index :
                    id_ans = op_id
            questions_inser = Questions(id=q_id, question =q, answer_id= id_ans)
            db.session.add(questions_inser)
        # db.session.commit()   
    return "created"
            
    
@tests.route("/api/grade", methods = ["GET", "POST"])
def coo():
    if request.method == "POST":
        q_a = Questions.dict_q_a() #Hemos definido una clase de metodo en models.py dentro de Questions llamado dict_q_a para convertir a diccionario el id de la pregunta y el id de la respuesta correcta
        answers = request.get_json()
        print(answers)
        result = {"grade":0, "answers":{}}
        for answer in answers:
            if answer[1]:
                result["answers"][answer[1]] = False
            if q_a[answer[0]] == answer[1]:
                result["grade"] +=1
                result["answers"][answer[1]] = True
            
            
        
        ses_token = session.get("token")
        u= User.query.filter_by(token=ses_token).first()
        t_id = uuid4().hex
        test = Test(id=t_id, user_id = u.id , grade = result["grade"] )
        db.session.add(test)
            
        for answer in answers:   
            q_id = answer[0]
            u_ans =answer[1]
            test_q = Test_question(id=uuid4().hex, test_id =t_id, question_id=q_id, user_choice = u_ans)
            db.session.add(test_q)
            
        # db.session.commit()
        print(result)    
    return result
            

          

                


        
        
            

# @tests.route("/api/test_rec", methods = ["GET", "POST"])
# def create_test_q():
#     # t_q_id  = uuid4().hex
#     # t_id = "596bfcaca8bb48588762ca032d553bc1"
#     # q_id = "ee125487fc6c46eb88db4f8c8e3ee5b5"
#     # u_c = "1cf48916b7414368ab4b87c22bdddbcb"
#     # testQ = Test_question(id=t_q_id, test_id = t_id, question_id=q_id, user_choice = u_c)
#     # db.session.add(testQ)
#     # db.session.commit()
#     return {"success": True}
