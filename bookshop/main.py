from bookshop import *
from os import path


cwd = path.dirname(__file__)


# with open(f"{cwd}/errors.log", mode="a") as file:
#     file.write("Error 1: Missing User ID")

# fichero = open("./lectura/test.txt")
# lectura = fichero.read()

# Análisis del fichero:

# mama = lectura[(lectura.find("mama")):]
# print(mama)

# with open("./test.txt", mode="a") as file:
#     file.write("Hola papá")


# fichero.close()
    
    
user = "0"

while user != "q":
    menu()

    user = input(": ")
    if user == "1":
        user = input("Escriba el ID: ")
        books = get_by_term ("id", user)
        if len(books):
            for book in books:
                pretty_book(book)
                write_to_record(user, book)
 
        else:
            print("No se ha encontrado NINGÚN RESULTADO")
        
    
    elif user == "2":
        user = input("Escriba el Titulo:  ")
        books = get_by_term ("title", user)
        if len(books):
            for book in books:
                pretty_book(book)
        else:
            print("No se ha encontrado NINGÚN RESULTADO")

    elif user == "3":
        user = input("Escriba el Autor:  ")
        books = get_by_term ("author", user)
        if len(books):
            for book in books:
                pretty_book(book)
        else:
            print("No se ha encontrado NINGÚN RESULTADO")
        
    elif user == "4":
        for i, genre in enumerate(genres):
            print(f"{i + 1}, {genre}")

        user = int(input("Género Nº: ")) -1
        user = genres[user]
        books = get_by_term ("genre", user)

        # write_to_record(user, f"{book["author"]} - {book["title"]}\n")
        
        if len(books):
            # write_to_record(user,[f"{book["author"]} - {book["title"]}\n") for book in books
            for book in books:
                pretty_book(book)
        else:
            print("No se ha encontrado NINGÚN RESULTADO")
        input()
    
    elif user == "5":
        user = input("Buscar libro a mofificar por ID: ")   
        book_to_update = search_id(user)
        if book_to_update:
            update_book(book_to_update)
        else:
            print("La informacion proporcionada no coincide con nuestra base de datos")
        print(DB)

    elif user == "6":
        user = input("Buscar libro a eliminar por ID: ")
        book_to_erase = search_id(user)
        if book_to_erase:
            DB.remove(book_to_erase)
        
        print(DB)

    elif user == "q":
        user = input("Desea guardar los datos (Y/N)? ")
        if user.lower() == "y":
            export_csv(DB,"books.csv")
                
            user = "q"

user = "0"