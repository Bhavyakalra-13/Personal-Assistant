from speak import speak
from function import *
import time
import sys

# text = sys.argv[1]

if __name__ == "__main__":
    speak("welcome sir")
    wishme(speak)
    

    while True:
        try:
            
            query = str(takecommand().lower())
            
            print("ok sir!")
            sys.stdout.flush()
            speak("ok sir!")
            print('processing...')
            sys.stdout.flush()
            speak('processing...')
            function(speak, query)
            time.sleep(2)
            print("your next command sir")
            sys.stdout.flush()
            speak("your next command sir")
            time.sleep(1)
            
        except Exception as e:
            print("Say that again please...")
            sys.stdout.flush()
            speak("Say that again please...")
