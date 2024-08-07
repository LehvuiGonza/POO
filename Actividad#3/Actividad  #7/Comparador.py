class Comparador:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return "A es mayor que B"
        elif self.a == self.b:
            return "A es igual a B"
        else:
            return "A es menor que B"