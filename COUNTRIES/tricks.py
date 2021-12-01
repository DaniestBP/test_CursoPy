import requests as req
import json

url = "https://restcountries.com/v3.1/all"
all = req.get(url).json()

countries_p = []

# for country in all:
#     try:
#         if country["name"]["common"].lower().startswith("p"):
#             countries_p.append(country)
#     except:
#         None
countries_p = list(filter(lambda country: country["name"]["common"].lower().startswith("p"),all))

countries_p = list(map(lambda country: country if country["name"]["common"].lower().startswith("p") else None ,all))
# print(countries_p[0])
countries_p = [country for country in countries_p if country]
# print(countries_p[1]["name"]["common"])
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

by_age = sorted(students, reverse=True, key=lambda student: student["age"])
print((by_age[0]["name"], by_age[0]["age"]))