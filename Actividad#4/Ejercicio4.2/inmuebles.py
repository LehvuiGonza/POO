class Inmueble:
    def __init__(self, id_inmobiliario, area, direccion, valor_m2):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion
        self.valor_m2 = valor_m2

    def calcular_valor_compra(self):
        return self.area * self.valor_m2

    def imprimir(self):
        print(f"ID Inmobiliario: {self.id_inmobiliario}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Valor de compra: {self.calcular_valor_compra()}")


class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, valor_m2, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, area, direccion, valor_m2)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones: {self.num_habitaciones}")
        print(f"Número de baños: {self.num_banos}")


class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, valor_m2, num_habitaciones, num_banos, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, valor_m2, num_habitaciones, num_banos)
        self.num_pisos = num_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self.num_pisos}")


class Local(Inmueble):
    TIPO_INTERNO = 'interno'
    TIPO_CALLE = 'calle'

    def __init__(self, id_inmobiliario, area, direccion, tipo_local):
        super().__init__(id_inmobiliario, area, direccion, 2000000)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {'Interno' if self.tipo_local == Local.TIPO_INTERNO else 'Da a la calle'}")


class CasaRural(Casa):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, distancia, altitud):
        super().__init__(id_inmobiliario, area, direccion, 1500000, num_habitaciones, num_banos, num_pisos)
        self.distancia = distancia
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal: {self.distancia} km")
        print(f"Altitud: {self.altitud} msnm")


class LocalComercial(Local):
    valor_area = 3000000

    def __init__(self, id_inmobiliario, area, direccion, tipo_local, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}")


class CasaUrbana(Casa):
    valor_area = 2500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, self.valor_area, num_habitaciones, num_banos, num_pisos)


class Apartamento(InmuebleVivienda):
    valor_area = 2000000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, area, direccion, self.valor_area, num_habitaciones, num_banos)


class ApartamentoFamiliar(Apartamento):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, valor_administracion):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self.valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self.valor_administracion}")


class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, id_inmobiliario, area, direccion):
        super().__init__(id_inmobiliario, area, direccion, 1, 1)


class CasaConjuntoCerrado(CasaUrbana):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos, valor_administracion, tiene_piscina, tiene_campos_deportivos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self.valor_administracion}")
        print(f"Tiene piscina: {'Sí' if self.tiene_piscina else 'No'}")
        print(f"Tiene campos deportivos: {'Sí' if self.tiene_campos_deportivos else 'No'}")


class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, num_pisos)


class Oficina(Local):
    valor_area = 3500000

    def __init__(self, id_inmobiliario, area, direccion, tipo_local, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {'Sí' if self.es_gobierno else 'No'}")