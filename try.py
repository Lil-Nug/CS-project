import webbrowser as wb
import pyttsx3
engine = pyttsx3.init()
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))

voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[1].id)
engine.say('')
engine.runAndWait()
