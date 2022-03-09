from flask import render_template, Blueprint,request,session,redirect,url_for,flash
from database import db
from functools import wraps
from uuid import uuid4
import secrets

users = Blueprint('users', __name__)

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique= True)
    pwd = db.Column(db.String(32), nullable = False )
    token = db.Column(db.String(16), unique =True, nullable = False)
    grades = db.Column(db.String(100), nullable= False) # nullable is True



@users.route("/")
def home():
    return render_template("base.html", text = "Welcome to PCEP tests")
    

@users.route("/signup", methods = ["GET", "POST"])
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
            res = redirect(url_for("users.login"))
            res.status_code = 307
            return res
        else:
            return {"success" : False}
    return render_template("index.html", text="Sign up")
 

@users.route("/login", methods=["GET", "POST"])
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
                return redirect(url_for("users.loquesea"))
        except AttributeError:
            flash("Email or password incorrect")
            return render_template("index.html", text = "Log in")
    return render_template("index.html", text = "Log in")
        


@users.route("/unsubs", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        email = request.form.get("email")       
        u = User.query.filter_by(email = email).first()
        if u.email == email:
            db.session.delete(u)
            session.pop("id", None)
            session.pop("token", None)
            db.session.commit()
            return redirect(url_for("users.home"))
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
        return redirect(url_for("users.login"))
    return i


@users.route("/secret")
@authorize
def loquesea():
    return redirect(url_for("tests.make_quiz"))

@users.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("token", None)
    return redirect(url_for('users.home'))