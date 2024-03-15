NI = input("Ingrese el número de inscripción del estudiante: ")
NOM = input("Ingrese los nombres del estudiante: ")
PAT = float(input("Ingrese el patrimonio del estudiante: "))
ES = int(input("Ingrese el estrato social del estudiante: "))

PAGMAT = 50000

if PAT > 2000000 and ES > 3:
    PAGMAT += 0.03 * PAT

print("EL ESTUDIANTE CON NUMERO DE INSCRIPCION", NI, "Y NOMBRE", NOM, "DEBE PAGAR: $", PAGMAT)