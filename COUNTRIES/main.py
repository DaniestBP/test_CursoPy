import requests as req
import os
import json
import random

CWD = os.path.dirname(__file__)

url = "https://restcountries.com/v3.1/all"

user = ""

def quiz(countries, region):
    countries_zip = []
    for country in countries:
        try:
            capital = country["capital"][0]
        except Exception as e:
            print(e)
        countries_zip.append({
            "name": country["name"]["common"], 
            "capital": capital, 
            "population": country["population"],
            "area": country["area"],
            "languages": country["languages"]
            })
    countries = countries_zip

    by_area = sorted(countries, key= lambda country: country["area"])
    half_by_area = int(len(by_area)/2)
    biggest, smallest = by_area[-1],by_area[0]
    
    any_country = random.choice(countries_zip)

    by_pop = sorted(countries, key = lambda country: country["population"])
    half_by_pop = int(len(by_pop)/2)
    most_pop, less_pop = by_pop[-1], by_pop[0]

    quiz = [
        {
            "q": f"Cuántos países hay en {region}?",
            "a": f"{len(countries)}",
            "o":[
                len(countries) + random.randint(2,16),
                len(countries),
                len(countries) + random.randint(2,16)
            ]
        },
        {
            "q": f"Cuál es el país más grande de {region}?",
            "a": f"{biggest['name']}",
            "o":[
                biggest["name"],
                by_area[random.randint(0,half_by_area)]['name'],   # PARA RANDOMIZAR LOS PÁISES QUE ENTREGAN COMO OPCIÓN DE RESPUESTA SE USA (RANDOM.RADINT) EN UN RANGO ENTRE 1 Y LA LONGITUD DE LA LISTA COUNTRIES
                by_area[random.randint(half_by_area,len(by_area)-2)]['name'],
                ] 
        },
        {
            "q": f"Cuál es el país más pequeño de {region}?",
            "a": f"{smallest['name']}",
            "o":[
                smallest["name"],
                by_area[random.randint(1,half_by_area)]['name'],
                by_area[random.randint(half_by_area,len(by_area)-1)]['name'],
                ] 
        },
        {
            "q": f"Cuál es la capital de {any_country['name']}?",
            "a": f"{any_country['capital']}",
            "o":[
                countries[random.randint(0,len(countries))]["capital"],
                any_country['capital'],
                countries[random.randint(0,len(countries))]['capital'],
                ] 
        },
        {
            "q": f"Cuáles son las lenguas de {any_country['name']}?",
            "a": f"{list(any_country['languages'].values())}",
            "o":[
                list(countries[random.randint(1,len(countries))]["languages"].values()),
                list(any_country['languages'].values()),
                list(countries[random.randint(1,len(countries))]['languages'].values()),
                ] 
        },
        {
            "q": f"Cuál es el país más poblado de {region}?",
            "a": f"{most_pop['name']}",
            "o":[
                by_pop[random.randint(0,half_by_pop)]["name"],
                most_pop['name'],
                by_pop[random.randint(half_by_pop,len(by_pop)-2)]["name"],
                ] 
        },
        {
            "q": f"Cuál es el país menos poblado de {region}?",
            "a": f"{less_pop['name']}",
            "o":[
                less_pop['name'],
                by_pop[random.randint(1,half_by_pop)]["name"],
                by_pop[random.randint(half_by_pop,len(by_pop)-1)]["name"],
                ] 
        }
        
    ]  
    random.shuffle(quiz)
    return quiz




while user != "q":
    print("\n"+" Bienvenido a tu base de datos de PAISES DEL MUDO preferida ".center(150,"*"))
    print("\n1. Buscar país")
    print("2. Descarga tu bandera")
    print("3. Juega con nosotros")
    print("Q. Salir")
    user = input("\n"": ")
    if user == "1":
        country_name = input("\nPaís: ")
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
        country_name = input("\nPaís: ")
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        res = req.get(url)
        if res.status_code == 200:
            country = res.json()[0]
            flag_url= country["flags"]["svg"]
            flag = req.get(flag_url)
            if flag.status_code == 200:
                with open(f"{CWD}/img/{flag_url[-6:]}", "wb")as file:   #"wb"= escribir binario
                    file.write(flag.content)
            else:
                print("\nNo hemos encontrado tu bandera. Inténtado otra vez"+"\n")
                
    elif user == "3":
        continent_name = input("\nContinente: ")
        url = f"https://restcountries.com/v3.1/region/{continent_name}"
        res = req.get(url)
        if res.status_code == 200:
            countries = res.json()
            game = quiz(countries, continent_name)
            user_answer = []
            note = 0
            for q in game:
                print("\n"+q["q"])
                random.shuffle(q["o"])
                for i, option in enumerate (q["o"]):
                    print(f"{i+1}: {option}")
                answer = q["o"][int(input(": "))-1]
                q["user"] = answer
                user_answer.append({q["q"]:answer})
                if q["a"] == q["user"]:
                    note += 1
            print("\n" + str(game))
            print("\n" + str(user_answer))
            print("\n"+f" ¡ Tu NOTA es: {note} !".center(100))



    
    