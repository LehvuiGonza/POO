VD1 = float(input("Ingrese las ventas del departamento 1: "))
VD2 = float(input("Ingrese las ventas del departamento 2: "))
VD3 = float(input("Ingrese las ventas del departamento 3: "))
SALAR = float(input("Ingrese el salario de los vendedores: "))

TOTVEN = VD1 + VD2 + VD3
PORVEN = 0.33 * TOTVEN

if VD1 > PORVEN:
    SALAR1 = SALAR + 0.2 * SALAR
else:
    SALAR1 = SALAR

if VD2 > PORVEN:
    SALAR2 = SALAR + 0.2 * SALAR
else:
    SALAR2 = SALAR

if VD3 > PORVEN:
    SALAR3 = SALAR + 0.2 * SALAR
else:
    SALAR3 = SALAR

print("SALARIO VENDEDORES DEPTO. 1:", SALAR1)
print("SALARIO VENDEDORES DEPTO. 2:", SALAR2)
print("SALARIO VENDEDORES DEPTO. 3:", SALAR3)