import requests as req
import csv
import json

# Direccion url de basa de datos en formato .csv ((NORMALEMENTE TRABAJAREMOS EN SOBRE FORMATOS .json))

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"

res = req.get(url).content # Se asigna una variable que devolverá/responderá(res) un contenido (Str) codificado en binario y no admite UTF8
res = res.decode("utf8", errors = "replace") # Se decodifica la Str para poder leerla y se reemplazan los caracteres especiales que no reconoce de UTF8 por ?

# with open("./data.csv", mode = "w", newline="", encoding= "utf8")as file:
#     json.dump
#     file.write(res)

with open("./data.csv", mode = "r", encoding= "utf8")as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    print(next(csv_reader))




# def to_json(dataset):

#     result={"muns":[]}
#     dict_keys = dataset[0]

#     for mun in dataset[1:]:
#         pre_dict = {}
#         for i, key in enumerate(dict_keys):
#             if i == 5 or i == 6 :

#                 pre_dict(key) = mun[i]
#         result["muns"].append(pre_dict)    
#     return result

# with open("muns.json", mode="w", enconding="utf")as file:
#     data_json = to_json(data)
#     print(len(data_json))
#     json.dump(data_json, file, indent=4)