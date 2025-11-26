import requests
import customtkinter as ctk
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
        text_area.delete("1.0", ctk.END)
        text_area.insert(ctk.END, result_text)
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
            result_label.configure(text=result_text)
            output=f"City: {location}, Temperature: {temp_c}°C, Condition: {condition}"
        else:
            result_text = data.get('error', {}).get('message', 'Error retrieving data.')
            result_label.configure(text=result_text, text_color="Red")
    except Exception as e:
        result_text = f"An error occurred: {e}"
        result_label.configure(text=result_text, text_color="Red")
        

root=ctk.CTk()
root.geometry("1050x700")
root.title("Weather App")
ctk.set_appearance_mode("dark")
root.configure(bg="#333333")
pywinstyles.apply_style(root, style='mica')
label=ctk.CTkLabel(root,text="Enter City Name",font=("JetBrains Mono",16), text_color="White")
prompt_label=ctk.CTkLabel(root,text="Enter city name",font=("JetBrains Mono",18), text_color="White")
prompt_label.pack(pady=10)
text_area=ctk.CTkTextbox(root,height=2,width=200,font=("JetBrains Mono",14))
text_area.pack(pady=10)
button=ctk.CTkButton(root,text="Get Weather",command=get_weather, font=("JetBrains Mono",14), fg_color="#0078D7", hover_color="#005A9E")
button.pack(pady=10)

result_label=ctk.CTkLabel(root,text="",font=("JetBrains Mono",16),)
result_label.pack(pady=10)
root.mainloop()