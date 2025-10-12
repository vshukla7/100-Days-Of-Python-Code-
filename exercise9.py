import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
 
# change the voice to Zira (the Windows voice)
engine.setProperty('voice', voices[1].id)

name = ["vinayak" , "manas"]

for n in name:
    engine.say(n + " ko soutout")
    engine.runAndWait()

