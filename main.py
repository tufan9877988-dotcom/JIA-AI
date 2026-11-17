import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language='hi-IN')
        except:
            return ""

speak("नमस्ते, मैं आपकी क्या मदद कर सकता हूँ?")

while True:
    question = listen()
    if not question:
        continue
    print(f"You: {question}")
    
    if "exit" in question.lower() or "quit" in question.lower():
        speak("अलविदा!")
        break
        
    response = f"आपने कहा: {question}"
    print(f"JIA: {response}")
    speak(response)

