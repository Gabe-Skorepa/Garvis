from threading import Thread
import pyttsx3


class Garvis(Thread):
    # INIT TTS ENGINE
    ttsEngine = pyttsx3.init()

    # TTS ENGINE VOICE SETTINGS
    def _ttsVoice(self):
        voices = self.ttsEngine.getProperty('voices')
        self.ttsEngine.setProperty('voice', voices[0].id)

    # TTS SPEECH COMMAND
    def speak(self, text, rate=150):
        self.ttsEngine.setProperty('rate', rate)
        self.ttsEngine.say(text)
        self.ttsEngine.runAndWait()

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        self._ttsVoice()
        print("Garvis Online.")
        self.speak('Garvis Online')


Garvis()
