import pyttsx3
text_speech = pyttsx3.init()
corpus = "Please speak up"
text_speech.say(corpus)
text_speech.runAndWait()