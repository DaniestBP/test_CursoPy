import requests as req


# def forecast(location, coordinates=False, date=False):

#     if coordinates:
#         woeid = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={location}").json()[0]["woeid"]
#         forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
#     else:
#         woeid = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["woeid"]
#         forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
#     forecast = {
#         "desc": forecast["weather_state_name"],
#         "max-temp": forecast["max_temp"],
#         "min_temp": forecast["min_temp"],
#         "st": forecast["the_temp"],
#         "humidity": forecast["humidity"],
#         "wind_speed": forecast["wind_speed"],
#         "wind_direction": forecast["wind_direction"]
#     }
#     return forecast



def forecast(location, **kwargs):
    woeid = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={location}").json()[0]["woeid"]
    forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
    
    if kwargs.get("coordinates"):
        woeid_res = woeid(kwargs["woeid"])
        return forecast(woeid_res)
    
    elif kwargs.get("date"):
        woeid_res = woeid(kwargs["woeid"])
        return forecast(woeid_res)



    else:
        woeid = req.get(f"https://www.metaweather.com/api/location/search/?query={location}").json()[0]["woeid"]
        forecast = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()["consolidated_weather"][0]
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


print(forecast("Madrid", date ="2013/10/10"))
