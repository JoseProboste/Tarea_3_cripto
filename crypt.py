print "ingrese la llave publica"

n = input("Ingrese n: ")
e = input("Ingrese e: ")
m = input("Ingrese el mensaje: ")
c = pow(m,e,n)
print("----------------------")
print "mensaje cifrado: " + str(c)
print("----------------------")