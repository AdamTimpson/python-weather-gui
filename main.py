import requests
from tkinter import *

locationInput = None
URL = "http://api.openweathermap.org/data/2.5/weather?q="
APPID = "aef05bec61475023552649aea192429b"

def trace(f):
    "Prints the trace for the given function"
    print("main::" + f)

    return

def displayWeatherInfo(data):
    "Displays the weather information on the GUI"
    trace("displayWeatherInfo")

    

    return

def getWeatherForLocation(locationString):
    "Gets weather information using a given location"
    trace("getWeatherForLocation")

    global URL
    URL += locationString
    print("URL: " + URL)

    r = requests.get(url = URL, params={"appid": APPID}, timeout=5)
    data = r.json()

    print(data)
    
    displayWeatherInfo(data)

    return

def submitButton_Click():
    "Click handler for submit button"
    trace("submitButton_Click")

    locationString = locationInput.get()

    print("Input: " + locationString)

    getWeatherForLocation(locationString)

    return

def initGUI():
    "Responsible for GUI"
    trace("initGUI")

    window = Tk()

    window.title("Weather GUI")
    window.geometry("640x480")
    
    global locationInput
    locationInput = Entry(window, width=20)
    locationInput.grid(column = 0, row = 0)

    submitButton = Button(window, text="Submit", command=submitButton_Click)
    submitButton.grid(column = 1, row = 0)

    window.mainloop()

    return

def main(): 
    "Start everything from here"
    trace("main")
    
    initGUI();

    return

main()
