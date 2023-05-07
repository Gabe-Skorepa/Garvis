import speech_recognition as sr
import time


def callback(recognizer, audio):
    try:
        print("You Said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("I didn't quite catch that...")
    except sr.RequestError as e:
        print("Couldn't request results from Google Speech Service".format(e))


class backgroundListener:
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)

    stopListening = r.listen_in_background(m, callback)

    for _ in range(50): time.sleep(0.1)
