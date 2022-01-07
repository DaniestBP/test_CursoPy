import random

import requests as req

res = req.get("https://restcountries.com/v3.1/region/europe").json()

countries = list(map(lambda country: {"name": country["name"]["common"], 
    "capital": country["capital"][0], 
    "population": country["population"],
    "area": country["area"]}, 
    res))


country = input("Escoja un pais de europa: ").lower()

def quizz():
    for c in countries:
            name = c["name"]
            if name.lower() == country:
                qa = [
                    {
                        "q": f"Cuál es la capital de {country}?",
                        "a": f"{c['capital']}"
                    },
                    {
                        "q": f"Cuál es el tamaño de {country}?",
                        "a": f"{c['area']}"
                    }
                ]  
                quizz = random.choice(qa)
                print(quizz)
                print(quizz["q"])
                answer = input("Respuesta(5 pts): ")
                a = quizz["a"]
                score = 0
                if answer == a:
                    score += 5
                else:
                    print("Lo siento, has fallado")
                score = print(f"Tu puntuación es: {score} pts")    
                    
                return score
                
    
print(quizz())
print(quizz())
print(quizz())