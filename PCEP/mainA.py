from functools import wraps
from flask import Flask, make_response, session, request, render_template, redirect, url_for,flash
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import secrets
from models import db, User, Questions, Options,Test, Test_question
import json
from random import shuffle

app = Flask(__name__)

DB_URI = "multitest.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_URI}'
app.config["SECRET_KEY"] = "ea540ebab7830738308806b1e77a7b27c4808e27dc16b37b78977fb792a4a0f6"

db.init_app(app) # inicialmente teniamos las sintaxis (( db = SQLAlchemy(app) )) para llevar los modelos de tablas a models.py y hacer la importacion aqui, daba error de importacion circular. Por eso hemos cambiado la  sintaxis.

# with app.app_context():
#         db.create_all()

@app.route("/")
def home():
    question = Questions.query.first()
    return render_template("base.html", text = "Welcome to PCEP tests")


@app.route("/signup", methods = ["GET", "POST"])
def registration():
    verb = request.method
    if verb == "POST":
        email_u = request.form.get("email")
        pwd_u = request.form.get("pwd")
        if email_u and pwd_u:
            u_id = uuid4().hex
            token_new = secrets.token_hex(16)
            user_new = User(id=u_id, email = email_u, pwd = pwd_u, token = token_new, grades = "" )
            db.session.add(user_new)
            db.session.commit()
            res = redirect(url_for("login"))
            res.status_code = 307
            return res
        else:
            return {"success" : False}
    return render_template("index.html", text="Sign up")
 

@app.route("/login", methods=["GET", "POST"])
def login():
    verb = request.method
    if verb == "POST":
        email_u = request.form.get("email")
        pwd_u = request.form.get("pwd")
        result = User.query.filter_by(email=email_u).first()
        try:
            if result.pwd == pwd_u:
                new_token = secrets.token_hex(16)
                session["token"] = new_token
                session["id"] = result.id
                result.token = session["token"]
                db.session.add(result)
                db.session.commit()
                return redirect(url_for("loquesea"))
        except AttributeError:
            flash("Email or password incorrect")
            return render_template("index.html", text = "Log in")
    return render_template("index.html", text = "Log in")
        


@app.route("/unsubs", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        email = request.form.get("email")       
        u = User.query.filter_by(email = email).first()
        if u.email == email:
            db.session.delete(u)
            session.pop("id", None)
            session.pop("token", None)
            db.session.commit()
            return redirect(url_for("home"))
        return "email does not match"
    return render_template("index.html", text = "Enter your credentials to unsubscribe")


def authorize(f):
    @wraps(f)
    def i():
        cookie_id = session.get("id")
        cookie_token = session.get("token")
        if cookie_id and cookie_token:
            cookie_conf = User.query.filter_by(token=cookie_token).first()
            if cookie_conf.token == cookie_token:
                return f()
        return redirect(url_for("login"))
    return i


@app.route("/secret")
@authorize
def loquesea():
    return redirect(url_for("make_quiz"))


@app.route("/exam", methods = ["GET","POST"])
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
        
        
        
@app.route("/to_database")
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
            
    
@app.route("/api/grade", methods = ["GET", "POST"])
def coo():
    if request.method == "POST":
        q_a = Questions.dict_q_a() #Hemos definido una clase de metodo en models.py dentro de Questions llamado dict_q_a para convertir a diccionario el id de la pregunta y el id de la respuesta correcta
        # print(q_a["a5c0f5a6ebdd4809b9af4f3d745e06f5"])
        answers = request.get_json()
        print(answers[0])
        result = {"grade":0, "answers":{}}
        for answer in answers:
            result["answers"][answer[1]] = False
            print(answer[0])
            if q_a[answer[0]] == answer[1]:
                result["grade"] +=1
                result["answers"][answer[1]] = True
    return result
            

@app.route("/test_question")
def create_test_q():
    t_q_id  = uuid4().hex
    t_id = "596bfcaca8bb48588762ca032d553bc1"
    q_id = "ee125487fc6c46eb88db4f8c8e3ee5b5"
    u_c = "1cf48916b7414368ab4b87c22bdddbcb"
    testQ = Test_question(id=t_q_id, test_id = t_id, question_id=q_id, user_choice = u_c)
    db.session.add(testQ)
    db.session.commit()
    return {"success": True}



# @app.route("/test_question")
# def create_test_q():
   
#     return {"success": True}


@app.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("token", None)
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)