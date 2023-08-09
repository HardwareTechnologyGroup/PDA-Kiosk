import tkinter as tk
import pyttsx3

# import pyttsx3
#
# engine = pyttsx3.init()
# engine.say('Please enter your account number and password ')
# engine.say('Thank you')
# # engine.runAndWait()

# pyobj=pyttsx3.init()
#
#
# fo=open("D:\CDAC\Voice.txt","r")
# ip=fo.read()
# fo.close()
# pyobj.say(ip)
# pyobj.runAndWait()
#
#
# pyobj=pyttsx3.init()
# fo=open("D:\CDAC\Voice1..txt","r")
# ip=fo.read()
# fo.close()
# pyobj.say(ip)
# pyobj.runAndWait()
#
#
#
# pyobj=pyttsx3.init()
# fo=open("D:\CDAC\Voice2..txt","r")
# ip=fo.read()
# fo.close()
# pyobj.say(ip)
# pyobj.runAndWait()



def text_to_speech():
    msg = "Hello there"
    speech = gTTS(text=msg)
    speech.save("msg.mp3")
    playsound("msg.mp3")
