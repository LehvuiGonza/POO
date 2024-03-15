import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return math.sqrt(3) / 2 * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def mostrar_informacion(self):
        perimetro = self.calcular_perimetro()
        altura = self.calcular_altura()
        area = self.calcular_area()
        print("Perímetro:", perimetro)
        print("Altura:", altura)
        print("Área:", area)



lado = float(input("Ingrese el valor del lado del triángulo equilátero: "))
triangulo = TrianguloEquilatero(lado)
triangulo.mostrar_informacion()