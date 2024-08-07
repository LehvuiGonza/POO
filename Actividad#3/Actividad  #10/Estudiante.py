class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago_matricula(self):
        pago_matricula = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            pago_matricula += 0.03 * self.patrimonio
        return pago_matricula

    def mostrar_informacion(self):
        pago_matricula = self.calcular_pago_matricula()
        return (self.numero_inscripcion, self.nombres, pago_matricula)