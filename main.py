import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
from pic import *
from news import *
from mail import *
from weather import *
from selenium_web import *

def talk(sound):
    print(sound)
    speaker.say(sound)
    speaker.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk("listening")
            listener.energy_threshold=10000
            listener.adjust_for_ambient_noise(source,1.2)
            voice=listener.listen(source)
            audio=listener.recognize_google(voice)
            print(audio)

    except:
        pass

    return audio.lower()

def run_jarvis():
    command=take_command()
    if 'play' in command:
        pywhatkit.playonyt(command)
    elif 'website' in command:
        command=command.replace('website','')
        pywhatkit.search(command)
    elif 'time' in command:
        talk('The currernt time is  ' + datetime.datetime.now().strftime('%I:%M:%p'))
    elif 'date' in command:
        talk('Today is '+ datetime.datetime.now().strftime('%d :%B')+' of '+ datetime.datetime.now().strftime('%Y'))
    elif 'weather' in command:
        w=temp()
        talk("the current temperature is "+w)
    elif 'search' in command:
        data=wikipedia.summary(command,1)
        talk(data)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'about' in command:
        command=command.replace('about','')
        assist=infow()
        assist.get_info(command)
    elif 'fat' in command:
        x=randfacts.getFact()
        talk('did you know ' + x)
    elif 'news' in command:
        arr=news()
        for i in range(len(arr)):
            talk(arr[i])
    elif 'email' in command:
        talk("to whom you want to send email ")
        name=take_command()
        rcvr=email_list[name]
        print(rcvr)
        talk("what is the subject of your email")
        sub=take_command()
        talk("what is the content")
        msg=take_command()
        send_email(rcvr,sub,msg)
        talk("successfully send the mail")
    elif 'capture' in command:
        shot=take_pic()
        talk('successfully captured you. Do you want your sketch?')
        reply=take_command()
        if 'yes' in reply:
            shot1=get_sketch()
    else:
        talk("sorry I didn't understand you. Say it again please.")

speaker=pyttsx3.init()
speaker.setProperty('rate',130)
#voices=speaker.getProperty('voices')
#speaker.setProperty('voice',voices[1].id)
listener=sr.Recognizer()
hour=int(datetime.datetime.now().hour)
if hour>0 and hour<12:
    talk("Good morning")
elif hour>12 and hour<16:
    talk("Good afternoon")
else:
    talk("Good evening")
#talk("please tell me your name so that i could recognize you")
#boss=take_command()
#if 'Alpha' in boss:
#   talk('hello my love. I am your voice assistant Jarvis. How can i help you')
#else:
#    talk('How can i help you')
run_jarvis()