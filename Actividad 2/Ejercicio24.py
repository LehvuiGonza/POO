peso_A = float(input("Ingrese el peso de la esfera A: "))
peso_B = float(input("Ingrese el peso de la esfera B: "))
peso_C = float(input("Ingrese el peso de la esfera C: "))

if peso_A > peso_B and peso_A > peso_C:
    print("La esfera A es la de mayor peso.")
elif peso_B > peso_A and peso_B > peso_C:
    print("La esfera B es la de mayor peso.")
elif peso_C > peso_A and peso_C > peso_B:
    print("La esfera C es la de mayor peso.")
else:
    print("Las esferas tienen el mismo peso.")