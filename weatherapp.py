import requests
import tkinter as tk
import pywinstyles
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('WEATHER_API_KEY')
base_url = "http://api.weatherapi.com/v1/current.json"


def get_weather():
    city=text_area.get("1.0","end-1c")
    if not city:
        result_text = "Please enter a city name."
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, result_text)
        return
    parameters = {'key': api_key, 'q': city, 'units': 'metric'}
    try:
        response = requests.get(base_url, params=parameters)
        data = response.json()
        if response.status_code == 200:
            location = data['location']['name']
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']
            result_text = f"City: {location}\nTemperature: {temp_c}°C\nCondition: {condition}"
            result_label.config(text=result_text, fg="black")
            output=f"City: {location}, Temperature: {temp_c}°C, Condition: {condition}"
        else:
            result_text = data.get('error', {}).get('message', 'Error retrieving data.')
    except Exception as e:
        result_text = f"An error occurred: {e}"
        

root=tk.Tk()
root.geometry("400x400")
root.title("Weather App")
root.config(bg="#333333")
pywinstyles.apply_style(root, style='mica')
label=tk.Label(root,text="Enter City Name",font=("JetBrains Mono",16),bg="#333333")
prompt_label=tk.Label(root,text="Enter city name",font=("JetBrains Mono",12),bg="#333333",fg="white")
prompt_label.pack(pady=10)
text_area=tk.Text(root,height=2,width=20,font=("JetBrains Mono",14),bg="#333333", fg="white")
text_area.pack(pady=10)
button=tk.Button(root,text="Get Weather",command=get_weather, font=("JetBrains Mono",14),bg="#555555",fg="white")
button.pack(pady=10)

result_label=tk.Label(root,text="",font=("JetBrains Mono",16),bg="#333333")
result_label.pack(pady=10)
root.mainloop()