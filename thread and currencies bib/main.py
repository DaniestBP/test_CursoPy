import time 
import threading
import requests as req
from requests.api import get


print("Empieza el programa")


# def get_data(data):
#     time.sleep(1)
#     return f"Se ha descargado la data de {data}"+

# thread_1 = threading.Thread(target=get_data, args=["REST countries 1"])
# thread_2 = threading.Thread(target=get_data, args=["REST countries 2"])
# thread_3 = threading.Thread(target=get_data, args=["REST countries 3"])
# thread_4 = threading.Thread(target=get_data, args=["REST countries 4"])

# thread_1.start()
# thread_2.start()
# thread_3.start()
# thread_4.start()
# thread_1.join()
# thread_2.join()
# thread_3.join()
# thread_4.join()

url_1 = "https://flagcdn.com/w320/ng.png"
url_2 = "https://flagcdn.com/w320/uy.png"

url_all = "https://restcountries.com/v3.1/all"

res = req.get(url_all).json()
flags_all = [country["flags"]["svg"] for country in res]

start = time.perf_counter()

def get_flag(url):
    res = req.get(url).content
    with open(f"flags/{url[-6:]}", "wb")as file:
        file.write(res)

for url in flags_all:
    t = threading.Thread(target = get_flag, args=[url])
    t.start()
# get_flag(url_2)

# t_1 = threading.Thread(target = get_flag, args = [url_1])
# t_2 = threading.Thread(target = get_flag, args = [url_2])

# t_1.start()
# t_2.start()
# t_1.join()
# t_2.join()

print("Ha finalizado el programa")
finish = time.perf_counter()
print(finish - start)