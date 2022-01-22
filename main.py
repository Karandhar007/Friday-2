#1
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os

#2
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newvoicerate = 180
engine.setProperty('rate', newvoicerate)

#3
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#4
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("THE CURRENT TIME IS")
    speak(Time)
def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("THE CURRENT DATE IS")
    DD = ["IT", "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH", "NINTH", "TENTH",
          "ELEVENTH", "TWELVETH", "THIRTEENTH", "FOURTEENTH", "FIFTEENTH", "SIXTEENTH", "SEVENTEENTH", "EIGHTEENTH",
          "NINETEENTH", "TWENTIETH", "TWENTY FIRST", "TWENTY SECOND", "TWENTY THIRD", "TWENTY FOURTH", "TWENTY FIFTH",
          "TWENTY SIXTH", "TWENTY SEVENTH", "TWENTY EIGHTH", "TWENTY NINTH", "THIRTIETH", "THIRTY FIRST"]
    speak(DD[Date])
    MM = ["IT", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER",
          "NOVEMBER", "DECEMBER"]
    speak(MM[Month])
    speak(Year)

#5
def greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("GOOD MORNING")
    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON")
    elif hour > + 18 and hour <= 24:
        speak("GOOD EVENING")
    speak("WELCOME BACK BOSS!")
    speak("HOW MAY I HELP YOU TODAY?")

#6
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("ARE YOU SAYING SOMETHING?")
        speak("IF YES , SAY THAT AGAIN PLEASE or DO YOU WANT ME TO GO OFFLINE?")
        return "NONE"
    return query

#DRIVER
if __name__ == "__main__":
    greet()
    while True:
        query = takecommand().lower()

        if "time" in query and "wikipedia" not in query:
            time()
        elif "your" and "name" in query :
            speak("my name is FRIDAY ; i am your assistant")
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("okay;going offline")
            quit()
        elif "wikipedia" in query:
            speak("SEARCHING...")
            try :
                query = query.replace("Wikipedia", "")
                query = query.replace("wikipedia", "")
                print(query)
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except :
                speak("THis page does not exsists , try being more specific")
        elif "open browser" in query :
            speak("what do you want me to search for ?")
            path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takecommand().lower()
            wb.get(path).open_new_tab(search+".com")

        #elif "logout" in query :
        #    os.system("shutdown -1")
        #elif "shutdown" in query :
        #    os.system("shutdown /s /t 1")
        #elif "restart" in query :
        #    os.system("shutdown /r /t 1")

        elif "play songs" in query :
            songsdir = "E:\The G.O.A.T\Eminem - Kamikaze (2018) Mp3 (320kbps) [Hunter]\Eminem - Kamikaze (2018)"
            songs = os.listdir(songsdir)
            os.startfile(os.path.join(songsdir,songs[0]))

        elif "remind me" in query :
            speak("what should i remember?")
            data = takecommand()
            rem = open("data.txt","w")
            rem.write(data)
            rem.close()

        elif "did i ask you to remember something" in query :
            rr = open("data.txt","r")
            speak("you said me" + rr.read())

