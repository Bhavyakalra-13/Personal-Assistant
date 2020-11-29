from datetime import date
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

def wishme(speak):
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning!sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!sir")
    elif hour >= 18 and hour < 21:
        speak("Good Evening!sir")
    else:
        speak("Good Night!sir")

    print("I am Jarvis Sir. Please tell me how I can help you")
    sys.stdout.flush()
    speak("I am Jarvis Sir. Please tell me how I can help you")
    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
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

    elif 'open youtube' in query:
        webbrowser.get('chrome').open("youtube.com")

    elif 'open google' in query:
        webbrowser.get('chrome').open("google.com")

    elif 'open github' in query:
        webbrowser.get('chrome').open("github.com")

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
        print(strDate)
        sys.stdout.flush()
        speak(f"Sir, the time is {strTime} and the date is {strDate}")

    elif 'open code' in query:
        codePath = "F:\VS CODE\Vs code\Microsoft VS Code\Code.exe"
        os.startfile(codePath)

    elif 'email to Bhavya' in query:
        try:
            speak("What should I say?")
            content = takecommand()
            to = "harryyourEmail@gmail.com"
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
