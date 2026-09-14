import pyttsx3
voice=pyttsx3.init()
voice.setProperty("rate",200)
voice.setProperty("volume",1)
voice.say("Hello bhai, kaise ho?")
voice.runAndWait()