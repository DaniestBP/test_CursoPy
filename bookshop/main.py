from bookshop import *



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
        user = input("Escriba el ID: ").lower()
        books = get_by_term ("id", user)
        if len(books):
            for book in books:
                pretty_book(book)
                write_to_record(user, book)
 
        else:
            print("\n"+" No se ha encontrado NINGÚN RESULTADO ".center(190,"*")+"\n")
        input()
    
    elif user == "2":
        user = input("Escriba el Titulo:  ")
        books = get_by_term ("title", user)
        if len(books):
            for book in books:
                pretty_book(book)
                write_to_record(user, book)
        else:
            print("\n"+" No se ha encontrado NINGÚN RESULTADO ".center(190,"*")+"\n")
       
    elif user == "3":
        user = input("Escriba el Autor:  ")
        books = get_by_term ("author", user)
        if len(books):
            for book in books:
                pretty_book(book)
                write_to_record(user, book)
        else:
            print("\n"+" No se ha encontrado NINGÚN RESULTADO ".center(190,"*")+"\n")
        
    elif user == "4":
        for i, genre in enumerate(genres):
            print(f"{i + 1}. {genre}")
        user = int(input("Género Nº: ")) -1
        user = genres[user]
        books = get_by_term ("genre", user)

        if len(books):
            write_to_record(user, [f'Se ha buscado {book["genre"]}: {book["author"]} - {book["title"]}\n' for book in books]) 

        for i, book in enumerate(books):
            pretty_book(book)
            print("-"*50)
            if i % 2 == 0:
                input("Siguiente: ")
                   
        input()
                

    
    elif user == "5":
        user = input("Buscar libro a mofificar por ID: ")   
        book_to_update = search_id(user)
        if book_to_update:
            update_book(book_to_update)
            write_to_record(user, book_to_update)
            print(f"El libro {book_to_update['title']} se ha mofificado".center(175, "*")+ "\n")
        else:
            print("La informacion proporcionada no coincide con nuestra base de datos".center(190,"*")+"\n")
        print(DB)

    elif user == "6":
        user = input("Buscar libro a eliminar por ID: ")
        book_to_erase = search_id(user)
        if book_to_erase:
            DB.remove(book_to_erase)
            print(f"El libro {book_to_erase['title']} se ha eliminado".center(175, "*"))
            write_to_record(user, book_to_erase)
        else:
            print("\n"+" No se ha encontrado NINGÚN RESULTADO ".center(190,"*")+"\n")
        print(DB)
        

    elif user == "q":
        user = input("Desea guardar los datos (Y/N)? ")
        if user.lower() == "y":
            export_csv(DB,"books.csv")
        print(" Thanks! Good bye! ".center(175, "-"))
        user = "q"        
user = "0"
            
        
            