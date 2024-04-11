import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  """Converts text to speech"""
  engine.say(text)
  engine.runAndWait()

def get_audio():
  """Listens for user input and returns recognized text"""
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    return text.lower()
  except sr.UnknownValueError:
    print("Sorry, could not understand audio")
    return None

def process_command(text):
  """Processes user commands and provides responses"""
  if "hello" in text:
    speak("Hello! How can I help you?")
  elif "time" in text:
    from datetime import datetime
    now = datetime.now().strftime('%H:%M:%S')
    speak("The time is " + now)
  elif "date" in text:
    from datetime import date
    today = date.today().strftime('%d/%m/%Y')
    speak("Today's date is " + today)
  elif "search" in text:
    search_query = text.split("search for ")[-1]
    speak("Searching the web for " + search_query)
    print("Search results can be found on the web.")
  else:
    speak("Sorry, I can't assist you with that yet.")

print("Assistant is listening...")
while True:
  text = get_audio()
  if text:
    process_command(text)
