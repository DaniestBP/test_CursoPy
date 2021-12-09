import requests as req
import json
import time 

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


def get_data(json_file):
    
    with open(json_file, encoding="utf8 ") as file:
        return json.load(file)


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
        print(f"term: {term}")
        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url).json()
        
        if len(woeid)>= 1:
            for loc in woeid:
                woeids[loc["title"].lower()]= loc["woeid"]
                write_data(woeids, "woeids.json")
            if limit:
                return [dic["woeid"] for dic in woeid[0:limit]]
            else:
                return [woeid[0]["woeid"]]
        else:
            return None
           
    return [woeid]
         

def get_forecast(location, **kwargs):
    woeid = get_woeid(location, **kwargs)[0]
    url = f"https://www.metaweather.com/api/location/{woeid}"
    date = kwargs.get("date")
    if date:
        url += date
    forecast = req.get(url).json()
    if type(forecast) == list:
        if len(forecast) >= 1:
            forecast = forecast[0]
        if not len(forecast):
            return None
    return forecast

def calculate_trip(A,B):
    A_woeid = get_woeid(A)
    # B_woeid = get_woeid(B)
    B_woeid, B_distance = None, None
    if A_woeid:
        A_woeid = A_woeid[0]
        A_coords = req.get(f"https://www.metaweather.com/api/location/{A_woeid}/").json()["latt_long"]
        des_list = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={A_coords}").json()
        
        for des in des_list[1:]:
            if des["title"].lower() == B.lower():
                B_woeid, B_distance = des["woeid"], des["distance"]
                
        if B_woeid:
            A_forecast, B_forecast = get_forecast(A)["consolidated_weather"][0], get_forecast(B)["consolidated_weather"][0]
            if A_forecast["weather_state_abbr"] in ("sn", "sl", "h", "t", "hr") or B_forecast["weather_state_abbr"] in ("sn", "sl", "h", "t", "hr"):
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
     


def forecast_v2(location, **kwargs):
    
    term = "query"
    woeid = woeids.get(location)

    if not woeid:
        
        if kwargs.get("coords"):
            term = "lattlong"
        url = f"https://www.metaweather.com/api/location/search/?{term}={location}"
        woeid = req.get(url).json()
           
        
        if len(woeid)>= 1:
            for loc in woeid:
                woeids[loc["title"].lower()]= loc["woeid"]
            woeid = woeid[0]["woeid"]
            write_data(woeids, "woeids.json")
            
        else:
            print("return none se ha ejecutado")
            return None  
   
    # A partir de aqui podemos buscar por "woeid":
    """
    generar la url de llamada en base al woeid obtenido en el codigo anterior --> url = "weather..."
    """
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    date = kwargs.get("date")
    
    if date:
        url += date
    print(url)
    forecast = req.get(url).json()
     
    if type(forecast) == list:
        forecast = forecast[0]
        if not len(forecast):
            return None
    forecast = forecast["consolidated_weather"][0]
    # print(forecast)               
    forecast = {
        "desc": forecast["weather_state_name"],
        "max-temp": forecast["max_temp"],
        "min_temp": forecast["min_temp"],
        "st": forecast["the_temp"],
        "humidity": forecast["humidity"],
        "wind_speed": forecast["wind_speed"],
        "wind_direction": forecast["wind_direction"]
    }
    return forecast
        
           
# print(forecast_v2("48.856930,2.341200"))


# print(get_forecast("lisbon", date = "2020/10/10"))




# forecast_v2("21.304850,-157.857758")


    
