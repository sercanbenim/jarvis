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
    speak("saat şuanda")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("tarih şuanda ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("tekrar hoşgeldiniz efendim!")

    time()

    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Günaydın efendim")
    elif hour >= 12 and hour < 18:
        speak("Tünaydın efendim")
    elif hour >= 18 and hour < 24:
        speak("iyi akşamlar efendim")
    else:
        speak("İyi geceler efendim")

    speak("Jarvis emrinizde efendim bugün size nasıl yardımcı olabilirim?")


def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("dinliyorum..")
            r.pause_threshold = 1  
            audio = r.listen(source)

        try:
            print("tanımlıyorum..")
            query = r.recognize_google(audio, language='tr-tr')
            print(query)
        except Exception as e:
            print(e)
            speak("Tekrarlarmısınız efendim?")

            return " none"
        return query


def sendEmail (to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('', '')
        server.sendmail('', to, content)
        server.close()


if __name__ == "__main__":
    #wishme()
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
        elif 'e-mail gönder' in query:
            try:
                speak("ne söylemek istersiniz?")
                content = takeCommand()
                to = 'srcnbnm@gmail.com'
                sendEmail(to, content)
                speak("email gönderildi")
            except Exception as e:
                print(e)
                speak("email gönderilemiyor")

        elif 'chrome da ara' in query:
            speak("ne aramalıyım efendim?")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'hatırla' in query:
                speak("neyi hatırlamalıyım efendim?")
                data = takeCommand()
                speak("bunu hatırlamamı istediniz efendim."+data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
        
        elif 'jarvis' in query:
                speak("Buradayım efendim.")

        elif 'still here' in query:
                speak("evet efendim")

        elif 'bana yardım et' in query:
                speak("istediğiniz herşeyi yaparım efendim")
        
        elif 'miss me' in query:
                speak("tabi ki efendim.")


        elif 'hatırlat' in query:
                remember = open('data.txt', 'r')
                speak("bunu hatırlatmamı istediiniz efendim" + remember.read())

        elif 'offline' in query:
            quit()
