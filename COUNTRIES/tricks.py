import requests as req
import json

url = "https://restcountries.com/v3.1/all"
all = req.get(url).json()

# countries_p = []

# for country in all:
#     try:
#         if country["name"]["common"].lower().startswith("p"):
#             countries_p.append(country)
#     except:
#         None
countries_p = list(filter(lambda country: country["name"]["common"].lower().startswith("p"),all))
# print(countries_p[0]["name"]["common"])
countries_p2 = list(map(lambda country: country if country["name"]["common"].lower().startswith("p") else None ,all))
# print(countries_p2)
countries_p3 = [country for country in countries_p if country]
# print(countries_p3[1]["name"]["common"])


# country = next(mylist)
# print(country)
# country = next(mylist)
# print(country)
'''
for country in countries_p:
    if country:
        # print(country["name"]["common"])
'''
''''''   
# highest_area = 0
# biggest_c = None

# for c in all:
#     if c["area"] >= highest_area:
#         highest_area = c["area"]
#         biggest_c = c["name"]["common"]
# print(biggest_c)

by_area = sorted(all, reverse = True, key= lambda country: country["area"])
# print(by_area[0]["name"]["common"])

students = [
    {"name": "Vito", "age": "22"},
    {"name": "Carlos", "age": "28"},
    {"name": "Jose", "age": "16"}
]

by_age = sorted(students, reverse=False, key=lambda student: student["age"])
# print((by_age[0]["name"], by_age[0]["age"]))



##############################################  GENERATORS #########################################


a = [1,2,3,4]

def squares(dataset):
    for num in dataset:
        yield num **2

'''# Funcion que genera iterando solo hasta cuando se necesita. /// yield en lugar de return // Las funciones generadoras son ITERABLES (se pueden generar) y son ITERATORS. 
# Y son funciones que trabajaran dentro de otras funciones  '''

b = squares(a)
# print(next(c_g))
# print(next(c_g))
# print(next(c_g))
# print(next(c_g))
# print(next(c_g))

''' Cuando no haya más valores sobre los que iterar dara un error deStopIterationError'''

c_g = (num ** 2 for num in a) # Si colocamos parentesis en lugar de corchetes la espresión se vuelve generadora
c_cl = [num ** 2 for num in a]
# print(next(c_g))
# print(c_cl)
# for num in c_g:
#     print(num)



