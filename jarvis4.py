from os import name, remove
import newsapi
import pyttsx3 #pip install pyttsx3 and use python 3.6.2 64 bit
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage, Message
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
from wikipedia.wikipedia import search
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize







engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice' , voices[0].id)
        speak("hello sir This is friday")

    if voice == 3:
        engine.setProperty('voice' , voices[2
        ].id)
        speak("hello sir this is jarvis")
    

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
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again sir")
        return "none"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search sir?')
    search = takeCommandMic()
    wb.open('https://www.google.com.tr/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='79e264eb07f2471592a357a1304c266d')
    speak('what topic you need to know sir?')
    topic = takeCommandMic()
    

    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
                                 
    
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("that is it sir i will update you soon")


def text2speech():
    text= clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data =  f'Confirmed cases : {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered : {data["recovered"]}'
    print(covid_data)
    speak(covid_data)


def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\x230\\Desktop\\jarvis\\screenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen =8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

#http://api.openweathermap.org/data/2.5/weather?q={city name}&units=imperial&appid={1164bd464e0a5923c4f550edd764ec2e



if __name__ == "__main__":
    getvoices(3)
    #wishme()
    wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'email' in query:
                email_list = {
                    'my email' :'benimsercan@gmail.com'

                }
                try:
                    speak("To whom you want to send mail sir?")
                    name = takeCommandMic()
                    receiver = email_list[name]
                    speak("What is the subject of the mail sir?")
                    subject = takeCommandMic()
                    speak('what should i send sir?')
                    content = takeCommandMic()
                    sendEmail(receiver, subject, content)
                    speak("email has been send sir")
                except Exception as e:
                    print(e)
                    speak("unable to send the email sir")

            elif 'message' in query:
                user_name = {
                    'Jarvis': '+905433035758'
                } 
                try:
                    speak("To whom you want to send whats app message sir?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message sir?")
                    message = takeCommandMic()
                    sendwhatsmsg(phone_no,message)                
                    speak("message has been send sir")
                except Exception as e:
                    print(e)
                    speak("unable to send the message sir")  
                    
            elif 'wikipedia' in query:
                    speak('searching on Wikipedia sir')
                    query = query.replace("wikipedia","")
                    result = wikipedia.summary(query, sentences = 2)
                    print(result)
                    speak(result)

            elif 'search' in query:
                    searchgoogle()

            elif 'youtube' in query:
                speak("what should i search on youtube sir?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)

            elif'weather' in query:
                url = 'http://api.openweathermap.org/data/2.5/weather?q=çorlu&units=imperial&appid=1164bd464e0a5923c4f550edd764ec2e'

                res = requests.get(url)
                data = res.json()

                weather = data['weather'] [0] ['main']
                temp = data['main']['temp']
                desp = data['weather'] [0] ['description']
                temp = round((temp -32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))
            
            elif 'news' in query:
                news()

            elif 'read' in query:
                text2speech()
                
            elif 'virus' in query:
                covid()

            elif 'open documents' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))


            elif 'open code' in query:
                codepath = 'C:\\Users\\x230\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)

            elif 'screenshot' in query:
                screenshot()

            elif 'remember that' in query:
                speak("what should i remember sir?")
                data= takeCommandMic()
                speak("You told me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()

            elif 'remind me' in query:
                remember = open('data.txt','r')
                speak("you told me to remeber that"+remember.read())

            elif 'pass' in query:
                passwordgen()
            elif 'here' in query:
                    speak("I'm here sir.")

            elif 'still here' in query:
                    speak("yes sir")

            elif 'help me' in query:
                    speak("i will do my best sir")
            
            elif 'miss me' in query:
                    speak("yes of course sir")
            
            elif 'friday' in query:
                codepath = 'C:\\Users\\x230\\Desktop\\jarvis\\friday.py'
                os.startfile(codepath)
            
            elif 'cpu' in query:
                cpu()

            elif 'offline' in query:
                speak('Jarvis going offline see you soon sir')
                quit()

# takeCommandMic == "hey jarvis what is the date today" tokenize =['hey' , 'jarvis' , 'what' , 'is' , 'the' , 'date' , 'today']