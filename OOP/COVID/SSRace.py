from main import*
from std import Std
import json

# Definimos funcion para otorgar a "y" los valores de "tasa_incidencia_acumulada_ultimos_14dias" en el dia 2021/12/14

# **************OBTENCION DE LOS DOS ELEMENTOS ESTADISTICOS *****

# def get_tia(dataset, date):
#     return tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"]for zone in dataset if zone["fecha_informe"].split(" ")[0] == date])

# std_y_tia_20211215 = get_tia(data, "2021/12/14")
# print(std_y_tia_20211215)
list_y_tia_20211214 = tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"]for zone in data_by_date["2021/12/14"])
list_y_tia_20201215 = tuple(zone["tasa_incidencia_acumulada_ultimos_14dias"]for zone in data_by_date["2020/12/15"])
list_x_tia = tuple(num for num in range(0, len(list_y_tia_20201215)))

std_y_tia_20211214 = Std(list_x_tia, list_y_tia_20211214) # OBJETO ESTADISTICO 1
std_y_tia_20201215 = Std(list_x_tia, list_y_tia_20201215) # OBJETO ESTADISTICO 2
# print(std_y_tia_20211214.avg_y) 
# print(std_y_tia_20201215.avg_y)

# DEFINIMOS LA ESTADISTICA DE CONTRASTE PARA NUESTROS DATOS

def ec_student(Obj1, Obj2):
    nu = Obj1.avg_y - Obj2.avg_y
    de = ((((Obj1.n -1)* Obj1.y_varianza_or_quasi(True) + (Obj2.n - 1)* Obj2.y_varianza_or_quasi(True)) / (Obj1.n + Obj2.n - 2 )) * (1/Obj1.n + 1/Obj2.n)) ** 0.5
    return nu/de

print(ec_student(std_y_tia_20211214, std_y_tia_20201215))  # = 5.4027 lo que si vamos a la tabla de "distribucion t student" vemos que el valor esta entre 0.05(95%) y 0.01(99%) lo que dice que la diferencia entre un obj (año2021) y el otro (2020) es notablemente grande. 



# CONCLUSION : La San Silvestre no deberia correrse como no se corrio el año pasado

# print(std_y_tia_20211214.y_varianza_or_quasi(True))
# print(std_y_tia_20201215.y_varianza_or_quasi(True))