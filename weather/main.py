#!/usr/bin/env python3
# code: utf-8
# Había un problema de encoding segun la documentación es posible solucionarlo así

# import requests as req
# import json
from funcs import *


# location = input("Ciudad: ")

# woeid = res[0]["woeid"]
# res = req.get(f"https://www.metaweather.com/api/location/{woeid}").json()

user = ""

while user != "q":
    menu()
    user = input("\n" + " Haga su elección ahora: ")
    if user == "1":
        city = input("Ciudad: ")
        # sin forecast_v2 implenentada
        forecast_search = get_forecast(city)
        if forecast_search:
            print(f"La sensación térmica para {city}:")
            # si devolvemos mas de una predicción (linea 74 de funcs.py) si no es asi debemos prescindir del for
            for predict in forecast_search:
                pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para la localización: {city}")
        input("...")

    elif user == "2":
        lattlong = input("Coordenadas(latt, long): ")
        # sin forecast_v2 implenentada
        forecast_search = get_forecast(lattlong, coords = True)
        print(f"El tiempo para las coordenadas {lattlong}, es:")
        if forecast_search:
            for predict in forecast_search:
                    pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para las coordenadas: {lattlong}")
        input("...")
        
        
    elif user == "3":
        # Habria que hacerlo para busqueda por ciudad o coordenadas
        lattlong = input("Coordenadas: ")
        date = input("Fecha ( year/month/day): ")
        # Para city sin coords=
        # date en la funcion get_forecast no es boolean es el valor suministrado por el input
        forecast_coords_date = get_forecast(lattlong, coords=True, date=date)
        if forecast_coords_date:
            print(f"El tiempo para las coordenadas {lattlong} en la fecha {date}, es:")
            for predict in forecast_coords_date:
                    pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para las coordenadas({lattlong}) en fecha {date}")
        input("...")

    elif user == "4":
        # La funcion calculate_trip tiene buena pinta, no la he podido revisar
        A = input("Desde: ")
        B = input("Hasta: ")
        trip_prediction = calculate_trip(A, B)
        if trip_prediction:
            if trip_prediction["is_bad_weather"]:
                print("Alerta de mal tiempo")
        print(f"Temperatura en {A}: {round(trip_prediction['A_forecast']['the_temp'],2)} grados")
        print(f"Temperatura en {B}: {round(trip_prediction['B_forecast']['the_temp'],2)} grados")

        print(f"Distancia:{round(trip_prediction['distance'])} km")
        print(f"Tiempo estimado:{round(trip_prediction['time'])} horas")

        input("...")
