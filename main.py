import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


# engine = pyttsx3.init()
# engine.setProperty("rate", 178)
# engine.say("I am the text spoken after changing the speech rate.")
# engine.runAndWait()


Chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(Chrome))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning!sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!sir")
    elif hour >= 18 and hour < 21:
        speak("Good Evening!sir")
    else:
        speak("Good Night!sir")

    speak("I am Jarvis Sir. Please tell me how I can help you")


def takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            keyword = 'JARVIS'
            r.adjust_for_ambient_noise(source)
            print("Listining...")
            speak("Listining...")
            audio = r.listen(source)
  
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if keyword.lower() in query.lower():
            print(f"User said: {query}\n")
            return query
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    speak("Hello sir")
    wishme()

    while True:
        # if 1:

        try:
            query = str(takecommand().lower())

            print('processing...')
            speak('processing...')
            if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
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
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(strTime)

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
                    speak("Sorry. I am not able to send this email")

            elif 'exit' in query:
                exit()
                
            else:
                print('no such command sorry....! try again')
                speak('no such command sorry....! try again')

        except Exception as e:
            # print(e)
            print("Say that again please...")
            speak("Say that again please...")
