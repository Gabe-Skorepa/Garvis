from threading import Thread
import pyttsx3

ttsEngine = pyttsx3.init()


def _ttsEngine():
    voices = ttsEngine.getProperty('voices')
    ttsEngine.setProperty('voice', voices[0].id)


def speak(text, rate=150):
    ttsEngine.setProperty('rate', rate)
    ttsEngine.say(text)
    ttsEngine.runAndWait()


class Garvis(Thread):
    _ttsEngine()

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        speak('Garvis Online')


Garvis()
