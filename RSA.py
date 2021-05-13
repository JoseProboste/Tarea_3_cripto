import sympy
import random

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inversoMod(a, m) :
    for i in range(2, m): 
        if ((a * i) % m == 1): 
            return i

arr_e = []
p = sympy.randprime(0,100)
q = sympy.randprime(0,100)
n=p*q
fi = (p-1)*(q-1)

for i in range(2,fi):
    if mcd(fi,i) == 1:
        arr_e.append(i)

e = random.choice(arr_e)

def inversoMod(a, m) :
    for i in range(2, m): 
        if ((a * i) % m == 1): 
            return i
d = inversoMod(e,fi)

print "p = " + str(p)
print "q = " + str(q)
print "n = " + str(n)
print "fi = " + str(fi)
print "e = " + str(e)
print "d = " + str(d)
print "public key = (" + str(n) +"," + str(e) +")"
print "private key = (" + str(d) +"," + str(p) +","+ str(q) +")"
print "private key = (" + str(n) +"," + str(d) +")"

