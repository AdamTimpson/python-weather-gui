import requests
from tkinter import *

locationInput = None
lonLabel = None
latLabel = None
mainLabel = None
tempLabel = None
humLabel = None
nameLabel = None
window = None

URL = "http://api.openweathermap.org/data/2.5/weather?q="
APPID = "aef05bec61475023552649aea192429b"

def trace(f):
    "Prints the trace for the given function"
    print("main::" + f)

    return

def changeText(c, t):
    "Used for changing the text of a coponent"
    trace("changeText")

    if c != None:
        c.configure(text = t)

        return True

    return False

def convertToCelcius(k):
    "Convert from Kelvin to Celcius"
    trace("convertToCelcius")

    c = (k - 273.15)

    return round(c, 1)

def displayWeatherInfo(data):
    "Displays the weather information on the GUI"
    trace("displayWeatherInfo")

    global window

    global lonLabel
    lonText = "Longitude: " + str(data["coord"]["lon"])
    
    if changeText(lonLabel, lonText) != True:    
        lonLabel = Label(window, text = lonText)
    
    lonLabel.grid(column = 0, row = 1)

    global latLabel
    latText = "Latitude: " + str(data["coord"]["lat"])

    if changeText(latLabel, latText) != True:    
        latLabel = Label(window, text = latText)

    latLabel.grid(column = 0, row = 2)

    global mainLabel
    mainText = "Weather: "
    mainText += str(data["weather"][0]["main"]) 
    mainText += " (" + str(data["weather"][0]["description"]) 
    mainText += ")"

    if changeText(mainLabel, mainText) != True:    
        mainLabel = Label(window, text = mainText)
    
    mainLabel.grid(column = 0, row = 3)

    global tempLabel
    tempText = "Temperature: "
    tempText += str(convertToCelcius(data["main"]["temp"]))
    tempText += "C"

    if changeText(tempLabel, tempText) != True:
        tempLabel = Label(window, text = tempText)

    tempLabel.grid(column = 0, row = 4)

    window.update()

    return

def getWeatherForLocation(locationString):
    "Gets weather information using a given location"
    trace("getWeatherForLocation")

    global URL
    URL += locationString
    print("URL: " + URL)

    r = requests.get(url = URL, params={"appid": APPID}, timeout=5)
    data = r.json()

    URL = "http://api.openweathermap.org/data/2.5/weather?q="

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

    global window
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
