import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
 texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
 print(token)
 
# Aquí, nuestra lista de tokens se llama "tokens"
palabras_total=len(tokens)

print(palabras_total)

print(palabras_total)
