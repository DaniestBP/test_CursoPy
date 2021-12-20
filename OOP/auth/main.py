import json
from hashlib import sha256
from deco import log
DB = "./users.json"

# def get_users(json_file):
#         with open(json_file, encoding="utf8 ") as file:
#             return json.load(file)


# def create_user(data, json_file):
#      with open (json_file, mode="w", encoding="utf8") as file:
#          json.dump(data, file, ensure_ascii=False, indent=4)

class User:
    def __init__ (self,name,pwd):
        self.name = name
        pwd_e = sha256(pwd.encode()).hexdigest()
        self.pwd = pwd_e


class Auth:
    def __init__(self,user,db):
        self.user = user
        self.db = db


    @property
    def users(self):
        with open(self.db, encoding="utf8 ") as file:
            return json.load(file)
    
    
    def create_user(self):
        data = self.users
        data["users"].append({"name": self.user.name, "pwd": self.user.pwd}) 
        with open (self.db, mode="w", encoding="utf8") as file:
            json.dump(data,file,ensure_ascii=False, indent=4) 
           
    @log
    def log_in(self,login_user):
        data = self.users
        list_login = list(filter(lambda u: u["name"] == login_user.name,data["users"]))
        try:
            confirmed_pwd = list_login[0]["pwd"] 
            if confirmed_pwd == login_user.pwd:
                return login_user
            else:
                return User("guest","")

        except:
            return User("guest","")   
            
        
        

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
            auth = Auth(user_instance, DB)
            auth.create_user()
            
        


    if user == "2":
        user_name = input("Introduzca su nombre: ").lower()
        passw = input("Escribe una contraseña: ")
        user_instance = User(user_name,passw)
        auth = Auth(user_instance, DB)
        auth.log_in(user_instance)
        input("...")
        
            
            
    
        

        

