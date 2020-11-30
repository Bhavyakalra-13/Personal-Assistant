import speech_recognition as sr
import sys

def takecmd():
    try:        
        res = sr.Recognizer()
        with sr.Microphone() as src:
            res.adjust_for_ambient_noise(src)
            ad = res.listen(src) 
        q = res.recognize_google(ad, language='en-in')
        return q
    except Exception as e:
        print("Say that again please...")
while True:
    print (takecmd())
    sys.stdout.flush()
