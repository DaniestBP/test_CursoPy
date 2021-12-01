import requests as req
import os
import json
import random

CWD = os.path.dirname(__file__)

user = ""

while user != "q":
    print("1. Buscar país")
    print("2. Descarga tu bandera")
    print("3. Juega con nosotros")
    print("Q. Salir")
    user = input(": ")
    if user == "1":
        country_name = input("País: ")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        res = req.get(url)
        if res.status_code == 200:
            res = res.json()[0]
            country_lang = list(res["languages"].values())[0]
            print(f'Capital: {res["capital"][0]}')
            print(f'Población: {res["population"]}')
            print(f'Superficie: {res["area"]}')
            print(f'Lenguaje: {country_lang}')
            input("...")
        else:
            print("Something went wrong")
    
    elif user == "2":
        country_name = input("País: ")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        res = req.get(url)
        if res.status_code == 200:
            country = res.json()[0]
            flag_url= country["flags"]["svg"]
            flag = req.get(flag_url)
            if flag.status_code == 200:
                with open(f"{CWD}/img/test.svg", "wb")as file:
                    file.write(flag.content)

    elif user == "3":
        continent_name = input("Continente: ")
        url = f"https://restcountries.com/v3.1/region/{continent_name}"
        res = req.get(url)
        if res.status_code == 200:
            countries = res.json()
            random_country = random.choice(countries)
            print(random_country["name"]["common"])
            for random_country in countries:
                pass
                # quizz = [
                #      "Cuál es la capital de {random_country}?",
                #      "Cuál es el idioma de {random_country}?",
                #      "Qué población tiene {random_country}?"
                # ]
                # print(quizz)
    