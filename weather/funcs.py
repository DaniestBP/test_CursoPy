import requests as req
import json
import time

from requests.api import get 

def menu():
    print("\n" + " BRILLIANT WEATHER".center(155, "*")+ "\n")
    print(" >  Por favor elija el lugar donde desea consultar el tiempo  <".center(150)+ "\n")
    print(" 1. Buscar por ciudad: " + (" "*(180 - len("2. Buscar por coordenadas: "))) + "\n")
    print(" 2. Buscar por coordenadas: " + (" "*(175 - len("2. Buscar por coordenadas: "))) +"\n")
    print(" 3. ciudad/coordenadas en fecha: " + (" "*(165 -len("3. ciudad/coordenadas en fecha: "))) + "\n")
    print(" 4. Planea tu viaje: " + (" "*(165 -len("3. ciudad/coordenadas en fecha: "))) + "\n")
    print(" Para salir (Q): " + (" " * (180 - len("Para salir (Q): ")))+ "\n")


def pretty_print(forecast):
    for k, v in forecast.items():
        print(f"{k.upper()}: {v}")
    input()


def get_data(json_file):
    try:   
        with open(json_file, encoding="utf8 ") as file:
            return json.load(file)
    except Exception:
        return {}


def write_data(data, json_file):
    with open (json_file, mode="w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

woeids = get_data("woeids.json")

def get_woeid(location, **kwargs):
    term = "query"
    woeid = woeids.get(location.lower())
    limit = kwargs.get("limit")
    if not woeid:
        if kwargs.get("coords"):
            term = "lattlong"
        
        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url)
        
        if woeid:
            woeid = woeid.json()
            if woeid:
                for loc in woeid:
                    woeids[loc["title"].lower()] = loc["woeid"]
                write_data(woeids, "woeids.json")
                if limit:
                    return [dic["woeid"] for dic in woeid[0:limit]]
                else:
                    return [woeid[0]["woeid"]]
            else:
                return []
    return [woeid]
                    
           
         

def get_forecast(location, **kwargs):
    woeid = get_woeid(location, **kwargs)

    if woeid:
        woeid = woeid[0]
        url = f"https://www.metaweather.com/api/location/{woeid}/"     
        date = kwargs.get("date")
        if date:
            url += date
        forecast = req.get(url)
    
        if forecast:
            forecast = forecast.json()
            if forecast:
                if not date:
                    forecast = forecast["consolidated_weather"]
                fore_reduc = []
                    
                for predict in forecast[:3]:
                    fore_reduc.append({
                        "date": predict["applicable_date"],  
                        "desc": predict["weather_state_name"],
                        "abbr": predict["weather_state_abbr"],
                        "max-temp": predict["max_temp"],
                        "min_temp": predict["min_temp"],
                        "st": predict["the_temp"],
                        "humidity": predict["humidity"],
                        "wind_speed": predict["wind_speed"],
                        "wind_direction": predict["wind_direction"]
                    })
                return fore_reduc
    return []
        


def calculate_trip(A,B):
    A_woeid = get_woeid(A)
    B_woeid, B_distance = None, None
    
    if A_woeid:
        A_woeid = A_woeid[0]
        A_coords = req.get(f"https://www.metaweather.com/api/location/{A_woeid}/").json()["latt_long"]
        des_list = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={A_coords}").json()
        
        for des in des_list[1:]:
            if des["title"].lower() == B.lower():
                B_woeid, B_distance = des["woeid"], des["distance"]
                
        if B_woeid:
            A_forecast, B_forecast = get_forecast(A)[0], get_forecast(B)[0]
            if A_forecast["abbr"] in ("sn", "sl", "h", "t", "hr") or B_forecast["abbr"] in ("sn", "sl", "h", "t", "hr"):
                is_bad_weather = True
            else:
                is_bad_weather = False
            
            wind_limit = 10
            result = {
                "A_forecast": A_forecast,
                "B_forecast": B_forecast,
                "distance": B_distance/1000,
                "A_wind_speed": A_forecast["wind_speed"],
                "B_wind_speed": B_forecast["wind_speed"],
                "is_bad_weather": is_bad_weather     
            }
            if result["A_wind_speed"] >= wind_limit or result["B_wind_speed"] >= wind_limit:
                result["time"] = result["distance"] / 90
            else:
                result["time"] = result["distance"] / 100
            return result
    return None




