import json
from hashlib import new, sha256
from deco import log
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

class Admin(User):
    def __init__(self, name, pwd):
        super().__init__(name, pwd)
        self.is_admin = True

    def user_update(self, old_name, new_name, auth):
        users = auth.users
        for user in users["users"]:
            if user["name"] == old_name:
                user["name"] = new_name
                break
        auth.write_data(users, auth.db)

        
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


    def get_user(self, user_name):
        db_user = next(filter(lambda db_user: db_user["name"] == user_name, self.users["users"]), False)
        return db_user

    def write_data(self, new_data, json_file):
        data = open(json_file, "w", encoding="utf8")
        json.dump(new_data, data,ensure_ascii=False, indent=4 )
        data.close()
    
  
    @log 
    def log_in(self,user):
        i, db_user = next(filter(lambda db_user: db_user[1]["name"] == user["name"],enumerate(self.users["users"])),(None, False))
        if db_user:
            if db_user["pwd"] == user["pwd"]:
                db_user["token"] = self.create_token(db_user)
                
                data = self.users
                data["users"][i] = db_user
                self.write_data(data, self.db)
                
                cookies = self.cookies
                cookies["tokens"] = {"name": db_user["name"], "token":db_user["token"]}
                self.write_data(cookies,"./cookies.json" )

                return True
            else:
                return False
        else:
            return False

    
    def authentication(self, f_to_deco):
        def inner():
            user_name, user_token = self.cookies["tokens"].values()
            db_user = self.get_user(user_name)
            if db_user:
                if db_user["token"] == user_token:
                    
                    return f_to_deco()
                else:
                    return False
            else:
                return False
        return inner()
           
    def is_admin(self, f):
        def inner():
            user_name, _ = self.cookies["tokens"].values()
            db_user = self.get_user(user_name)
            try:
                if db_user ["is_admin"]:
                    return f()
            except:
                print("\n" + f" Lo sentimos, {user_name}. Sólo usuarios admin pueden hacer cambios ".center(100, "-")+"\n")
                return None
        return inner 

    

auth = Auth(DB)   
user = ""

while user != "q":
    print("\n"+" Bienvenido ".center(150 - len("Bienvenido"), "*") + "\n")
    print("1. Crear Usuario \n".center(150- len("1. Crear Usuario ")))
    print("2. Log in \n".center(145 - len("2. Log in ")))
    print("3. Editar usuario(sólo admin)    " "\n".center(158 - len("3. Editar usuario(sólo admin)")))
    print("\n"+"Pulse Q para salir\n")

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
        elif passw.isalpha():
            print("\nFalta algún número")
        elif passw.isnumeric():
            print("\nNo pueden ser todo números")
        elif passw.isidentifier():
            print("\nFalta algun símbolo.(No se considera '_' un símbolo)")
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
            print(f"\nLo sentimos.No tenemos ningún usuario con estas credenciales")

    elif user == "3":
        @auth.authentication
        @auth.is_admin
        def update_user():
            for i, user in enumerate(auth.users["users"]):
                print(f"{i+1}:{user['name']}")
            user = int(input(":")) - 1
            new_name = input("Nuevo nombre: ")
            admin_instance = Admin("admin", "1234")
            print("Está seguro?")
            decision = input("Y/N: ")
            if decision.lower() == "y":
                admin_instance.user_update(auth.users["users"][user]["name"], new_name, auth)
                print("Los cambio se han realizado")
            else:
                print("No hemos podido realizar los cambios")



            
       
        
        
        
        

        

