import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User Said: {statement}\n")

        except Exception as e:
            speak("Could you please say that again !")
            return "None"
        return statement

wishMe()
print("I am your Personal Assistant Jingle Bell")
speak("I am your Personal Assistant Jingle Bell")
speak("Say me, How can I Help you ?")

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('See you later !!')
            print('See you later !!')
            break

        if 'wikipedia' in statement:
                    speak('Searching Wikipedia...')
                    statement =statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    break

        elif 'open youtube' in statement:
                    speak('Opening...')
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(1)
                    break

        elif 'open google' in statement:
                    speak('Opening...')
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(1)

        elif 'open gmail' in statement:
                    speak('Opening...')
                    webbrowser.open_new_tab("gmail.com")
                    speak("Google Mail open now")
                    time.sleep(1)
                    break
               
        elif 'time' in statement or "what is the time" in statement:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                    break

        elif 'news' in statement:
                    news = webbrowser.open_new_tab('https://www.hindustantimes.com')
                    speak('Here are some headlines from the Hindustan Times, Happy reading')
                    time.sleep(1)
                    break

        elif "camera" in statement or "take a photo" in statement:
                    ec.capture(1,"robo camera","img.jpg")
                    break


        elif 'search'  in statement:
                    statement = statement.replace("search", "")
                    webbrowser.open_new_tab(statement)
                    time.sleep(1)	
                    break


        elif 'ask' in statement:
                    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                    question=takeCommand()
                    app_id="Paste your unique ID here "
                    client = wolframalpha.Client('54HT42-Q7GQYX6UTW')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)
                    break


        elif 'who are you' in statement:
                    speak('I am Jingle Bell version 3 point O your personal assistant')
                    

        elif 'what can you do' in statement:
                    speak('I am programmed to do minor tasks like opening youtube, google chrome, gmail and stackoverflow , predict time,'
                          'take a photo, search wikipedia, predict weather in different cities, get top headline news from Hindustan Times,' 
                          'and you can ask me computational or geographical questions too !')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I was built by Team-14")
                    print("I was built by Team-14")


        elif "weather" in statement:
                    api_key="Apply your unique ID"
                    base_url="https://api.openweathermap.org/data/2.5/weather?"
                    speak("what is the city name")
                    city_name=takeCommand()
                    complete_url=base_url+"appid="+api_key+"&q="+city_name
                    response = requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        current_temperature = y["temp"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" Temperature in kelvin unit is " +
                            str(current_temperature) +
                            "\n humidity in percentage is " +
                            str(current_humidiy) +
                            "\n description  " +
                            str(weather_description))
                        print(" Temperature in kelvin unit = " +
                            str(current_temperature) +
                            "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                            "\n description = " +
                            str(weather_description))


        elif "log off" in statement or "sign out" in statement:
                    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])
                    
        time.sleep(1)
