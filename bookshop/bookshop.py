########################     Function creation exercice: managing a bookshop
# comented

from functools import total_ordering
from os import path
import csv

cwd = path.dirname(__file__)

DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

# DB = []

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

user = "0"



def read_csv(dataset, file_name):
    with open(file_name, mode="r", enconding ="utf8")as file:
        csv_reader= csv.reader(file, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            new_dict = {
                "id" : row[1],
                "author": row[0],
                "title": row[1],
                "genre": row[2]
            }
            DB.append(new_dict)

read_csv(DB, "books.csv")
    


def export_csv(dataset, file_name):
    with open(file_name, mode="w", newline="", encoding="utf8")as file:
        csv_writer= csv.writer(file, delimiter = ";")
        csv_writer.writerow(["id", "author", "title", "genre"])
        for entry in dataset:
           csv_writer.writerow(entry.values())





def menu():
    print("BIENVENIDO A LIBRERIA FANTASIA".center(90, "-"))
    print("Busque su libro".center(30))
    print("1. Id: " + (" "* (49 - len("1. Id: "))) + "#")
    print("2. Title: " + (" "* (49 - len("2. Title: "))) + "#")
    print("3. Author: " + (" "* (49 - len("3. Author: "))) + "#")
    print("4. Genre: " + (" "* (49 - len("4. Genre: "))) + "#")
    print("5. Update: " + (" "* (49 - len("5. Update: "))) + "#")
    print("6. Eliminar libros: " + (" "* (49 - len("6. Eliminar libros: "))) + "#")
    print("Q. Salir: " + (" "* (49 - len("Q. Salir: "))) + "#")
    print("#"*50)




def search_id(usuario_id):
    
    for libro in DB:
        if libro["id"].lower() == usuario_id:
            return libro
    return None    
    
def search_title(usuario_title):
    
    for libro in DB:
        if libro["title"] == usuario_title:
            return libro
    return None
def search_author(usuario_author):
    
    for libro in DB:
        if libro["author"] == usuario_author:
            return libro
    return None
def search_genre(usuario_genre):

    for libro in DB:
        if libro["genre"] == usuario_genre:
            return libro 
    return None



def pretty_book(book):
    for k, v in book.items():
        print(f"{k}: {v}")


def get_by_term(term, search_term):
    result = []
    for book in DB:
        if book[term].lower().find(search_term.lower()) >= 0:
            result.append(book)    
    return result        

def update_book(book):
    print("Si no desea modificar pulse Enter")
    for k, v in list(book.items())[1:]:
        user = input(f"{k}: ")
        if user:
            book[k] = user
       
def write_to_record(search_term, to_write):
    with open(f"{cwd}/test.txt", mode="a") as file:
        if type(to_write) == dict:
            file.write(f"Se ha buscado {search_term}: {to_write['author']} - {to_write['title']}\n")
        elif type(to_write) == list:
            file.writelines(to_write)
            



# while user != "q":
#     menu()

#     user = input(": ")
#     if user == "1":
#         user = input("Escriba el ID: ")
#         books = get_by_term ("id", user)
#         if len(books):
#             for book in books:
#                 pretty_book(book)
#         else:
#             print("No se ha encontrado NINGÚN RESULTADO")
    
#     elif user == "2":
#         user = input("Escriba el Titulo:  ")
#         books = get_by_term ("title", user)
#         if len(books):
#             for book in books:
#                 pretty_book(book)
#         else:
#             print("No se ha encontrado NINGÚN RESULTADO")

