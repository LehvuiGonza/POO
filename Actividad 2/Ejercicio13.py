VALCOMP = float(input("Ingrese el valor de la compra: "))
COLOR = input("Ingrese el color de la bolita: ").upper()  # Convertir a mayúsculas para evitar errores de comparación


if COLOR == "BLANCO":
    PDES = 0
elif COLOR == "VERDE":
    PDES = 10
elif COLOR == "AMARILLO":
    PDES = 25
elif COLOR == "AZUL":
    PDES = 50
else:
    PDES = 100

VALPAG = VALCOMP - PDES * VALCOMP / 100

print("EL CLIENTE DEBE PAGAR: $", VALPAG)