class Empleado:
    def __init__(self, codigo, nombre, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = salario_bruto * (self.retencion / 100)
        return salario_bruto - retencion

    def mostrar_informacion(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        print("Código del empleado:", self.codigo)
        print("Nombres:", self.nombre)
        print("Salario bruto:", salario_bruto)
        print("Salario neto:", salario_neto)


empleado1 = Empleado( "001", "Juan Perez", 160, 10, 10)
empleado1.mostrar_informacion()