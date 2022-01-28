import os
from funcs import *


user = ""

while user != "q":
    menu()
    user = input("\n" + " Haga su elección ahora: ")
    os.system("clear")
    if user == "1":
        city = input("Ciudad: ")  
        forecast_search = get_forecast(city)
        if forecast_search:
            print(f"La sensación térmica para {city.capitalize()}:")
            for predict in forecast_search:
                pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para la localización: {city.capitalize()}")
        input("...")
        os.system("clear")
    
    elif user == "2":
        lattlong = input("Coordenadas(latt, long): ")
        forecast_search = get_forecast(lattlong, coords = True)
        print(f"El tiempo para las coordenadas {lattlong}, es:")
        if forecast_search:
            for predict in forecast_search:
                    pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para las coordenadas: {lattlong}")
        input("...")
        os.system("clear")
        
    elif user == "3":
        lattlong = input("Coordenadas/ciudad: ")
        date = input("Fecha ( year/month/day): ")
        forecast_coords_date = get_forecast(lattlong, coords=True, date=date)
        if forecast_coords_date:
            print(f"La última predicción para {lattlong} en la fecha {date}, es:")
            predict=  forecast_coords_date[0]
            pretty_print(predict)
        else:
            print(f"No hay pronóstico disponible para las coordenadas({lattlong}) en fecha {date}")
        input("...")
        os.system("clear")


    elif user == "4":
        A = input("Desde: ")
        B = input("Hasta: ")
        trip_prediction = calculate_trip(A, B)

        if trip_prediction:
            if trip_prediction["is_bad_weather"] == True:
                print("\n"+"¡"*10 +"ATENCIÓN: Alerta de mal tiempo".center(60 - len("Alerta de mal tiempo"))+"!"*10)
            print(f"Temperatura en {A}: {round(trip_prediction['A_forecast']['st'],2)} grados")
            print(f"Temperatura en {B}: {round(trip_prediction['B_forecast']['st'],2)} grados")
            print(f"Distancia:{round(trip_prediction['distance'])} km")
            print(f"Tiempo estimado:{round(trip_prediction['time'])} horas")
            input("...")
        else:
            print("No tenemos rutas para estas ciudades")
        input("...")
        os.system("clear")

    elif user == "q":
        print("\n" +" Gracias por visitar BRILLIANT WEATHER!".center(100, "*")+ "\n")
        input("...")
    
    else:
        os.system("clear")
