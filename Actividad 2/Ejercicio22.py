nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_por_hora = float(input("Ingrese el salario básico por hora: "))
horas_trabajadas_mes = float(input("Ingrese el número de horas trabajadas en el mes: "))


salario_mensual = salario_por_hora * horas_trabajadas_mes

if salario_mensual > 450000:
    print("Nombre del empleado:", nombre_empleado)
    print("Salario mensual:", salario_mensual)
else:
    print("Nombre del empleado:", nombre_empleado)