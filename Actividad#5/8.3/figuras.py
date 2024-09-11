import math

class FiguraGeometrica:
    def calcular_volumen(self):{}

    def calcular_superficie(self):{}
 

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio**2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return 4/3 * math.pi * self.radio**3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio**2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return (self.base**2 * self.altura) / 3

    def calcular_superficie(self):
        return self.base**2 + 2 * self.base * self.apotema