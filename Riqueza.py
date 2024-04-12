import nltk
def riqueza_lexica(tokens):

 tokens_conjunto=set(tokens)
 palabras_totales=len(tokens)
 palabras_diferentes=len(tokens_conjunto)
 riqueza_lexica=palabras_diferentes/palabras_totales
 return riqueza_lexica
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
 texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print(riqueza_lexica)

# Aquí, nuestra lista de tokens se llama "tokens"
conteo_individual=tokens.count("a")
print(conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print(porcentaje," %")

#con este programa se saca el porcetajee