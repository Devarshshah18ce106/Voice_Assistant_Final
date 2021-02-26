import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time #   timer
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib
from tkinter import *
from tkinter import ttk
from pyowm import OWM #weather
import requests
from bs4 import BeautifulSoup #for news


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("I am Tom. Please tell me how may I help you")
    speak("I am Tom. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        # speak("sorry i didnt get it. Say that again please")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    key = '1'

    def gui():
        root = Tk()
        b1 = ttk.Button(root, text="click here for next command", command=label)
        b1.pack()
        mi=PhotoImage(file="C:\\Users\\LENOVO\\PycharmProjects\\untitled5\\mic.png")
        b1.config(image=mi)
        tmi=mi.subsample(2,2)
        b1.config(image=tmi)
        root.mainloop()


    def label():

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('ok, opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('ok, opening google')
            webbrowser.open("google.com")

        elif 'drive'in query:
            query = query.replace("drive", "")
            query = query.replace("open", "")
            query=query.replace(" ", "")
            speak(f'ok, opening {query} drive')
            print(f'ok, opening {query} drive')
            a=":"
            path = "{}{}\\".format(query,a)

            print(path)



            os.startfile(path, "open")

        elif 'open stackoverflow' in query:
            speak('ok, opening stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'play' in query:
                speak('ok, the results are')
                query = query.replace("play ", "")
                query = query.replace(" song", "")
                query = query.replace(" ", "+")
                webbrowser.open("youtube.com/results?search_query={}".format(query))
        elif 'timer' in query:

            query = query.replace("start timer of ", "")
            query = query.replace(" seconds", "")
            boom = int(query)
            while boom > 0:
                time.sleep(1)
                print(boom)
                boom -= 1
            print("countdown over")
            speak("countdown over")

        elif 'cd' in query:
            speak('please place the disc')
            os.startfile("D:", "open")

        elif 'start music' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\my music'
            songs = os.listdir(music_dir)
            i=0
            for x in songs:
                print(i ,"  ", x)
                i+=1
            s=random.randint(0,9)
            print("playing ",s,songs[s] )
            os.startfile(os.path.join(music_dir, songs[s]))

        elif 'choice' in query:
            music_dir = 'C:\\Users\\LENOVO\\Desktop\\my music'
            songs = os.listdir(music_dir)
            i=0
            for x in songs:
                print(i, "  ",  x)
                i += 1
            speak("please speak the number of track")
            query = takeCommand().lower()
            i= int(query)
            print("playing ",i ,songs[i] )
            os.startfile(os.path.join(music_dir, songs[i]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%x")
            print(strTime)
            speak(f"Sir todays date is {strTime}")

        elif ' day' in query:
            strTime = datetime.datetime.now().strftime("%A")
            print(strTime)
            speak(f"Sir todays day is {strTime}")

        elif 'month' in query:
            strTime = datetime.datetime.now().strftime("%B")
            print(strTime)
            speak(f"Sir this month is {strTime}")

        elif 'weather' in query:
            query = query.replace("what is the weather in ", "")
            query = query.replace(" ", "")

            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(query)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            print(
                'The current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                    query, k, x['temp_max'], x['temp_min']))
            speak(
                'The current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                query, k, x['temp_max'], x['temp_min']))

        elif "today's news" in query:



            def print_headlines(response_text):
                count = 1
                soup = BeautifulSoup(response_text, 'lxml')
                headlines = soup.find_all(attrs={"itemprop": "headline"})
                for headline in headlines:
                    if count<7:

                        print(headline.text)
                        speak(headline.text)
                        count=count+1

            url = 'https://inshorts.com/en/read'
            response = requests.get(url)

            print_headlines(response.text)


        elif "headlines" in query:

            def print_headlines(response_text):
                count = 1
                soup = BeautifulSoup(response_text, 'lxml')
                headlines = soup.find_all(attrs={"itemprop": "headline"})
                for headline in headlines:
                    if count < 7:
                        print(headline.text)
                        speak(headline.text)
                        count = count + 1

            url = 'https://inshorts.com/en/read'
            response = requests.get(url)

            print_headlines(response.text)
        # var1 = ['who made you', 'who created you']
        # var2 = ['I_was_created_by_yash and devarsh.', 'yash and devarsh']
        elif "who created you" in query:


            # elif r.recognize_google(audio) in var1:
            print("I was created by yash and devarsh")
            speak("I was created by yash and devarsh")


        elif 'open netbeans' in query:
            speak("opening netbeans")
            codePath ="C:\\Program Files\\NetBeans 8.2\\bin\\netbeans.exe"
            os.startfile(codePath)
        # elif 'open camera' in query:
        #       codePath ="C:\\Program Files (x86)\\CyberLink\\YouCam"
        #       os.startfile(codePath)

        elif 'who are you' in query:
            speak("I am Tom , speed 1 tera hertz,   memmory 1 zeta bytes")

    label()
    gui()
