import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data=r.record(source , duration=5)
    audio = r.listen(source)
    print("Dinliyorum")
    text = r.recognize_google(audio, language='tr-tr')
    print(text)


