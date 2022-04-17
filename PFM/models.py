from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

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
    adv_name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(60), nullable=False, unique= True)
    latitude = db.Column(db.String(11), nullable=True)
    longitude = db.Column(db.String(11), nullable=True)
    contact_phone = db.Column(db.String(12), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    business_type = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"id: {self.id} user: {self.user_id}"

    images= db.relationship("Upload", backref=db.backref("advert", lazy=True))


class Upload(db.Model):
    id = db.Column(db.String(32), primary_key= True)
    advert_id = db.Column(db.String(32), ForeignKey("advert.id"))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)