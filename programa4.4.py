import os 
carpeta_nombre="Documentos\\"
archivos_lista=os.listdir(carpeta_nombre)# os contitene instrucciones del sistema operativo y listdir es para mostrar el directorio 
for archivo_nombre in archivos_lista:
    print(archivo_nombre)