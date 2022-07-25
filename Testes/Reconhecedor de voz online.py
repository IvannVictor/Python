# Importando a biblioteca!
import speech_recognition as sr

# Criando receptor de audio!
r = sr.Recognizer()

# Abrindo o microfone para captar o audio!
with sr.Microphone() as mi:
   while True:
        audio = r.listen(mi)  # Vai usar o microfone como fonte de audio!
        print(r.recognize_google(audio, language='pt'))

# Obs: Como ele faz o reconhecimento de forma online, pode ser que demore um pouco para aparecer o que voce falou na tela!
# A biblioteca vai entra no google e fazer o reconhcimento apartir do seu microfone e demora um pouco para trazer as respostas!