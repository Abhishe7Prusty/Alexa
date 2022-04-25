from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

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

    speak("I am Alexa, your personal assistant! How may I help you?")

def takeCommand():
    #takes input command from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sender's email", "your-password")
    server.sendmail("receiver's email", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #uncomment the below line and comment if 1: if you want a continuous conversation with the assistant
    #while True: 
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia")            
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KIIT\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            #the above line contains a path to the application and remember to put an extra slash like this "//"
            os.startfile(codepath)

        elif 'open discord' in query:
            codepath = "C:\\Users\\KIIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord"
            os.startfile(codepath)

        elif 'open canva' in query:
            codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(codepath)

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Abhishek. I am unable to send this email!")

        elif 'bye' or 'exit' or 'quit' in query:
            speak("Goodbye!")
            os._exit(1)

#You can add multiple features to your assistant. Sky is the limit! This code contains the basic functionalities.
