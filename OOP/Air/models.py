import datetime as dt
import json



def get_data(json_file):
    with open (json_file, encoding = "utf8")as file:
        return json.load(file)
flights = get_data("airports.json") 

class Flights:
    def __init__(self, origin, destination, dep_hours,t_v):
        self.origin = origin
        self.destination = destination
        self.dep_hours = dep_hours
        self.t_v = t_v

    def avg_UTC(self):
        return self.destination["UTC"] - self.origin["UTC"]

    def tomorrow():
        pre = dt.datetime.utcnow() + dt.timedelta(days=1)
        pos = dt.datetime(year=pre.year, month = pre.month, day=pre.day)
        return pos

    def ETA(self):
        t_v = dt.timedelta(hours = self.t_v)
        time_now =dt.datetime.utcnow()
        
        now_str = dt.date.isoformat(time_now)
        flight_str = f"{now_str}T{self.dep_hours}:00"
        print(flight_str)
        flight_iso = dt.datetime.fromisoformat(flight_str)
        arrival_time = flight_iso + t_v
        UTC_adj = dt.timedelta(hours = self.avg_UTC())
        arrival_time = arrival_time + UTC_adj                           
        return arrival_time
        
    
        
# print(flights["SPA"]["UTC"])
Vuelo1= Flights(flights["ARG"], flights["PER"], "19:00",4.5)
# print(Vuelo1.avg_UTC())
print(Vuelo1.ETA())
# print(type(Vuelo1.origin))
# print(type(Vuelo1.destination))