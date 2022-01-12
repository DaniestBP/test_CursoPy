from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Soy un mensaje")
    return "Estás en la página principal"

@app.route("/about")
def about():
    return "Te encuentras en la página ABOUT"
    

if __name__ == "__main__":
    app.run(debug=True) # dentro de run podemos asignarle un puerto en concreto con : port=3000  p.e