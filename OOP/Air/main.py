import datetime as dt
dt.datetime.utcnow
time_now =dt.datetime.utcnow()
def menu():
    print("1. Comprar vuelo")
    print("2. Modificar vuelo")
    print("3. Cancelar vuelo")
    print("Q. Salir")


dt.date.fromisoformat("2021-12-23")
time1=dt.datetime(2021,12,24, hour=19,minute=26,second=6)
time2=dt.datetime(2021,12,20, hour=10,minute=12,second=3)
newt = time1 - time2 
# print(type(newt))
result = time1 - time_now
# print(result)
print(type(result))
print(type(time_now))
eta_1 = time_now + result
print(eta_1)
print(type(eta_1))