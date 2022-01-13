from flask import Flask, request
import json

app = Flask(__name__)

def get_all(json_file):
    with open(json_file, encoding="utf8")as file:
        return json.load(file)

books = get_all("bookshop.json")

def write_data(data):
    with open ("bookshop.json", "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_by_id(book_id):
    return next(filter(lambda book: book["id"] == book_id, books["data"]),False)

def delete_by_id(book_id):
    book_to_delete = get_by_id(book_id)
    if book_to_delete:
        books["data"].remove(book_to_delete)
        write_data(books)
        return True
    else:
        return False
        
@app.route("/test", methods=["GET", "POST"])
def test():
    print(request.method)
    if request.method == "GET":
        return f"El método utilizado es {request.method}"
    else:
        return f"El método utilizado es {request.method}"

@app.route("/all")
def all():
    return get_all("bookshop.json")

@app.route("/book/<book_id>", methods = ["GET", "DELETE"])
def book_by_id(book_id):
    if request.method == "GET":
        result = {}
        book_found = get_by_id(book_id)
        if book_found:
            result["success"] = True
            result["book"] = book_found
        else:
            result["success"] = False
        return result
    elif request.method == "DELETE":
        if delete_by_id(book_id):
            return {"success" : True}
        else:
            return {"success" : False}
            

@app.route("/delete_book/<book_id>")
def delete(book_id):
    if delete_by_id(book_id):
        return {"success":True}
    else:
        return  {"success":False}


if __name__ == "__main__":
    app.run(debug=True) # dentro de run podemos hacer que se ejecute el server con 'debug' y asignarle un puerto en concreto con : port=3000  p.e app.run(debug=,ports= 3000)