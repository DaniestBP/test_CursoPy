import requests as req
import json
import matplotlib.pyplot as plt
from std import Std
import datetime as dt

url = "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/907a2df0-2334-4ca7-aed6-0fa199c893ad/download/covid19_tia_zonas_basicas_salud_s.json"
data = req.get(url).json()["data"]


# with open("./covid.json", "w", encoding = "utf8") as file:
#     json.dump(data, file ,ensure_ascii=False, indent=4)

def get_data(json_file):
    with open(json_file, encoding="utf8 ") as file:
        return json.load(file)
      
data = get_data("./covid.json")

def data_by_date(dataset):
    result = {}
    for area in dataset:
        idate = area["fecha_informe"].split(" ")[0]
        if result.get(idate):
            result[idate].append(area)
        else:                             # por que hace el if and else en lugar de poner debajo del for: result.append(idate)
            result[idate] = [area]
    return result

data_by_date = data_by_date(data)

def get_y(dataset):
    result = []
    for area_list in dataset.values():
        result.append(sum(zone["casos_confirmados_totales"]for zone in area_list))
    return result

y = get_y(data_by_date)
y.reverse()
x = [num for num in range(0, len(y))]

analyze_cct = Std(x,y)  #Analizamos los casos confirmados totales(acumulados)

# def get_y_line(std_object):
#     B = std_object.B
#     result = [B]
#     for _ in range(1, len(std_object.y)):
#         result.apgiopend(B + result[-1])

# o

# def get_y_line_v2(std_object):
#     result = []
#     for week in std_object.x:
#         result.append(std_object.y_prediction(week))
#     return result

def predic_last_Dec(std_object):
    #como sabemos que es 07/dec sabemos que hasta el 31/dec son 24 dias
    last_of_dec = 17/7
    predict_last_dec = std_object.n + last_of_dec
    prediction = std_object.y_prediction(predict_last_dec)
    return prediction
   
    # return [std_object.y_prediction(week + 3 + 42.9 * 7 /100) for week in std_object.x]

def predict_by_date(std_object,date):
        new_date = date.replace("/", "-")
        dt_new_date = dt.datetime.fromisoformat(new_date)
        date_origin = dt.datetime.fromisoformat("2021-12-14")
        to_predic = dt_new_date - date_origin
        to_predic = to_predic.days/7
        new_to_predict = std_object.n + to_predic
        prediction = std_object.y_prediction(new_to_predict)
    
        return prediction

y_lineal = analyze_cct.lineals


# plt.plot(analyze_cct.x, analyze_cct.y, analyze_cct.x, y_lineal)
# plt.ylabel("Casos confirmados")
# plt.xlabel("Prediccion")
# plt.show()

# print(predic_last_Dec(analyze_cct))
# print(predict_by_date(analyze_cct,"2022/01/07"))
