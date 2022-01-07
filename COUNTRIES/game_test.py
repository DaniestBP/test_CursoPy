import random

# country= None
# country = {"name":"Spain", "capital": "Madrid"}

# qa = [
#     {
#         "q": "Cuál es la capital de {country}?",
#         "a": f"{country['capital']}"
#     }
# ]

# qa = {
#     "country_1": {
#         "q": "Como?",
#         "a": "Asi",
#     },
#     "country_2": {
#         "q": "Cuanto?",
#         "a": "mucho",
#     }
# }
# print(qa.values())

# for country in qa.values():
#     print (country["q"])

countries= [{"name":"spain", "capital": "madrid", "area": 50}, {"name":"italy", "capital": "roma", "area": 40}, {"name":"portugal", "capital": "lisboa", "area": 20}]
# print(countries[0]['name'])
any_country = random.choice(countries)
any_name = any_country["name"]
print(any_name)
# def quizz(country):
    
#     for c in countries:
#         if c["name"] == country:
#             qa = [
#                 {
#                     "q": f"Cuál es la capital de {c['name']}?",
#                     "a": f"{c['capital']}"
#                 },
#                 {
#                     "q": f"Cuál es el tamaño de {c['name']}?",
#                     "a": f"{c['area']}"
#                 }
#             ]  
#             quizz = random.choice(qa)
#             return quizz["q"]

# print(quizz("italy"))

# qa = [
#                 {
#                     "q": "Cuál es la capital de {c['name']}?",
#                     "a": "{c['capital']}"
#                 },
#                 {
#                     "q": "Cuál es el tamaño de {c['name']}?",
#                     "a": "{c['area']}"
#                 }
#             ]  
    
# q = random.choice(qa)
# print(q["a"])