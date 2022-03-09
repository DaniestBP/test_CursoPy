from flask import Flask, url_for
from views.users.routes import users
from views.tests.routes import tests

from database import db
import os

DB_URI = "multitest.db"
def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_URI}'
    app.config["SECRET_KEY"] = "ea540ebab7830738308806b1e77a7b27c4808e27dc16b37b78977fb792a4a0f6"
    app.register_blueprint(users, url_prefix ="/users")
    app.register_blueprint(tests, url_prefix ="/tests")
    db.init_app(app)
    return app


def set_db(app):
    with app.app_context():
        db.create_all()



if __name__ == "__main__":
    app = create_app()
    if not os.path.isfile("multitest.db"):
        set_db(app)
    app.run(debug=True)






# from flask import Flask, session, request, render_template
# from flask_sqlalchemy import SQLAlchemy
# from uuid import uuid4
# from sqlalchemy import ForeignKey



# app = Flask(__name__)
# DB_URI = "test.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_URI}'
# db = SQLAlchemy(app)


# class Owner(db.Model):
#     id = db.Column(db.String(10), primary_key = True)
#     name = db.Column(db.String(60), nullable= False)
    
#     def __repr__(self):
#         return f"ID: {self.id} NAME: {self.name}"

# class Dog(db.Model):
#     id  = db.Column(db.String(32), primary_key=True)
#     name = db.Column(db.String(60), nullable= False)
#     age = db.Column(db.Integer, nullable = False)
#     owner_id = db.Column(db.String, ForeignKey("owner.id")) # --> FOREIGN KEY (owner_id) REFERENCES owner(id)

#     def __repr__(self):
#         return f"ID: {self.id} NAME: {self.name}"


# @app.route("/create")
# def create():
#     user_id = request.args.get("id")
#     user_name = request.args.get("name")
#     if user_id and user_name:
#         to_add = Owner(id=user_id, name=user_name)
#         db.session.add(to_add)
#         db.session.commit()
#     return "Create"

# @app.route("/id/<user_id>" , methods = ["GET", "PUT", "POST", "DELETE"])
# def get_by_id(user_id):
#     result = Owner.query.filter_by(id=user_id).first() # .first() nos entrega el elemento si es unico. POdemos usar .all() que nos entregará una lista si es que hay mas elementos que cumplen la premisa indicada. 
#     print(result.name)
#     if request.method == "PUT":
#         new_name = request.args.get("name")
#         if new_name:
#             result.name = new_name
#             db.session.add(result)
#             db.session.commit()

#     elif request.method == "POST":
#         owner_id = result.id
#         dog_id = uuid4().hex
#         new_dog = Dog(id=dog_id , name = request.args.get("name"), age=5, owner_id= owner_id )
#         db.session.add(new_dog)
#         db.session.commit()
#         dog = Dog.query.filter_by(id=dog_id).first()
#         print(dog)
#         return dog.__repr__()

#     elif request.method == "DELETE":
#         name_to_delete = request.args.get("name")
#         result = Dog.query.filter_by(name=name_to_delete).first()
#         db.session.delete(result)
#         db.session.commit()

#     return result.__repr__()

# if __name__ == "__main__":
#     app.run(debug=True)