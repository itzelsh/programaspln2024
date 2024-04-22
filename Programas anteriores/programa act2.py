print("Universidad de Colima")
print("Ingenieria en Computacion Inteligente")
Nombre="Carmen Itzel Chavez Rodriguez"
print("Hola",Nombre)
edad= input("Escribe tu edad:")
print(Nombre,"Tiene la edad de:",edad)
print("operacion1:",4*5-6)
x=4+7
y=x-2
z=x+y
print("x=",x)
print("y=",y)
print("z=",z)
archivo_abierto=open("c:\\Users\\Carmen\\Documents\\fime.txt","w")
archivo_abierto.write("Esto se escribe en el archivo\n")
archivo_abierto.write("Esto tambien\n")
archivo_abierto.write("Mira, puedo escribir\"comillas\"\n")
archivo_abierto.write("Gracias a la diagonal invertida:  \n")
archivo_abierto.close()

archivo_abierto=open("c:\\Users\\Carmen\\Documents\\fime.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()
 