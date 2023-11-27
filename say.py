#스피커
import os
def say(text) :
    os.system("espeak -v ko + f3" + text)