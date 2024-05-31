import tkinter as tk
import os

def abrir_script(script):
    os.system(f"python {script}.py")

root = tk.Tk()
root.title("Aplicaciones de Procesamiento de Lenguaje Natural")
root.geometry("400x600")

label = tk.Label(root, text="¿Qué deseas hacer?")
label.pack()

button1 = tk.Button(root, text="Convertir texto a audio", command=lambda: abrir_script("word"))
button1.pack()

button2 = tk.Button(root, text="Convertir audio a texto", command=lambda: abrir_script("mundo"))
button2.pack()

button3 = tk.Button(root, text="Reproducir audio y convertirlo a texto", command=lambda: abrir_script("texto_a_audio"))
button3.pack()

button4 = tk.Button(root, text="Iniciar chat con GPT", command=lambda: abrir_script("prog4"))
button4.pack()

button5 = tk.Button(root, text="Convertidor de Audio-Texto-Audio", command=lambda: abrir_script("progr6"))
button5.pack()

button6 = tk.Button(root, text="Convertir el texto de un archivo txt o Word a audio y reproducirlo", command=lambda: abrir_script("chat"))
button6.pack()

button7 = tk.Button(root, text="Programa en Python que realiza la función de chat GPT", command=lambda: abrir_script("senti"))
button7.pack()

button8 = tk.Button(root, text="Análisis de Sentimientos con SentimentIntensityAnalyzer()", command=lambda: abrir_script("chuking"))
button8.pack()

button9 = tk.Button(root, text="Chunking: Identificar frases sustantivas, verbales, etc., en un texto", command=lambda: abrir_script("identifica"))
button9.pack()

button10 = tk.Button(root, text="Análisis de un archivo de texto, PDF o Word", command=lambda: abrir_script("backend"))
button10.pack()

button11 = tk.Button(root, text="Salir", command=root.quit)
button11.pack()

root.mainloop()
