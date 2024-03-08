c="c:\\Users\\Carmen\\Documents\\FIME\\optativa\\" #carpeta donde esta el documento
e="Competencias específicas.txt" #documento que vamos a llamar
s="archivo_text.txt"#archivo que no existe que se va a crear
 
with open(c+s,"r") as archivo:#otra forma de abrir el archivo y leerlo
    texto=archivo.read()
print(texto)

palabra=input("Escribe la palabra a buscar:")
#print(texto)
if palabra in texto:
    print("La palabra fue encontrada")
else:
    print("Palabra no encontrada ")
