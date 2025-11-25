import tkinter as tk
root = tk.Tk()
root.title("Weather App")
root.geometry("600x400") # Changed resolution for better display

# 1. Title Label
title_label = tk.Label(root, text="Welcome to Weather App", font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

# 2. Input/Text Area (for city name)
prompt_label = tk.Label(root, text="Enter City Name:")
prompt_label.pack()

text_area = tk.Text(root, height=1, width=30, font=('Arial', 12))
text_area.pack(pady=10)

# 3. Button (connected to the function)
# The 'command' attribute links the button click to the get_weather function.
button = tk.Button(root, 
                   text="Get Weather", 
                   command=get_weather, 
                   font=('Arial', 12), 
                   bg='#4CAF50', fg='white')
button.pack(pady=20)

# 4. Result Display Label
result_label = tk.Label(root, text="Results will appear here.", justify=tk.LEFT, font=('Arial', 12))
result_label.pack(pady=10, padx=10)

root.mainloop()