from pyowm import OWM


def weather_response(city):

    API_KEY = '908ecabfc23fdac5d5e200db99a0f9df'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    output_text = f"City: {city}\nConditions: {w.detailed_status}\nTemperature is " \
                  f"{round(w.temperature('celsius')['temp'], 2)} C"\
                  f"\nWind speed is {w.wind()['speed']} km/hour\nHumidity of the air is {w.humidity}"

    return output_text


    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75


