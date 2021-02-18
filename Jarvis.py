import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[2].id)
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Mr.Darshan")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr.Darshan")
    else:
        speak("Good Evening Mr.Darshan")

    speak("I'm Jarvis Sir. Please tell me how may I help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('darshanagrawal007@gmail.com','121997@dax')
    server.sendmail('darshanagrawal007@gmail.com',to,content)
    server.close()


if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.get()
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("www.facebook.com")
        
        elif "play music" in query:
            speak("Playing a Song")
            music_dir='H:\\mmmmm'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open V.S code" in query:
            speak("Opening Visual Studio Code")
            codePath="C:\\Users\\MY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to' in query:
            try:
                speak("what should i say?") 
                content=takeCommand()
                to="daxagrawal.da@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry Mr.Darshan. I am not able to send this email")
        elif 'how are you' in query:
                speak("I am very good Sir and what about you?")
        elif 'what do you think about me' in query:
                speak("You are Best Person I have ever Met Mr.Darshan")
        elif 'thank you' in query:
                speak("My Pleasure Sir")
        