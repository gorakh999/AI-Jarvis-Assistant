from espeak import espeak
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', 160)
engine.setProperty('volume', 8)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's Date is ")

    speak(date)
    speak(month)
    speak(year)

def wishMe():
    speak("Welcome")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    time()
    date()
    speak("Jarvis At your Service. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that Again Please...")
        return "None"
    return query

if __name__ == "__main__":
    # wishMe()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("Going Offline")
            quit 