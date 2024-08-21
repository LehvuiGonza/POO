class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self._saldo = saldo
        self._numero_consignaciones = 0
        self._numero_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0

    def consignar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            self._numero_consignaciones += 1
        else:
            print("La cantida a consignar debe ser pisitiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            self._numero_retiros += 1
        else:
            print("La cantida a retirar excede el saldo actual.")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 12) * self._saldo / 100
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        print(f"Saldo: {self._saldo}")
        print(f"Número de consignaciones: {self._numero_consignaciones}")
        print(f"Número de retiros: {self._numero_retiros}")
        print(f"Comisión mensual: {self._comision_mensual}")

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, cantidad):
        if self._activa:
            super().consignar(cantidad)
        self.verificar_estado_cuenta()

    def retirar(self, cantidad):
        if self._activa:
            super().retirar(cantidad)
        self.verificar_estado_cuenta()

    def extracto_mensual(self):
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        super().extracto_mensual()
        self.verificar_estado_cuenta()

    def verificar_estado_cuenta(self):
        self._activa = self._saldo >= 10000

    def imprimir(self):
        super().imprimir()
        print(f"Cuenta activa: {self._activa}")

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0

    def retirar(self, cantidad):
        if cantidad > self._saldo:
            self._sobregiro += (cantidad - self._saldo)
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self._sobregiro > 0:
            if cantidad > self._sobregiro:
                self._saldo += (cantidad - self._sobregiro)
                self._sobregiro = 0
            else:
                self._sobregiro -= cantidad
        else:
            super().consignar(cantidad)

    def imprimir(self):
        super().imprimir()
        print(f"Sobregiro: {self._sobregiro}")