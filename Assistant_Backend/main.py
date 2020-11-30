from speak import speak
from function import *
import time
import sys
import os

id = os.getpid()

stop=open("id.txt", "w")
stop.write(str(id))
stop.close()


def main():
    print("Welcome sir!")
    sys.stdout.flush()
    speak("welcome sir")
    time.sleep(1)
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

main()