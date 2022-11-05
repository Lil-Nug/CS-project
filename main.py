import speech_recognition as sr
import pyttsx3
import webbrowser as wb

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Listening...")
    audio = r.listen(mic, timeout=3, phrase_time_limit=5)

text = r.recognize_google(audio).lower()
print("You said: ", text)

if 'website' in text:
    with mic as source:
        print("Which website would you like to open")
        engine.say("Which website would you like to open")
        audio = r.listen(mic, timeout=3, phrase_time_limit=5)
    url = r.recognize_google(audio).lower()
    print("You said: ", url)
    wb.open(url, new=2)
    engine.say('opening')
    engine.runAndWait()
