import requests as req
import json
from funcs import *

# location = input("Ciudad: ")

# woeid = res[0]["woeid"]
# res = req.get(f"https://www.metaweather.com/api/location/{woeid}").json()

user = ""

while user != "q":
    menu()
    user = input("\n" +" Haga su elección ahora: ")
    if user == "1":
        city = input("Ciudad: ")
        forecast_search = forecast_v2(city)
        if forecast_search:
            print(f"La sensación térmica para {city}:")
            pretty_print(forecast_search)
        else:
            print("No hay pronóstico disponible para la localización: {city}")
        input("...")

    elif user =="2":
        lattlong = input("Coordenadas: ")
        forecast_search = forecast_v2(lattlong, coordinates = True)
        print(f"El tiempo para las coordenadas {lattlong}, es:")
        pretty_print(forecast_search)
        input("...")
    
    # elif user == "3":
    #     lattlong = input("Coordenadas: ")
    #     date = input("Fecha: ")
    #     forecast_coords_date = forecast_v2(lattlong, date=True)
    #     if forecast_coords_date:
    #         print(f"El tiempo para las coordenadas {lattlong} en la fecha {date}, es:")
    #         pretty_print(forecast_coords_date)
    #     else:
    #         print("No hay pronóstico disponible")

    #     input("...")

    elif user == "4":
        A = input("Desde: ")
        B = input("Hasta: ")
        trip_prediction = calculate_trip(A, B)
        if trip_prediction:
            if trip_prediction["is_bad_weather"]:
                print("Alerta de mal tiempo")
        print(f"Temperatura en {A}: {round(trip_prediction['A_forecast']['the_temp'],2)}")
        print(f"Temperatura en {B}: {round(trip_prediction['B_forecast']['the_temp'],2)}")

        print(f"Distancia:{round(trip_prediction['distance'])}")
        print(f"Tiempo estimado:{round(trip_prediction['time'])}")

        input("...")

