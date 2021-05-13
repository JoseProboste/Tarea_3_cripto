print "ingrese la llave privada"

n = input("Ingrese n: ")
d = input("Ingrese d: ")
c = input("Ingrese el mensaje cifrado: ")
m = pow(c,d,n)
print("----------------------")
print "mensaje descifrado: " + str(m)
print("----------------------")