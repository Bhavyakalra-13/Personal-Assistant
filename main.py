import pyttsx3
import speech_recognition as sr
import datetime



# engine = pyttsx3.init()
# engine.setProperty("rate", 178)
# engine.say("I am the text spoken after changing the speech rate.")
# engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am Jarvis Sir. Please tell me how I can help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # r.pause_threshold = 1
        
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 
    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None"
    return query


if __name__=="__main__" :
    speak("Hello sir")
    wishme()
    takecommand()