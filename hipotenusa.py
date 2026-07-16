import math

cateto1 = float(input("Ibtroduce el primer cateto: "))
cateto2 = float (input("Introduce el segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print ("La hipotenusa del triangulo es: ", hipotenusa)