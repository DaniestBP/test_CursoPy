import requests as req
import csv
import json
# from os import system

# Direccion url de basa de datos en formato .csv ((NORMALEMENTE TRABAJAREMOS EN SOBRE FORMATOS .json))

# url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"

# res = req.get(url).content # Se asigna una variable que devolverá/responderá(res) un contenido (Str) codificado en binario y no admite UTF8
# res = res.decode("utf8", errors = "replace") #NOS DEVUELVE UNA STRING Se decodifica la Str para poder leerla y se reemplazan los caracteres especiales que no reconoce de UTF8 por ?




def get_by_ine(dataset, ine_code):
    result = None
    for mun in dataset:
        if mun[2] == ine_code:
            result = mun
    return result

def get_largest(dataset):
    current_area = 0
    largest_mun = None
    for mun in dataset:
        if float(mun[-2]) > float(current_area):
            current_area = mun[-2]
            largest_mun = mun
    return largest_mun

def sup_total(dataset):
    area_counter = 0
    for mun in dataset:   
        area_counter += float(mun[-2])
    return round(area_counter)

def densidad_total(dataset):
    den_counter = 0
    for mun in dataset:
        den_counter += float(mun[-1])
    return round(den_counter)

def pob_total(dataset):
    result = []
    for mun in dataset:
        result.append(float(mun[-2])*float(mun[-1]))
    return round(sum(result))

def ley_bendford(dataset):
    densities = [mun[-1] for mun in dataset]
    result = {}
    for num in range(1,10):
        result[str(num)] = 0
    for density in densities:
        result[density[0]] += 1/len(densities)
    for k, v in result.items():
        print(f"{k}: {v}")
    

def menu():
    print("\n"*5 + " Bienvenido a la base de datos de los Municipios de la CAM ".center(150, "*")+ "\n")
    print("1. Buscar por INE del Municipio: " + (" " * (150 - len("1. Buscar por INE del Municipio: "))) + "#" + "\n")
    print("2. Cuál es el Municipio más grande de la CAM?"+ (" " * (150 - len("2. Cuál es el Municipio más grande de la CAM?"))) + "#" + "\n")
    print("3. Sepa cuál es la Superficie de la CAM"+ (" " *(150 - len("3. Sepa cuál es la Superficie de la CAM"))) + "#" + "\n")
    print("4. Sepa la densidad de población por km2 de la CAM"+ (" " *(150 - len("4. Sepa la densidad de población de la CAM"))) + "#" + "\n")
    print("5. Población total de la CAM"+ (" " *(150 - len("5. Población total de la CAM"))) + "#" + "\n")
    print("6. Sepa la población media por Municipio de la CAM"+ (" " *(150 - len("6. Sepa la población media por Municipio de la CAM"))) + "#" + "\n")
    print("7. Cómo aplica la Ley de Bendford en la CAM"+ (" " * (150 - len("7. Cómo aplica la Ley de Bendford en la CAM"))) + "#" + "\n")
    print("Q. Pulsa Q para salir" + (" " * (150 - len("Q. Pulsa Q para salir"))) + "#" + "\n")


with open("data.csv", mode = "r", encoding= "utf8")as file:
    data = list(csv.reader(file, delimiter=";"))[1:]



user = ""

while user != "q":
    menu()
    user = input(": ")
    if user == "1":
        
        ine_code_chosen = input("Introduzca el INE: "+ "\n"*2)
        mun_found = get_by_ine(data, ine_code_chosen)
        if mun_found:
            print("\n", f" Has escogido el Municipio {mun_found[1]} con un área de {mun_found[-2]} km2 y una densidad de {mun_found[-1]} personas/km2 ".center(100,"-"))   
        else:
            print("No se ha encontrado el Municipio")
        input("...")
        

    elif user == "2":
        largest_mun = get_largest(data)
        print("\n", f" El Municipio más grande es {largest_mun[1]}con un área de {largest_mun[-2]} km2 ".center(100,"-"))
 
    
    elif user == "3":
        total_area = sup_total(data)
        print("\n", f" La Superficie total de la CAM es {total_area} km2 ".center(100,"-"))
   
    elif user == "4":
        densidad_total_area= densidad_total(data)
        print("\n", f" En la CAM viven {densidad_total_area} personas por km2 ".center(100, "-"))
    
    elif user == "5":
        poblacion_total =  pob_total(data)
        print("\n", f" La población total de la CAM es {poblacion_total} ".center(100, "-"))
   
    elif user == "6":
        pob_media = pob_total(data) / len(data)
        print("\n", f" La población media de la CAM es de {round(pob_media)} personas por Municipio ".center(100, "-"))

    elif user == "7":
        ley_bendford(data)

    elif user == "q":
        print("\n" *2, " Gracias por visitarnos ".center(155, "*"))
        user = "q"
    
user = "0"
# system("cls")






# CONVERT .CSV TO .JSON >>>>


    
"""

with open("data.csv", mode = "r", encoding= "utf8")as file:
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



with open("data.json", mode = "w", encoding= "utf8")as file:
    data_to_json = to_json(data)
    json.dump(data_to_json, file, indent=4, ensure_ascii=False)

"""