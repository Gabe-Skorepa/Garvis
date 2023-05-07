import speech_recognition as sr


class voiceIn:
    # def parseCommand(displayMessages):
    def parseSpeech(self):
        listener = sr.Recognizer()

        print('Listening for a command...')

        with sr.Microphone() as source:
            listener.pause_threshold = 2
            input_speech = listener.listen(source)

            try:
                query = listener.recognize_google(input_speech, language='en-us', with_confidence=False)
                print('Working on what you said...')
                print(f'You said: {query}')
            except Exception as exception:
                print("Sorry, didn't quite catch that")
                print(exception)
                return 'None'
            return query
