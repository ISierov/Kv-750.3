from pyowm import OWM
import tkinter as tk
import traceback

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather = f"""
 Status - {w.detailed_status}
 Wind speed - {w.wind()["speed"]}
 Humidity - {w.humidity}
 Temperature - {w.temperature('celsius')["temp"]}
 Rain - {w.rain}
 Heat index - {w.heat_index}
 Clouds - {w.clouds}
"""
        label['text'] = weather
    except:
        traceback.print_exc(file=open('test.log', 'a'))
        label['text'] = " Enter correct city name"


HEIGHT = 400
WIDTH = 520

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


def on_click(event):
    event.widget.delete(0, tk.END)


entry_field = tk.Entry(frame, font=('Courier', 16))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.insert(0, "Enter name of the city")
entry_field.bind("<Button-1>", on_click)
entry_field.bind("<Return>", lambda event: get_weather(entry_field.get()))

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="black",
                   font=('Courier', 15),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, justify=tk.LEFT, anchor="w", font=('Courier', 20))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
