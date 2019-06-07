import speech_recognition as sr
from gtts import gTTS
import os
import time as t
import csv
import random as ran
import geocoder as geo
from PyDictionary import PyDictionary as dicti
import pyautogui
import webbrowser
d=["Hi","Hey","Whats up","Hello"]
r=sr.Recognizer()
r.energy_threshold=2800
file='venesa.csv'
venesa1=[]
def voice(x):
    tts=gTTS(text=x,lang='en')
    tts.save("veneesaa.mp3")
    os.system("veneesaa.mp3")
    t.sleep(5)
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(1350, 12)
    pyautogui.click()
    
def dictionary1(value):
    mean=dicti.meaning(value)
    meaning=mean["Noun"][0]
    print(meaning)
    voice(meaning)
    
    
def web(y):
    url="https://www.google.co.in/search?q="+y
    webbrowser.open_new(url)

def loca():
    g=geo.ip('me')
    la=g.lat
    longni=g.lng
    ge=geo.google([la,longni],method='reverse')
    print(la,longni)
    c=ge.city
    s=ge.state_long
    comb=(c+s)
    print(comb)
    voice(comb)
while(1):
    with sr.Microphone() as source:
        print("Say something.......")
        audio=r.listen(source,phrase_time_limit=5)   #listen for 5 secs
        cmd=r.recognize_google(audio)
        print(cmd)
        cmd1=cmd.split()
        if(cmd=="go to sleep") :
            voice("Thank you sir ")
        if(cmd=="hey Vanessa"):
            ra=ran.randint(0,3)
            p=d[ra]
            voice(p)
            print(d[ra])
        for i in range (len(cmd1)):
            if(cmd1[i]=="meaning"):
                dictionary1(cmd1[-1])
            if(cmd1[i]=="Search"):
                web(cmd1[-1])
            if(cmd1[i]=="place" or cmd[i]=="where"):
               loca()            
        
    
    try:
        print("You said "+cmd)
    except sr.UnkonwnValueError:
        print("Could not understand your speech")
    except sr.RequestError:
        print("Could not request from google")
    '''with open(file,'r') as file:
        a=csv.DictReader(file)
        for i in (a):
            venesa1.append(a)'''
    
    
    
