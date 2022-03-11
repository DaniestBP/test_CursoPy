
from flask import Flask, message_flashed, session, request, render_template, redirect, url_for,flash
from uuid import uuid4
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import secrets

app = Flask(__name__)
DB_URI = "myguide.db"

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_URI}'
app.config["SECRET_KEY"] = "ea540ebab7830738308806b1e77a7b27c4808e27dc16b37b78977fb792a4a0f6"
DB_URI = "myguide.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique= True)
    pwd = db.Column(db.String(32), nullable = False )
    token = db.Column(db.String(16), unique =True, nullable = False)
    
    def __repr__(self):
        return f"EMAIL: {self.email} NAME: {self.name}"

class Advert(db.Model):
    id = db.Column(db.String(32), primary_key= True)
    user_id = db.Column(db.String(32), ForeignKey("user.id"))
    address = db.Column(db.String(60), nullable=False, unique= True)
    latitude = db.Column(db.String(11), nullable=True)
    longitude = db.Column(db.String(11), nullable=True)
    contact_phone = db.Column(db.String(12), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"id: {self.id} user: {self.user_id}"

class Upload(db.Model):
    id = db.Column(db.String(32), primary_key= True)
    advert_id = db.Column(db.String(32), ForeignKey("advert.id"))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    

"https://www.google.com/maps/place/Bernardo+Lima+48/@38.7401615,-9.1575212,15z"

@app.route("/")
def home():
    return render_template("base.html", text = "Welcome to MyGuide")
    

@app.route("/signup", methods = ["GET", "POST"])
def registration():
    verb = request.method
    if verb == "POST":
        email_u = request.form.get("email")
        name_u = request.form.get("name")
        pwd_u = request.form.get("pwd")
        try:
            if email_u and pwd_u:
                u_id = uuid4().hex
                token_new = secrets.token_hex(16)
                user_new = User(id=u_id, name=name_u, email = email_u, pwd = pwd_u, token = token_new)
                db.session.add(user_new)
                db.session.commit()
                res = redirect(url_for("login"))
                res.status_code = 307
                return res
        except:
            flash(f"This email {email_u} was already stored in our database")
            return render_template("signup.html")
    return render_template("signup.html", text = "Sign up")
 

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

@app.route("/auth")
@authorize
def auth():
    cookie_token = session.get("token")
    u = User.query.filter_by(token=cookie_token).first()
    user = u.id
    print(user)
    return redirect(url_for("dashboard" ,  user= user))


@app.route("/us_dashb/<user>", methods=["GET", "POST"])
def dashboard(user):
    verb = request.method
    if verb == "POST":
        photo = request.files["file"]
        if photo:
            pass
    cookie_token = session.get("token")
    u = User.query.filter_by(token=cookie_token).first()
    user = u.id
    u_adverts = Advert.query.filter_by(user_id = user).all()
    adverts = [advert for advert in u_adverts]
    
    return render_template("u_dashboard.html", text= f"{(u.name)}´s space", us_adverts=adverts)

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
                return redirect(url_for("auth"))
        except AttributeError:
            flash("Email or password incorrect")
            return render_template("login.html", text = "Log in")
    return render_template("login.html", text = "Log in")


descript_allowed = ["Solicitors", "Veterinary", "Hairdressing","Groceries", "Nursery Schools", "Condos' Management", "Hospitality", "Other"]

@app.route("/create_adv", methods= ["GET", "POST"])
def create_ad():
    verb = request.method
    u_token = session.get("token")
    print(u_token)
    u = User.query.filter_by(token=u_token).first()
    print(u)
    u_id = u.id
    print(u.id)
    if verb == "POST":
        address_ad = request.form.get("address")
        phone_ad = request.form.get("con_phone")
        email_ad = request.form.get("con_email")
        lat = request.form.get("lat")
        lon = request.form.get("lon")
        description = request.form.get("description")
        
        if description in descript_allowed:
            advert = Advert(id=uuid4().hex, user_id=u_id ,address= address_ad, latitude=lat, longitude=lon, contact_phone=phone_ad, contact_email=email_ad, description=description)
            db.session.add(advert)
            db.session.commit()
            res = redirect(url_for("dashboard", user=u_id))
            # res.status_code = 307
            return res
    return render_template("ad_creation.html", user=u_id, text=f"{u.name}, build it up!")
        

@app.route("/edit_spc/<adv_id>", methods= ["GET", "POST"])
def edit_space(adv_id):
    print(adv_id)
    advert = Advert.query.filter_by(id=adv_id).first()
    ad = Advert.query.get(adv_id)
    print(advert,ad)
    return render_template("customize.html")




@app.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("token", None)
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)