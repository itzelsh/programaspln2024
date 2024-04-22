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

#Aqui, nuestra lista de tokens se llama "tokens"
tokens_conjunto=set(tokens)

palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)

riqueza_lexica=palabras_diferentes/palabras_totales
print(riqueza_lexica)
#Si funciona