import requests as req
import json

# location = input("Ciudad: ")

# woeid = res[0]["woeid"]
# res = req.get(f"https://www.metaweather.com/api/location/{woeid}").json()



def menu():
    print("BRILLIANT WEATHER".center(85, "*"))
    print("Por favor elija el lugar donde desea consultar el tiempo".center(60))
    print("1. Buscar por ciudad:".center(85, "*")))
    print("2. Buscar por coordenadas: " + (" "*80 - len("2. Buscar por coordenadas: ")) + "#")
    print("3. ciudad/coordenadas en fecha: " + (" "*85 -len("3. ciudad/coordenadas en fecha: ")) + "#")
    print("Para salir (Q): " + (" " * (80 - len("Para salir (Q): ")) + "#"))

def forecast(location):
    woeid = res = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["weoid"]
    forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/"),json()["consolidated_weather"][0]
    


user = 0

while user != "q":
    menu()
    user = input("Haga su elección ahora: ")
    if user == "1":
        location = input(user)
        # res = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()
        # for entry in res[1:]:






