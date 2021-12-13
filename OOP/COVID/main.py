import requests as req
import json
import matplotlib.pyplot as plt
from std import Std


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
x = [num for num in range(1, len(y) + 1)]

analyze = Std(x,y)

# def get_y_line(std_object):
#     B = std_object.B
#     result = [B]
#     for _ in range(1, len(std_object.y)):
#         result.append(B + result[-1])

# o

# def get_y_line_v2(std_object):
#     result = []
#     for week in std_object.x:
#         result.append(std_object.y_prediction(week))
#     return result
    # return [std_object.y_prediction(week + 3) for week in std_object.x]

y_lineal = analyze.lineals


plt.plot(analyze.x, analyze.y, analyze.x, y_lineal)
plt.ylabel("Casos confirmados")
plt.xlabel("Prediccion")
plt.show()

# print(get_y_line_v2(analyze))