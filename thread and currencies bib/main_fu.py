import concurrent.futures
import requests as req
import time
url_1 = "https://flagcdn.com/w320/ng.png"
url = "https://restcountries.com/v3.1/all"

def get_flag(url):
    res = req.get(url).content
    with open(f"flags/{url[-6:]}", "wb")as file:
        file.write(res)

res =  req.get(url).json()
flags_all = [country["flags"]["svg"] for country in res]

start = time.perf_counter()

# ThreadPoolExecutor permite guardar los valores en variables. MAP permite almacenar muchos hilos(urls) y submit un solo hilo (una url)
# y al momento de ejecutar el submit/map arrancamos el proceso. A diferencia del Threading.thread donde ne necesita ejecutar cada url usando, a parte, el .start()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_flag, flags_all)
    future_1 = executor.submit(get_flag, url_1)
    # data = future_1.result()
    # print(data)

finish = time.perf_counter()
print(finish - start)

