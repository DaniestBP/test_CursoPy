import requests as req
import csv
import json

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
    
'''

with open("data.csv", mode = "r", encoding= "utf8")as file:
    data = list(csv.reader(file, delimiter=";"))[1:] 
    # next(data)
    # for element in data:
    #     data.append(element) 
    # print(data[1])
    
# ********Ejercicio 1.>> BUSCAR POR CODIGO INE:******   

    ine_code_chosen = input("Introduzca el INE a buscar: ")
    mun_found = get_by_ine(data, ine_code_chosen)
    if mun_found:
        print(f"Los datos para el Municipio escogido son {mun_found[1]} con un area de {mun_found[-2]} km2 y una densidad de {mun_found[-1]} personas/km2")   
    else:
        print("No se ha encontrado el Municipio")

# ********Ejercicio 2.>> LOCALIZAR EL MUNICIPIO MAS GRANDE****** 

    largest_mun = get_largest(data)
    print(f"El Municipio mas grande es {largest_mun[1]}con un area de {largest_mun[-2]} km2")

# ********Ejercicio 3.>> ****** 

    total_area = sup_total(data)
    print(f"La Superficie total de la CAM es {total_area} km2")

# ********Ejercicio 4.
    densidad_total_area= densidad_total(data)
    print(f"En la CAM viven {densidad_total_area} personas por km2")

# ********Ejercicio 5.
    poblacion_total =  pob_total(data)
    print(f"La poblacion total de la CAM es {poblacion_total}")

# ********Ejercicio 6.
    pob_media = poblacion_total / len(data)
    print(f"La población media de la CAM es de {round(pob_media)} personas por Municipio")


# ********Ejercicio 7.
    ley_bendford(data)
    
'''

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
    