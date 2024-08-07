import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        discriminante = self.b**2 - 4*self.a*self.c
        if discriminante > 0:
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"Las soluciones son: x1 = {x1:.2f} y x2 = {x2:.2f}"
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return f"La solución doble es: x = {x:.2f}"
        else:
            real = -self.b / (2 * self.a)
            imaginario = math.sqrt(-discriminante) / (2 * self.a)
            return (f"Las soluciones complejas son: "
                    f"x1 = {real:.2f} + {imaginario:.2f}i y "
                    f"x2 = {real:.2f} - {imaginario:.2f}i")