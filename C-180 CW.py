from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import subprocess 

root=Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label=Label(root,text="Welcome To Your Personal Desktop Assistant",bg="Light Blue",font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How can I help you...?")
    speech_recognisor=sr.Recognizer()
    with sr.Microphone as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data = speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnknownValueError:
            print('Please repeat I did not get that')
            speak('Please repeat I did not get that')
    respond(voice_data)

def respond(voice_data):
    voice_data= voice_data.lower()
    print(voice_data)
    if"name" in voice_data:
        speak("My name is Trisha")
        print("My name is Trisha")
    if"time" in voice_data:
        speak("Current time is ")
        now = datatime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    if"search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com/")
    if"videos" in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowserr.get().open("https://youtube.com/")
    if"text editor" in voice_data:
        speak("Opening App")
        print("Opening App")
        subprocess.call(["/usr/bin/open","ApplicationsTextEdit.app"])
        
btn = Button(root,text="start",padx=10,pady=1,relief=FLAT,command=r_audio)    
btn.place(relx=0.5,rely=0.5,anchor=CENTER)    
        
r_audio()
oot.mainloop()        
