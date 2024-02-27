import re
carpeta_nombre="Documentos\\"
archivo_nombre="archivo_text.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo: #la va busar como expresion por la r
      texto=archivo.read()
expresion_regular=re.compile(r"redes") 
resultado_busqueda=expresion_regular.search(texto) #search va mostrar la primera coincidencia que encuentre  solo una 
print(resultado_busqueda.group(0)) 
#expresion_regular=re.compile(r"redes*")  #el asterisco permite cualquier cantidad de repeticiones del simbolo que lo precede
#expresion_regular=re.compile(r"s+") el mas muestra todas las letras de eso
#expresion_regular=re.compile(r"$") $ el final de la lineaexpresion_regular=re.compile(r"^redes")/*}
#resultados_busqueda=expresion_regular.finditer(texto)#finditer encontrar la palabra que se replite en el texto en encuentra todas las coincidencias

#for resultado in resultado_busqueda:#para usar finditer se ocupa un bucle
 # print(resultado.group(0))
    