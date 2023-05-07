from threading import Thread
import pyttsx3
import time
import commandInput


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

        # Begin TTS / "Boot Garvis" on the front of what an end user should get here.
        self._ttsVoice()
        print("Garvis Online.")
        self.speak('Garvis Online')
        self.speak("How are you sir?", rate=200)

    def run(self):
        while True:
            commandInput.commandInput().parseCommand()


Garvis().run()
