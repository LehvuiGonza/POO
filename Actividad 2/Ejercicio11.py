N1 = int(input("Ingrese el primer número entero: "))
N2 = int(input("Ingrese el segundo número entero: "))
N3 = int(input("Ingrese el tercer número entero: "))

if N1 > N2 and N1 > N3:
    MAYOR = N1
elif N2 > N3:
    MAYOR = N2
else:
    MAYOR = N3

print("El valor mayor entre", N1, ",", N2, "y", N3, "es:", MAYOR)