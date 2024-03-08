
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
    #sirve para sustituir las comillas
simbolos=["(",")",",",".",";",":","\""]
for simbolo in simbolos:
    
    
    texto=texto.replace(simbolo," " + simbolo + " ")
palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
 print(palabra)