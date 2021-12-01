########################     Function creation exercice: managing a bookshop
# comented

# from functools import total_ordering
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
    "id": "ne_2",
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
    "id": "ne_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Las Armas y las Letras",
    "author": "Andres Trapiello",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

# DB = []

user = "0"


    

def menu():
    print("\n" + "BIENVENIDO A LIBRERIA FANTASIA".center(190, "-")+"\n")
    print("\n" + "Busque su libro".center(130)+"\n"*2)
    print("1. Id: " + (" "* (149 - len("1. Id: "))) + "#"+"\n")
    print("2. Title: " + (" "* (149 - len("2. Title: "))) + "#"+"\n")
    print("3. Author: " + (" "* (149 - len("3. Author: "))) + "#"+"\n")
    print("4. Genre: " + (" "* (149 - len("4. Genre: "))) + "#"+"\n")
    print("5. Update: " + (" "* (149 - len("5. Update: "))) + "#"+"\n")
    print("6. Eliminar libros: " + (" "* (149 - len("6. Eliminar libros: "))) + "#"+"\n")
    print("Q. Salir: " + (" "* (149 - len("Q. Salir: "))) + "#"+"\n")
    print("\n" + "#"*150)




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
    with open(f"{cwd}/test.txt", mode="a+", encoding="utf8") as file:
        if type(to_write) == dict:
            file.write(f"Se ha buscado {search_term}: {to_write['author']} - {to_write['title']}\n")
        elif type(to_write) == list:
            file.writelines(to_write)
            

def read_csv(dataset, file_name):
    with open(file_name, mode="r", enconding ="utf8")as file:
        csv_reader= csv.reader(file, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            new_dict = {
                "id" : row[0],
                "title": row[1],
                "author": row[2],
                "genre": row[3]
            }
            DB.append(new_dict)

# read_csv(DB, "books.csv")



def export_csv(dataset, file_name):
    with open(file_name, mode="w", newline="", encoding="utf8")as file:
        csv_writer= csv.writer(file, delimiter = ";")
        csv_writer.writerow(["id", "title", "author", "genre"])
        for entry in dataset:
           csv_writer.writerow(entry.values())



