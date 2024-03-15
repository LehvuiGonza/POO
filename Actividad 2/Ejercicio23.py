import math


A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))
C = float(input("Ingrese el término independiente C: "))


discriminante = B**2 - 4*A*C


if discriminante > 0:
    x1 = (-B + math.sqrt(discriminante)) / (2*A)
    x2 = (-B - math.sqrt(discriminante)) / (2*A)
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
elif discriminante == 0:
    x = -B / (2*A)
    print("La solución es:")
    print("x =", x)
else:
    parte_real = -B / (2*A)
    parte_imaginaria = math.sqrt(abs(discriminante)) / (2*A)
    print("Las soluciones son complejas:")
    print("x1 =", parte_real, "+", parte_imaginaria, "i")
    print("x2 =", parte_real, "-", parte_imaginaria, "i")