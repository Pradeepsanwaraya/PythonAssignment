import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("rate", 150)

if len(voices) > 0:
    engine.setProperty("voice", voices[0].id)

engine.say("This is a Python text to speech example.")
engine.runAndWait()

print("Speech completed")
