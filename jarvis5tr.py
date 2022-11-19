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
import pyjokes
import wolframalpha







engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice' , voices[0].id)
        speak("Merhaba efendim ben sanal asistanınız fatma")

    if voice == 3:
        engine.setProperty('voice' , voices[2].id)
        speak("Merhaba efendim ben sanal asistanınız jarvis")
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Şuan saat:")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Tbugünün tarihi:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("günaydın efendim")
    elif hour >= 12 and hour < 18:
        speak("Tüanydın efendim")
    elif hour >= 18 and hour < 24:
        speak("iyi akşamlar efendim")
    else:
        speak("iyi geceler efendim")

def wishme():
    speak("tekrar hoşgeldiniz efendim")
    time()
    date()
    greeting()
    speak("Jarvis hizmetinizde size nasıl yardımcı olabilirim?")


#while True:
#    voice = int(input("press 1 for friday\npress 2 for jarvis\n"))
#    speak(audio)
#    getvoices(voice)
#wishme()

def takeCommandCMD():
    query = input("Size nasıl yardımcı olabilirim?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Çözümlüyorum...")
        query = r.recognize_google(audio , language="tr-tr")
        print(query)
    except Exception as e:
        print(e)
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
    speak('ne aramalıyım efendim?')
    search = takeCommandMic()
    wb.open('https://www.google.com.tr/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='79e264eb07f2471592a357a1304c266d')
    speak('ne hakkında arama yapmamı istersiniz efendim?')
    topic = takeCommandMic()
    

    data = newsapi.get_top_headlines(q=topic,
                                    language='tr',
                                    page_size=5)
                                 
    
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("sizi yakında bilgilendireceğim")


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
    speak('CPU şuan'+ usage)
    battery = psutil.sensors_battery()
    speak('Batarya şuan')
    speak(battery.percent)

#http://api.openweathermap.org/data/2.5/weather?q={city name}&units=imperial&appid={1164bd464e0a5923c4f550edd764ec2e

def jokes():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by Sir John , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak("Sir John is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")

if __name__ == "__main__":
    getvoices(0)
    #wishme()
    wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        print(query)
       
        if 'saat' in query:
            time()
        elif 'gün' in query:
            date()
        elif 'posta' in query:
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

        elif 'mesaj' in query:
            user_name = {
                'Ben': '+905433035758'
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

        elif 'ara' in query:
                searchgoogle()

        elif 'youtube' in query:
                speak("what should i search on youtube sir?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)

        elif 'hava' in query:
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
            
        elif 'haber' in query:
                news()

        elif 'oku' in query:
                text2speech()
                
        elif 'virus' in query:
                covid()
        elif 'nasılsın' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")

        elif 'open documents' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))


        elif 'want to play' in query:
                codepath = 'D:\\EA GAMES\\Need for Speed Most Wanted\\speed.exe'
                os.startfile(codepath)

        elif 'screenshot' in query:
                screenshot()

        elif 'hatırla' in query:
                speak("what should i remember sir?")
                data= takeCommandMic()
                speak("You told me to remember that"+data)
                remember = open('data.txt','a')
                remember.write(data)
                remember.close()
        elif 'kimim' in query:
            speak("If you can talk, then definitely you are a human")
        elif 'why you came to this world' in query:
            speak("Thanks to Sir John. further it is a secret")

        elif 'şarkı çal' in query:
            video ='C:/VIDEOS'
            audio = 'C:/SONGS'
            speak("What songs should i play? Audio or Video")
            ans = (takeCommandMic().lower())
            while(ans != 'ses' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (takeCommandMic().lower())
        
            if 'ses' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (takeCommandMic().lower())
            while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                rand = (takeCommandMic().lower())

            if 'numara' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'rastgele' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue

        elif 'hatırlat' in query:
            remember = open('data.txt','r')
            speak("you told me to remeber that"+remember.read())

        elif 'şifre' in query:
                passwordgen()
        

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
        elif 'not yaz' in query:
            speak("What should i write, sir")
            note = takeCommandMic()
            file = open('note.txt', 'a')
            speak("Sir, Should i include date and time")
            dt = takeCommandMic()
            if 'evet' in dt or 'tabi' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif 'not göster' in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 
        elif 'joke' in query:
            jokes()
        elif 'who are you' in query:
            Introduction()
        
        elif 'creator' in query:
            Creator()
        
        #show location on map
        elif "nerede" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "hesapla" in query:
            
            app_id = "ERV4RP-6XWH2JAVWT"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif 'nedir' in query or 'kim' in query: 
			
			# Use the same API key 
			# that we have generated earlier
            app_id = "ERV4RP-6XWH2JAVWT"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 




        #sleep-time
        elif 'dinleme' in query or 'dinlemeyi bırak' in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(takeCommandMic())
            time.sleep(a)
            print(a)


        elif 'offline' in query:
                speak('Jarvis going offline see you soon sir')
                quit()

# takeCommandMic == "hey jarvis what is the date today" tokenize =['hey' , 'jarvis' , 'what' , 'is' , 'the' , 'date' , 'today']