from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()



def get_data(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    return f"""
 Status: {w.detailed_status}
 Wind speed: {w.wind()["speed"]}
 Humidity: {w.humidity}
 Temperature: {w.temperature('celsius')}
 Rain: {w.rain}
 Heat index {w.heat_index}
 Clouds - {w.clouds}
"""