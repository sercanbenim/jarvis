import pyttsx3  # pip install pyttsx3  # python 3.8.5 32 bit
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os





engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Sir!")

    time()

    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("Jarvis is at your service Please tell me how can i help you today?")


def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening..")
            r.pause_threshold = 1  
            audio = r.listen(source)

        try:
            print("recognizing..")
            query = r.recognize_google(audio, language='en-us')
            print(query)
        except Exception as e:
            print(e)
            speak("say that again please sir")

            return " none"
        return query


def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('akural78@gmail.com', 'angeluss')
        server.sendmail('akural78@gmail.com', to, content)
        server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'srcnbnm@gmail.com'
                sendEmail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif 'search in chrome' in query:
            speak("what should i search sir?")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)

        elif 'remember that' in query:
                speak("what should i remember?")
                data = takeCommand()
                speak("you told me to remember"+data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
        
        elif 'jarvis' in query:
                speak("I'm here sir.")

        elif 'still here' in query:
                speak("yes sir")

        elif 'help me' in query:
                speak("i will do my best sir")
        
        elif 'miss me' in query:
                speak("yes of course sir")


        elif 'do you know' in query:
                remember = open('data.txt', 'r')
                speak("you told me to remember that" + remember.read())

        elif 'offline' in query:
            quit()
