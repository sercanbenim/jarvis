import pyttsx3 #pip install pyttsx3 and use python 3.6.2 64 bit
import datetime
import speech_recognition as sr #pip install SpeechRecognition



engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice' , voices[0].id)
    
    if voice == 2:
        engine.setProperty('voice' , voices[1].id)
    
    speak("hello sir")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is:")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")

def wishme():
    speak("welcome back sir")
    time()
    date()
    greeting()
    speak("Jarvis at your service , How can i help you sir?")


#while True:
#    voice = int(input("press 1 for friday\npress 2 for jarvis\n"))
#    speak(audio)
#    getvoices(voice)
#wishme()

def takeCommandCMD():
    query = input("please tell me how can i help you sir?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-us")
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandCMD().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
