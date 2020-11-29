import speech_recognition as sr
from speak import speak
import sys

def takecommand():
    try:
        print("Listining...")
        sys.stdout.flush()
        speak("Listining...")
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            keyword = 'JARVIS'
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) 
            
        
        query = r.recognize_google(audio, language='en-in')
        
        if keyword.lower() in query.lower():
            print(query)
            sys.stdout.flush()
            return query

    except Exception as e:
        print("Say that again please...")
        sys.stdout.flush()
        speak("Say that again please...")