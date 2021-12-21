import json
from hashlib import sha256
from deco import authentication, log
from random import random


DB = "./users.json"

SECRET = b"perro"

class User:
    def __init__ (self,name,pwd):
        self.name = name
        pwd_e = sha256(pwd.encode()).hexdigest()
        self.pwd = pwd_e

    @property
    def user_dict(self):
        return {
            "name": self.name,
            "pwd": self.pwd
        }

class Auth:
    def __init__(self,db):
        self.db = db
        

    @property
    def users(self):
        with open(self.db, encoding="utf8") as file:
            return json.load(file)
    
    @property
    def cookies(self):
        with open("./cookies.json", encoding = "utf8")as file:
            return json.load(file)
    
    def create_user(self,user):
        data = self.users
        data["users"].append(user) 
        with open (self.db, mode="w", encoding="utf8") as file:
            json.dump(data,file,ensure_ascii=False, indent=4) 


    def create_token(self,user):
        token = sha256(user["name"].encode())
        token.update(SECRET)
        token.update(str(random()).encode())
        return token.hexdigest()


    def get_user(self):
        db_user = next(filter(lambda db_user: db_user[1]["name"] == user["name"], self.users["users"]), False)
        return db_user

    
    # @authentication
    # @log 
    def log_in(self,user):
        i, db_user = next(filter(lambda db_user: db_user[1]["name"] == user["name"],enumerate(self.users["users"])),(None, False))
        if db_user:
            if db_user["pwd"] == user["pwd"]:
                db_user["token"] = self.create_token(db_user)
                data = self.users
                data["users"][i] = db_user
                users_db = open(self.db, "w", encoding="utf8")
                json.dump(data, users_db,ensure_ascii=False, indent=4 )
                users_db.close()
                cookies = self.cookies
                cookies["tokens"] = {"name": db_user["name"], "token":db_user["token"]}
                cookies_db = open("./cookies.json", "w", encoding="utf8")
                json.dump(cookies, cookies_db,ensure_ascii=False, indent=4)
                cookies_db.close()
                return True
            else:
                return False

        else:
            return False

                
    
    def authentication(self, f):
        user_name, user_token = self.cookies["token"].values()
        db_user = self.get_user(user_name)
        def inner():
            if db_user:
                if db_user["token"] == user_token:
                    return f()
                else:
                    return False
            else:
                return False
        return inner
           
                     


auth = Auth(DB)   
user = ""

while user != "q":
    print("\n"+" Bienvenido ".center(150 - len("Bienvenido"), "*") + "\n")
    print("1. Crear Usuario \n".center(150- len("1. Crear Usuario ")))
    print("2. Log in \n".center(145 - len("2. Log in ")))
    print("Pulse Q para salir\n".center(150- len("Pulse Q para salir")))

    user = input("Escoja: ")
        
    if user == "1":
        print("\n< Solo se considera válidas contraseñas con igual o más de 6 caracteres, que contengan alguna mayúscula y minúscula, algún número y algún símobolo >".center(80,"*")+ "\n")
        user_name = input("Introduzca su nombre: ").lower()
        passw = input("Escribe una contraseña: ")
        if len(passw) < 8:
            print("\nComo mínimo 8 caracteres")
        elif passw.islower():
            print("\nFalta alguna mayúscula")
        elif passw.isupper():
            print("\nFalta alguna minúscula")
        elif passw.isnumeric():
            print("\nNo pueden ser todo números")
        elif passw.isalpha():
            print("\nFalta algun símbolo")
        else:
            user_instance = User(user_name,passw)
            auth.create_user(user_instance.user_dict)           
        
    elif user == "2":
        user_name = input("Introduzca su nombre: ").lower()
        passw = input("Escribe una contraseña: ")
        user_instance = User(user_name,passw)
        if auth.log_in(user_instance.user_dict):
            print(f"\nBienvenido {user_instance.name}. Se ha logueado correctamente.")
        else:
            print("\nLo sentimos.No tenemos ningún usuario con estas credenciales")

    elif user == "3":
        @auth.authentication
        def restricted_menu():
            print( "\nSección restrigida")


            
        input("...")

        
        
        
        

        

