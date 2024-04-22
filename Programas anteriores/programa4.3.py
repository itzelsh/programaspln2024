carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"

with open(archivo_nombre,"r") as archivo: #r es abrir el archivo modo lectura
  lineas_lista=archivo.readlines()# separa por linea
#print(lineas_lista)
num_linea=1
for linea in lineas_lista: # para que salga linea por linea
    if linea.strip()=="": # strip es para identificar las lineas vacias y omitirlas 
        continue #continue es para continuar con la siguientes linea, permite que siga ejucutando
    print("Linea",num_linea,":",linea)
    num_linea=num_linea+1