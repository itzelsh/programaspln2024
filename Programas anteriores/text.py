import nltk
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)