import time
from threading import Thread
import pyttsx3
import speech_recognition as sr


class Garvis(Thread):
    # TTS Creation
    @property
    def ttsEngine(self):
        # TTS Engine Init - this one doesn't throw an error, but it won't speak to me.
        self.ttsEngine = pyttsx3.init()
        voices = self.ttsEngine.getProperty('voices')
        self.ttsEngine.setProperty('voice', voices[0].id)

        return self.ttsEngine

    @ttsEngine.setter
    def ttsEngine(self, value):
        self.ttsEngine = value

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        self.speak("Garvis Online")

    def speak(self, text, rate=150):
        self.ttsEngine.setProperty('rate', rate)
        self.ttsEngine.say(text)

    def run(self):
        print('running')
        self.speak("Garvis Online")


Garvis = Garvis()
