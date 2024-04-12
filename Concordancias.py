#Las concordacias muestran todas las apariciones de una palabra
#junto con algo del texto que la rodea.
import nltk
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
   texto=archivo.read()
 
tokens=nltk.word_tokenize(texto,"spanish")
texto_nltk=nltk.Text(tokens)
texto_nltk.concordance("internacionales")