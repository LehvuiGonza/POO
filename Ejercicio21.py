import math

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def calcular_semiperimetro(self):
        return self.calcular_perimetro() / 2

    def calcular_area(self):
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c))

    def mostrar_informacion(self):
        perimetro = self.calcular_perimetro()
        semiperimetro = self.calcular_semiperimetro()
        area = self.calcular_area()
        print("Perímetro:", perimetro)
        print("Semiperimetro:", semiperimetro)
        print("Área:", area)


lado_a = 3
lado_b = 4
lado_c = 5

triangulo = Triangulo(lado_a, lado_b, lado_c)
triangulo.mostrar_informacion()