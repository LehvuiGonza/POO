peso_A = float(input("Ingrese el peso de la esfera A: "))
peso_B = float(input("Ingrese el peso de la esfera B: "))
peso_C = float(input("Ingrese el peso de la esfera C: "))
peso_D = float(input("Ingrese el peso de la esfera D: "))


if peso_A == peso_B and peso_A == peso_C:
    if peso_D > peso_A:
        print("La esfera D es diferente y de mayor peso.")
    else:
        print("La esfera D es diferente y de menor peso.")
elif peso_A == peso_B and peso_A == peso_D:
    if peso_C > peso_A:
        print("La esfera C es diferente y de mayor peso.")
    else:
        print("La esfera C es diferente y de menor peso.")
elif peso_A == peso_C and peso_A == peso_D:
    if peso_B > peso_D:
        print("La esfera B es diferente y de mayor peso.")
    else:
        print("La esfera B es diferente y de menor peso.")
else:
    if peso_A > peso_B:
        print("La esfera A es diferente y de mayor peso.")
    else:
        print("La esfera A es diferente y de menor peso.")