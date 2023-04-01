import tkinter as tk
from pyowm import OWM


def wind_direction(deg):
    """Convert degrees to wind direction"""
    direction = ("North \U00002b07", "East \U00002b05", "South \U00002b06", "West \U000027A1")
    if 0 <= deg <= 45 or 315 <= deg <= 360:
        return direction[0]
    elif 45 < deg <= 135:
        return direction[1]
    elif 135 < deg <= 225:
        return direction[2]
    else:
        return direction[3]


def get_weather(city):
    owm = OWM('ef2206ff5da67de63306d0b143e20872')
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        detailed_status = w.detailed_status  # 'clouds'
        wind = w.wind()  # {'speed': 4.6, 'deg': 330}
        humidity = w.humidity  # 87
        temper = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        heat_index = w.heat_index  # None
        clouds = w.clouds  # 75
        information = f'''Sky status: {detailed_status}
    Current temperature: {round(temper.get('temp'))}°C
    Wind: {wind.get('speed')}m/s {wind_direction(wind.get('deg'))}
    Humidity: {humidity}%
    Density clouds: {clouds}%
    Heat index: {heat_index}
    '''
        return information
    except:
        return "Your city not found"


HEIGHT = 350
WIDTH = 450

root = tk.Tk()
message = tk.StringVar()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="black",
                   font=('Courier', 10),
                   command=lambda: message.set(get_weather(entry_field.get())))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), textvariable=message)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
