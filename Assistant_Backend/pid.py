import os
import sys
import signal

file = open("id.txt", "r")
pid = file.readline()
print("Program Terminated")
sys.stdout.flush()
os.kill (int(pid),signal.SIGTERM)