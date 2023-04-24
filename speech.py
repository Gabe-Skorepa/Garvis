import speech_recognition as sr
import pyaudio


class speechRecognition:
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
