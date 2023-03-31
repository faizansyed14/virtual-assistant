from abc import update_abstractmethods
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
from wikipedia.wikipedia import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good morning sir!")

    elif hour>=12 and hour<18:
        speak("Good after noon sir!")

    else:
        speak("Good evening sir!") 

    speak("Iam rock. How may I help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("slow internet connection...")
        return"none"
    return query


if __name__ == "__main__":
  wishme()
while True:
# if 1:
    query = takecommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif'open youtube' in query:
        webbrowser.open("youtube.com")

    elif'open google' in query:
        webbrowser.open("google.com")  

    elif'play some music' in query or 'any song' in query:

        speak("ok sir ")
        music_dir='C:\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[1]))

    elif 'how are you' in query:
            speak("I am fine")
            speak("How are you Sir")
 
    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            

    elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H%M")
         speak(f"sir, the time is{strTime}")

    elif 'open vs code' in query:
        codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'open my trip video' in query:
        tripvideo="C:\\Users\\hp\\Videos\\trip video"
        os.startfile(tripvideo)

    elif 'check my youtube channel' in query:
        youtubechannel="https://www.youtube.com//channel//UCcFc1xfh1mT4H5vwkD3JhNA"
        os.startfile(youtubechannel)
        speak("congratulactions sir,we have crosed 18k subscribers and more to go!")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()

     
    elif 'open my linkedin account'in query:
        linkedin="https://www.linkedin.com/in/syed-faizan-uddin-563187225/"
        os.startfile(linkedin)   

    elif 'any joke' in query:
        speak(pyjokes.get_joke())
 
    elif 'what is love' in query:
        speak("It is 7th sense that destroy all other senses")
 
    elif "who are you" in query:
        speak("I am your virtual assistant created by faizan")

    elif 'who created you' in query:
        speak("sir iam Rock,I was created by faizan,he is the man behinde my intelligence")
    
    

    
