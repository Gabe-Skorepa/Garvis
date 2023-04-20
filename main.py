import pyttsx3
import speech_recognition as sr

# Creating the main speech engine brain of Garvis as a whole
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# TTS Creation
def speak(text, rate=150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


# Making this thing be able to take in commands
def parseCommand(displayMessages):
    listener = sr.Recognizer()

    if displayMessages:
        print('Listening for a command...')

        with sr.Microphone() as source:
            listener.pause_threshold = 1
            input_speech = listener.listen(source)

            try:
                query = listener.recognize_google(input_speech, language='en-us', with_confidence=False)
                if displayMessages:
                    print('Working on what you said...')
                    print(f'You said: {query}')
            except Exception as exception:
                if displayMessages:
                    print("Sorry, didn't quite catch that")
                    print(exception)
                    return 'None'
            return query


# ah, the good ol main function.
def main():
    if __name__ == '__main__':
        print('Garvis Online')
        speak('Garvis Online')


main()
