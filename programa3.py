c= "c:\\Users\\Carmen\\Documents\\FIME\\optativa\\" #carpeta donde esta el documento
e="Competencias específicas.txt" #documento que vamos a llamar
s="archivo_text.txt"#archivo que no existe que se va a crear 
#leer archivos y abrirlos
e2=open(c+e,"r")
#print(e2.read())

s2=open(c+s,"w")#pasamos toda la informacion del archivo viejo  al nuevo archivo 
t=e2.read()
t2=t
s2.write(t2)

e2.close()
s2.close()

s3=open(c+s,"r")
print(s3.read())#se vuelve abrir el archivo nuevo para ver que informacion se agrego
s3.close()
