import requests as req
import json

# location = input("Ciudad: ")

# woeid = res[0]["woeid"]
# res = req.get(f"https://www.metaweather.com/api/location/{woeid}").json()

def menu():
    print("\n" + " BRILLIANT WEATHER".center(185, "*")+ "\n")
    print(" >  Por favor elija el lugar donde desea consultar el tiempo  <".center(150)+ "\n")
    print(" 1. Buscar por ciudad: " + (" "*(180 - len("2. Buscar por coordenadas: "))) + "#")
    print(" 2. Buscar por coordenadas: " + (" "*(175 - len("2. Buscar por coordenadas: "))) + "#")
    print(" 3. ciudad/coordenadas en fecha: " + (" "*(165 -len("3. ciudad/coordenadas en fecha: "))) + "#"+ "\n")
    print(" Para salir (Q): " + (" " * (180 - len("Para salir (Q): ")) + "#")+ "\n")



def forecast(location, coordinates=False, date=False):

    if coordinates:
        woeid = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={location}").json()[0]["woeid"]
        forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
    else:
        woeid = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["woeid"]
        forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
    forecast = {
        "desc": forecast["weather_state_name"],
        "max-temp": forecast["max_temp"],
        "min_temp": forecast["min_temp"],
        "st": forecast["the_temp"],
        "humidity": forecast["humidity"],
        "wind_speed": forecast["wind_speed"],
        "wind_direction": forecast["wind_direction"]
    }
    return forecast



def pretty_print(forecast):
    for k, v in forecast.items():
        print(f"{k.upper()}: {v}")


user = ""

while user != "q":
    menu()
    user = input("\n" +" Haga su elección ahora: ")
    if user == "1":
        city = input("Ciudad: ")
        forecast_search = forecast(city)
        print(f"La sensación térmica para {city}:")
        pretty_print(forecast_search)
        input("...")
    elif user =="2":
        lattlong = input("Coordenadas: ")
        forecast_search = forecast(lattlong, coordinates = True)
        print(f"El tiempo para las coordenadas {lattlong}, es:")
        pretty_print(forecast_search)
        input("...")

        






