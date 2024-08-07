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
        self.radio = int(radio)

    def calcular_area(self):
        return round(math.pi * self.radio**2,2)

    def calcular_perimetro(self):
        return round(2 * math.pi * self.radio,2)

    def mostrar_informacion(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        return "Área del círculo: {}\nPerímetro del círculo: {}".format(area, perimetro)

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_informacion(self):
        area = round(self.calcular_area(), 2)
        perimetro = round(self.calcular_perimetro(), 2)
        return "Área del rectángulo: {}\nPerímetro del rectángulo: {}".format(area, perimetro)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def mostrar_informacion(self):
        area = round(self.calcular_area(), 2)
        perimetro = round(self.calcular_perimetro(), 2)
        return "Área del cuadrado: {}\nPerímetro del cuadrado: {}".format(area, perimetro)

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
        area = round(self.calcular_area(), 2)
        hipotenusa = round(self.calcular_hipotenusa(), 2)
        tipo = self.determinar_tipo_triangulo()
        return ("Área del triángulo rectángulo: {}\n"
                "Hipotenusa del triángulo rectángulo: {}\n"
                "Tipo de triángulo: {}".format(area, hipotenusa, tipo))