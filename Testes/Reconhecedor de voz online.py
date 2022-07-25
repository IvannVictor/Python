# Importando a biblioteca!
import speech_recognition as sr

# Criando receptor de audio!
r = sr.Recognizer()

# Abrindo o microfone para captar o audio!
with sr.Microphone() as mi:
    while True:
        audio = r.listen(mi)  # Vai usar o microfone como fonte de audio!
        print(r.recognize_google(audio, language='pt'))