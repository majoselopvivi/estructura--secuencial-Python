valPresente = float(input("Ingrese el valor presente: "))
dias = int(input("Ingrese el número de días: "))

tasInteres = (1 + 0.115) ** (dias / 360) - 1
intBrutos = valPresente * tasInteres
impuesto = intBrutos * 0.04
intNeto = intBrutos - impuesto
valFinal = valPresente + intNeto

print("La tasa de interés es:", tasInteres)
print("Los intereses brutos son:", intBrutos)
print("El impuesto es:", impuesto)
print("Los intereses netos son:", intNeto)
print("El valor final es:", valFinal)