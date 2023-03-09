# programa para hallar las raíces de una función cuadrática
import math
print("-------------------------------------")
print("---raices de la funcion cuadratica---")
print("-------------------------------------")

# input

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))

#procesing 

d = (b**2)-(4*a*c)

if (d == 0):
    x = -b/2*a
#output
    print(str("las dos raices son: " + str(x)))
else:
    if (d<0):
#output
        print(str(" son raices imaginarias "))
    else:
        x2 = (-(b)+(math.sqrt(d)))/(2*a)
        x1 = (-(b)-(math.sqrt(d)))/(2*a)
#output
        print(str("las raices son: "+" x1: "+ str(x1)+" x2: " + str(x2)))