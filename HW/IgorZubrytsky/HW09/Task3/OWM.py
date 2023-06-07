from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def weather_response(city):
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        # Search for current weather in city
        observation = mgr.weather_at_place(city)
        w = observation.weather
        strr = f"""City: {city}\n Conditions: {w.detailed_status}\nTemperature is {round(w.temperature('celsius')
        ['temp'],2)} C \nWind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}%."""
        return strr
    except:
        return '''Oops!!! There was a problem\nretrieving that information.'''

# API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# # ---------- FREE API KEY examples ---------------------


# owm = OWM(API_KEY)
# mgr = owm.weather_manager()
#
#
# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
#
# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75
