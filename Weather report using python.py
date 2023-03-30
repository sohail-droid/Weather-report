import requests     #gets data from the browser
import json         #converts into dictionary parts
import pyttsx3      #text to speech conversion only for windows

engine = pyttsx3.init('sapi5')
engine.say("Welcome to Today's Weather Report")
print("Welcome to Today's Weather Report ")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)     #0 -- male  , 1 - female
print(voices[1].id)                      #u can know whats the name of machine speaking here.
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':                        #MAIN function starts here
     x = "zira"
     engine.say(f"Hii there, my name is{x}, your Assistant ")



speak("Enter The Name of the City: ")
city = input("Enter The Name of the City: ")
speak(city)

url = f"http://api.weatherapi.com/v1/current.json?key=e5e800737cb54fb692252101232803&q={city}"
speak(f"Gathering The info of {city}from the clouds...hang on")

r = requests.get(url)  # Making a get request
print("Gathering all the info...........")
print(r.text)  # printing request text it will convert the data into text for requests module
# json function

wdic = json.loads(r.text)
w = wdic["current"]["temp_f"]   #u can change ur input or commands what u want here in this nested dictionary
speak(f"The current iformation of the {city} is {w}  ")
print(w)

