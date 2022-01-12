import datetime as dt
import requests as req
import json

# def outer(func_to_decorate):  # DECORATOR: agrega funcionalidad a la funcion que le pasamos a traves de otra función interna
#     def inner(name):
#         return f"{func_to_decorate(name)}!".upper()
#     return inner

# @outer
# def greeting(name):
#     return f"Hola {name}"

# print(greeting("Dani"))

#con la def the outer() (DECORADORA) podremos "decorar" otras funciones. En este caso decoramos el "hola" con una exclamación


# def outer(func_to_decorate):
#     def inner():
#         return func_to_decorate() #haciendo con esa funcion a decorar lo que queramos hacer como en el ejemplo anterior.
#     return inner

# AHORA CUALQUIER FUNCION QUE QUERAMOS DECORAR (AÑADIRLE LA FUNCIONALIDAD QUE HEMOS DEFINIDO) SOLO TEHEMOS QUE COLOCALE " @<nombre de la funcion decorator>"


def log(func):
    def inner(*args,**kwargs):
        time = dt.datetime.now()
        result = func(*args, **kwargs)
        user = args[1]["name"]
        with open("./login.log", "a", encoding="utf8")as file:
            try:
                if result == True:
                    file.write(f"{time} | Usuario: {user} logged in.\n")
            except:
                    file.write(f"{time} | La función {func.__name__} se ha ejecutado\n")
        return result
    return inner
        

def authentication(func):
        def inner(*args,**kwargs):
            result = func(*args, **kwargs)
            # token_user = args[1]["token"]
            user_name = (args[1]["name"], args[1]["token"])
            # token = str({"name":user_name, "token": token_user})
            with open("./cookies.json", "a",encoding="utf8")as file:
                if result:
                    json.dump(user_name, file,ensure_ascii=False, indent=4 )
                else:
                    print("Authentication failure")
            return True
        return inner
               



# @log
# def greeting():
#     return "Hola"

# @log
# def goodbye():
#     return "Adios"

# @log
# def add(a,b):
#     return a +b

# print(greeting())
# # print(goodbye())

# print(add(1,2))


    


