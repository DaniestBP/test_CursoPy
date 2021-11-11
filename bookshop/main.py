# from bookshop import DB, menu, pretty_book, get_by_term, update_book, search_id, genres
# from bookshop import *
fichero = open("./lectura/test.txt")
lectura = fichero.read()


# Análisis del fichero:

mama = lectura[(lectura.find("mama")):]
print(mama)









fichero.close()
    
    
# user = "0"

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

#     elif user == "3":
#         user = input("Escriba el Autor:  ")
#         books = get_by_term ("author", user)
#         if len(books):
#             for book in books:
#                 pretty_book(book)
#         else:
#             print("No se ha encontrado NINGÚN RESULTADO")
        
#     elif user == "4":
#         for i, genre in enumerate(genres):
#             print(f"{i + 1}, {genre}")

#         user = int(input("Género Nº: ")) -1
#         user = genres[user]

#         books = get_by_term ("genre", user)
#         if len(books):
#             for book in books:
#                 pretty_book(book)
#         else:
#             print("No se ha encontrado NINGÚN RESULTADO")
#         input()
    
#     elif user == "5":
#         user = input("Buscar libro a mofificar por ID: ")   
#         book_to_update = search_id(user)
#         if book_to_update:
#             update_book(book_to_update)
#         else:
#             print("La informacion proporcionada no coincide con nuestra base de datos")
#         print(DB)

#     elif user == "6":
#         user = input("Buscar libro a eliminar por ID: ")
#         book_to_erase = search_id(user)
#         if book_to_erase:
#             DB.remove(book_to_erase)
        
#         print(DB)

    