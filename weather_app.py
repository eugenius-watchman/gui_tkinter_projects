from tkinter import *
from unicodedata import category

from PIL import ImageTk, Image
import requests
import json

# from new_window import my_label

root = Tk()
root.title("Weather App")
root.geometry("500x100")

# create zipcode lookup function
def zipLookUp():
    # zip_code.get()
    # zip_label = Label(root, text=zip_code.get())
    # zip_label.grid(row=1, column=0, columspan=2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_code.get() + "&distance=25&API_KEY=3AACB537-0B07-4DCE-9F6C-C57CADB8CD5C")

        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#66000"

        root.configure(background=weather_color)

        my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                         background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error...!"


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=3AACB537-0B07-4DCE-9F6C-C57CADB8CD5C


# zip code entry
zip_code = Entry(root)
zip_code.grid(row=0, column=0, stick=W+E+N+S)

zip_button = Button(root, text="Zipcode Lookup", command=zipLookUp)
zip_button.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()