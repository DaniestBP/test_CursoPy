import datetime as dt
import json
from random import randint


def get_data(json_file):
    with open (json_file, encoding = "utf8")as file:
        return json.load(file)
flights = get_data("airports.json")

def get_tickets(json_file):
    with open (json_file, encoding="utf8")as file:
        return json.load(file)
tickets = get_tickets("flights.json")


def ticket_writter(func):
    def writter(*args, **kwargs):
        time = dt.datetime.utcnow()
        tomorrow = time + dt.timedelta(days = 1)
        tomor_str = dt.date.isoformat(tomorrow)
        ticket_id = str(randint(100000,999999))
        result = func(*args, **kwargs)
        origin = args[0]
        destination = args[1]
        d_t = args[2]
        t_v = args[3]
        eta = result.ETA()
        ticket_dict = {
                "ticket_id": ticket_id,
                "time": f"{time}",
                "from": origin["city"],
                "to": destination["city"],
                "departure at": f"{tomor_str} {d_t}:00",
                "flight_time": t_v,
                "Arrival_times":eta
            }
        tickets["tickets"].append(ticket_dict)
        with open("./flights.json", "w", encoding = "utf8")as file:
            json.dump(tickets, file, ensure_ascii=False, indent=4)
            for key in ticket_dict:
                print(f"{key}: {ticket_dict[key]}")
        return result
    return writter
                

            
   
   

@ticket_writter
class Flights:
        
    def __init__(self, origin, destination, dep_hours,t_v):
        self.origin = origin
        self.destination = destination
        self.dep_hours = dep_hours
        self.t_v = t_v
   

    def avg_UTC(self):
        return self.destination["UTC"] - self.origin["UTC"]

    def ETA(self):
        t_v = dt.timedelta(hours = self.t_v)
        time_now =dt.datetime.utcnow()
        tomorrow = time_now + dt.timedelta(days=1) 
        tomor_str = dt.date.isoformat(tomorrow)
        flight_str = f"{tomor_str}T{self.dep_hours}:00"
        flight_iso = dt.datetime.fromisoformat(flight_str)
        arrival_time1 = flight_iso + t_v
        UTC_adj = dt.timedelta(hours = self.avg_UTC())
        arrival_time2 = arrival_time1 + UTC_adj
        info = {f"Arrival_origin":f"{arrival_time1}", f"Arrival_destination":f"{arrival_time2}"}              
        return info  
        

 

    
        
# print(flights["SPA"]["UTC"])
# Vuelo1= Flights(flights["SPA"], flights["BRA"], "07:30",11)
# print(Vuelo1.avg_UTC())
# print(Vuelo1.ETA())
# print(Vuelo1.origin["city"])
# print(type(Vuelo1.destination))
