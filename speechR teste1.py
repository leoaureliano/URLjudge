#organizando as ideias, ela tem que ter um reconhecimento de voz e uma lista do que responder e  do que perguntar  (etapa2) e
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone() as mic:
       
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print("Recognized {"text"})


    except: speech_recognition.speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
