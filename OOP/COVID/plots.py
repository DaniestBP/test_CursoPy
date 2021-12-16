from main import analyze_cct, y_lineal
import matplotlib as Plt
from SSRace import std_y_tia_20211214, std_y_tia_20201215

Plt.plot(analyze_cct.x, analyze_cct.y, analyze_cct.x, y_lineal)
Plt.ylabel("Casos confirmados")
Plt.xlabel("Prediccion")
Plt.show()

