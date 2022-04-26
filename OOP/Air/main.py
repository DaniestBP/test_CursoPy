import datetime as dt
dt.datetime.utcnow
from models import Flights, flights, tickets
import json
import os 

def menu():
    print("\n"+" BIENVENIDO A DANIEL AIRLINES ".center(150-len("BIENVENIDO A DANIEL AIRLINES"),"-"))
    print("\n1. Comprar vuelo")
    print("2. Modificar vuelo")
    print("3. Cancelar vuelo")
    print("Q. Salir")


def airports_list():
    for i, city in enumerate(flights):
        print( f"{i+1}: {city}")

def departures_list():
    for i, time in enumerate(destination["departures"]):
        print(f"{i+1}: {time}")

user = ""

while user != "q":
    os.system('clear')
    menu()
    user = input("\n>>>  ")

    if user == "1":
        print(f"\nCountries available:"+"\n")
        airports_list()
        ori_sel = input("\n>>> From (acronyms): ").upper()
        origin = flights[ori_sel]
        dest_sel = input("\n>>> To (acronyms): ").upper()
        destination = origin[dest_sel]
        os.system('clear')
        departures_list()
        dep_time = input("\nSelect departure time: ")
        os.system('clear')
        for i, time in enumerate(destination["departures"]):
            if int(dep_time)-1 == i:
                d_t = time                
        t_v = destination["flight_time"]
        country_dest = flights[dest_sel]
        print("\n>>>> La INFORMACION de tu VUELO es la siguiente:\n")
        Ticket = Flights(origin,country_dest,d_t,t_v)
        print("\n"+f"Departure: {origin['airport_name']} airport")
        print(f"Arrival: {flights[dest_sel]['airport_name']} airport")
        input("...")
        os.system('clear')
        
        

    elif user == "2":
        to_alter = input("Ticket ID: ")
        for i, ticket in enumerate(tickets["tickets"]):
            if ticket["ticket_id"] == to_alter:
                tickets["tickets"].pop(i)
                os.system('clear')
                airports_list()
                new_ori_sel = input("\n>>> From (acronyms): ").upper()
                ori = flights[new_ori_sel]
                new_dest_sel = input("\n>>> To (acronyms): ").upper()
                dest = flights[new_dest_sel]
                os.system('clear')
                ori_to_des = ori[new_dest_sel]
                for i, time in enumerate(ori_to_des["departures"]):
                    print(f"{i+1}: {time}")
                new_dep_time = input("\nSelect departure time: ")
                os.system('clear')
                time = ori_to_des["departures"][int(new_dep_time)-1]
                print("\n>>>> Tu VUELO se MODIFICADO. Comprueba que todo está correcto:\n")
                New_ticket =Flights(ori,dest,time, ori_to_des["flight_time"])
                print("\n"+f"Departure: {ori['airport_name']} airport")
                print(f"Arrival: {dest['airport_name']} airport")
                input("...")
              
            
                
                
          
    elif user == "3":
        to_remove = input("Ticket ID: ")
        for i, ticket in enumerate(tickets["tickets"]):
            if ticket["ticket_id"] == to_remove:
                tickets["tickets"].pop(i)
                with open("./flights.json", "w", encoding = "utf8")as file:
                    json.dump(tickets, file, ensure_ascii=False, indent=4)
                os.system('clear')
                print("\n"+" Hemos CANCELADO tu vuelo.".center(120 - len("Hemos cancelado tu vuelo."),"*"))
                input("...")
                os.system('clear')
            
    
                
                
































# # result = time_now + dt.time
# #'2011-11-04T00:05:23'
# now_str = dt.date.isoformat(time_now)
# # print(type(now_str))
# # print(dt.datetime.fromisoformat(now_str))

# # print(dt.datetime.fromisoformat('2011-11-04T00:05:23'))
# time1=dt.datetime(2021,12,24, 19,26,6)
# time2=dt.datetime(2021,12,20, hour=10,minute=12,second=3)
# print(type(time1))
# newt = time1 - time2 
# print(newt)
# result = time1 - time_now
# # print(result)
# # print(type(result))
# # print(type(time_now))
# eta_1 = time_now + result
# # print(eta_1)
# # print(type(eta_1))