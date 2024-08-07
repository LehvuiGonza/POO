class Trabajador:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def mostrar_informacion(self):
        salario_mensual = self.calcular_salario_mensual()
        if (salario_mensual > 450000):
            return f"Nombre: {self.nombre}\nSalario Mensual: ${salario_mensual:.2f}"
        else:
            return f"Nombre: {self.nombre}"