# Importando a biblioteca!
from vosk import Model, KaldiRecognizer
import os
import pyaudio

# Modelo de voz que sera usado (PT-BR/INGLES)
model = Model('model')  # Acesse a documentacao do vosk e baixe os modelos de voz (Link para pegar os modelos de voz(https://alphacephei.com/vosk/models))
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())