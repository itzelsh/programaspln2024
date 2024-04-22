carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(archivo_nombre,"r") as archivo: #r es abrir el archivo modo lectura
  lineas_lista=archivo.readlines()# separa por linea
#print(lineas_lista)

for linea in lineas_lista: # para que salga linea por linea
    print(linea)
  

