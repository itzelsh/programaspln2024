from gtts import gTTS

texto = "Holaaaaa  profe "
lenguaje = 'es'

audio = gTTS(text = texto, lang = lenguaje, slow = False)
audio.save('audio.mp3')

print("Proceso Terminado")