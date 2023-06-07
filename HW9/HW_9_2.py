import tkinter as tk
import requests
from PIL import ImageTk, Image
import io

# Function to get the weather
def get_weather(city):
    weather_key = '4cb1d0ea01dc3b3c2fa5629eb7a61c0a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    # Output the weather to the console
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    return weather

# Function to display the weather
def show_weather():
    city = city_entry.get()
    weather = get_weather(city)

    # Display the weather on the screen
    weather_desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    temp_label.config(text='Temperature: {:.1f}°C'.format(temp))
    desc_label.config(text='Weather: {}'.format(weather_desc))

    # Display the weather icon
    icon_url = 'http://openweathermap.org/img/w/{}.png'.format(weather['weather'][0]['icon'])
    icon_response = requests.get(icon_url, stream=True)
    img_data = icon_response.content
    img = Image.open(io.BytesIO(img_data))
    icon = ImageTk.PhotoImage(img)
    icon_label.config(image=icon)
    icon_label.image = icon


# Creating a graphical interface
root = tk.Tk()
root.title('Weather App')

# Create a field for entering a location and a button
city_entry = tk.Entry(root)
city_entry.pack(pady=10)
get_weather_button = tk.Button(root, text='Get Weather', command=show_weather)
get_weather_button.pack()

# Creating labels for weather output
temp_label = tk.Label(root, font=('Calibri', 14))
temp_label.pack(pady=10)
desc_label = tk.Label(root, font=('Calibri', 14))
desc_label.pack(pady=10)

# Create a label to display the weather icon
icon_label = tk.Label(root)
icon_label.pack()

root.mainloop()