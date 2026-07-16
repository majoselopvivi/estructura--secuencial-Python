salario = float(input("Ingrese el salario: "))

salud = salario * 0.04
pension = salario * 0.04
segSocial = salud + pension 
salarioNeto = salario - segSocial

print ("El salario es: ", salario)
print ("La salud es: ", salud)
print ("La pension es: ", pension)
print ("La segSocial es: ", segSocial)
print ("El salarioNeto es: ", salarioNeto)