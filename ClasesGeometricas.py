import math

class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def mostrar_informacion(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_informacion(self):
        print("Área del círculo:", self.calcular_area())
        print("Perímetro del círculo:", self.calcular_perimetro())

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_informacion(self):
        print("Área del rectángulo:", self.calcular_area())
        print("Perímetro del rectángulo:", self.calcular_perimetro())

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def mostrar_informacion(self):
        print("Área del cuadrado:", self.calcular_area())
        print("Perímetro del cuadrado:", self.calcular_perimetro())

class TrianguloRectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def determinar_tipo_triangulo(self):
        if self.base == self.altura:
            return "Equilátero"
        elif self.base == self.altura or self.base**2 + self.altura**2 == self.calcular_hipotenusa()**2:
            return "Isósceles"
        else:
            return "Escaleno"

    def mostrar_informacion(self):
        print("Área del triángulo rectángulo:", self.calcular_area())
        print("Hipotenusa del triángulo rectángulo:", self.calcular_hipotenusa())
        print("Tipo de triángulo:", self.determinar_tipo_triangulo())

# Solicitar datos al usuario
radio = float(input("Ingrese el radio del círculo: "))
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
base_triangulo = float(input("Ingrese la base del triángulo rectángulo: "))
altura_triangulo = float(input("Ingrese la altura del triángulo rectángulo: "))

circulo = Circulo(radio)
rectangulo = Rectangulo(base_rectangulo, altura_rectangulo)
cuadrado = Cuadrado(lado_cuadrado)
triangulo = TrianguloRectangulo(base_triangulo, altura_triangulo)

circulo.mostrar_informacion()
rectangulo.mostrar_informacion()
cuadrado.mostrar_informacion()
triangulo.mostrar_informacion()