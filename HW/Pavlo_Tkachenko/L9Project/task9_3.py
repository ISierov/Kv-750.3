import tkinter as tk
from tkinter import font
from pyowm import OWM

def get_weather(place):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(place)
    w = observation.weather

    res = '' + str(w.detailed_status) + ' (' + str(w.clouds) + '%)' + '\n' \
          + str(w.temperature('celsius')['temp_min']) + ' - ' + str(w.temperature('celsius')['temp_max']) + '\u2103\n' \
          + 'wind: ' + str(w.wind()['speed']) + ' m/s, ' + str(w.wind()['deg']) + ' deg' + '\n' \
          + 'humidity: ' + str(w.humidity) + '%' \
          + ('\n' + 'rain: ' + str(w.rain) if len(w.rain) > 0 else "") \
          + ('\n' + 'heat_index: ' + str(w.heat_index) if w.heat_index is not None else "")

    label["text"] = res

#######
HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda:  get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

