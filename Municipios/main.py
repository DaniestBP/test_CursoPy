import requests as req
import csv
import json
from funcs import *
from os import system

# Direccion url de basa de datos en formato .csv ((NORMALEMENTE TRABAJAREMOS EN SOBRE FORMATOS .json))

# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"

# res = req.get(url).content # Se asigna una variable que devolverá/responderá(res) un contenido (Str) codificado en binario y no admite UTF8
# res = res.decode("utf8", errors = "replace") #NOS DEVUELVE UNA STRING Se decodifica la Str para poder leerla y se reemplazan los caracteres especiales que no reconoce de UTF8 por ?


with open("data.csv", mode = "r", encoding= "utf8")as file:
    data = list(csv.reader(file, delimiter=";"))[1:]



user = ""

while user != "q":
    menu()
    user = input(": ")
    if user == "1":
        
        ine_code_chosen = input("\nIntroduzca el INE: "+ "\n"*2)
        mun_found = get_by_ine(data, ine_code_chosen)
        if mun_found:
            print("\n", f" Has escogido el Municipio {mun_found[1]} con un área de {mun_found[-2]} km2 y una densidad de {mun_found[-1]} personas/km2 ".center(100,"-"))   
        else:
            print("No se ha encontrado el Municipio")
        input("...")
        system("clear")

    elif user == "2":
        largest_mun = get_largest(data)
        print("\n", f" El Municipio más grande es {largest_mun[1]}con un área de {largest_mun[-2]} km2 ".center(100,"-"))
        input("...")
        system("clear")
    
    elif user == "3":
        total_area = sup_total(data)
        print("\n", f" La Superficie total de la CAM es {total_area} km2 ".center(100,"-"))
        input("...")
        system("clear")

    elif user == "4":
        densidad_total_area= densidad_total(data)
        print("\n", f" En la CAM viven {densidad_total_area} personas por km2 ".center(100, "-"))
        input("...")
        system("clear")

    elif user == "5":
        poblacion_total =  pob_total(data)
        print("\n", f" La población total de la CAM es {poblacion_total} ".center(100, "-"))
        input("...")
        system("clear")

    elif user == "6":
        pob_media = pob_total(data) / len(data)
        print("\n", f" La población media de la CAM es de {round(pob_media)} personas por Municipio ".center(100, "-"))
        input("...")
        system("clear")

    elif user == "7":
        ley_bendford(data)
        input("...")
        system("clear")

    elif user == "q":
        print("\n" *2, " Gracias por visitarnos ".center(155, "*"))
        input("...")
        system("clear")
        
    else:
        print("\n", " Por favor escoja una de las opciones disponibles ".center(100, "/"))
user = "0"
system("clear")






# CONVERT .CSV TO .JSON >>>>


    
"""

with open("./data.csv", mode = "r", encoding= "utf8")as file:
    data = list(csv.reader(file, delimiter=";"))


def to_json(dataset):
    result = {"muns":[]}
    dict_keys = dataset[0]
    for mun in dataset[1:]:
        pre_dict= {}
        for i, k in enumerate(dict_keys):
            if i == 5 or i == 6:  # convertimos los indices 5 y 6 (Superficie y densidad) a float porque los teníamos en una String originalmente.
                pre_dict[k] = float(mun[i])
            else:
                pre_dict[k] = mun[i]
                
        result["muns"].append(pre_dict)
    return result



with open("./data.json", mode = "w", encoding= "utf8")as file:
    data_to_json = to_json(data)
    json.dump(data_to_json, file, indent=4, ensure_ascii=False)

"""