import datetime
import time
import datetime
import wikipedia
import webbrowser
import os
import datetime
import smtplib
from listen import *
import sys


Chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(Chrome))

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        return("Good Morning!")
    elif hour >= 12 and hour < 18:
        return("Good Afternoon!")
    elif hour >= 18 and hour < 21:
        return("Good Evening!")
    else:
        return("Good Night!")

def wishme(speak):
    print(wish())
    sys.stdout.flush()
    speak(wish())
    time.sleep(2)
    print("I am Jarvis Sir. Please tell me how I can help you")
    sys.stdout.flush()
    speak("I am Jarvis Sir. Please tell me how I can help you")
    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('himeshkumar148@gmail.com', 'mynameisp')
    server.sendmail('aiassistant@gmail.com', to, content)
    server.close()

def function(speak, query):
    if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        sys.stdout.flush()
        speak(results)
        time.sleep(3)

    elif 'open youtube' in query or 'Youtube' in query:
        webbrowser.get('chrome').open("youtube.com")
        print("Opening Youtube")
        sys.stdout.flush()
        speak("Opening Youtube")

    elif 'open google' in query or 'Google' in query:
        webbrowser.get('chrome').open("google.com")
        print("Opening Google")
        sys.stdout.flush()
        speak("Opening Google")

    elif 'open github' in query or 'Github' in query:
        webbrowser.get('chrome').open("github.com")
        print("Opening Github")
        sys.stdout.flush()
        speak("Opening Github")

    elif 'play music' in query:
        music_dir = 'https://www.youtube.com/watch?v=Bqyw-H66gxo'
        songs = os.listdir(music_dir)
        print(songs)
        sys.stdout.flush()
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in query or 'date' in query:
        date = datetime.datetime.now()
        strTime = date.strftime("%I.%M,%p")
        strDate = date.strftime("%A %d %B %Y")
        print(strTime)
        sys.stdout.flush()
        time.sleep(0.5)
        print(strDate)
        sys.stdout.flush()
        speak(f"Sir, the time is {strTime} and the date is {strDate}")

    elif 'open code' in query or 'vs code' in query:
        codePath = "F:\VS CODE\Vs code\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
        print("Opening Code")
        sys.stdout.flush()
        speak("Opening Code")


    elif 'email to Bhavya' in query:
        try:
            speak("What should I say?")
            content = takecommand().lower()
            to = "19bcg1050@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            sys.stdout.flush()
            speak("Sorry. I am not able to send this email")

    elif 'exit' in query or 'stop' in query:
        exit()
        
    else:
        print('no such command sorry....! try again')
        sys.stdout.flush()
        speak('no such command sorry....! try again')
