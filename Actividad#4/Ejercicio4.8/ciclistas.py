from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador, nombre, tiempo_acumulado=0):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado = tiempo_acumulado

    @abstractmethod
    def imprimirTipo(self):
        pass

    def get_identificador(self):
        return self.__identificador

    def get_nombre(self):
        return self.__nombre

    def get_tiempo_acumulado(self):
        return self.__tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo):
        self.__tiempo_acumulado = tiempo

    def imprimir_datos(self):
        print(f"ID: {self.__identificador}, Nombre: {self.__nombre}, Tiempo Acumulado: {self.__tiempo_acumulado} minutos")


class Velocista(Ciclista):
    def __init__(self, identificador, nombre, tiempo_acumulado, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_promedio = velocidad_promedio

    def imprimirTipo(self):
        return "Es un Velocista"

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Potencia Promedio: {self.__potencia_promedio} W, Velocidad Promedio: {self.__velocidad_promedio} km/h")


class Escalador(Ciclista):
    def __init__(self, identificador, nombre, tiempo_acumulado, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa

    def imprimirTipo(self):
        return "Es un Escalador"

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Aceleración Promedio: {self.__aceleracion_promedio} m/s², Grado de Rampa: {self.__grado_rampa} grados")


class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, tiempo_acumulado, velocidad_maxima):
        super().__init__(identificador, nombre, tiempo_acumulado)
        self.__velocidad_maxima = velocidad_maxima

    def imprimirTipo(self):
        return "Es un Contrarrelojista"

    def imprimir_datos(self):
        super().imprimir_datos()
        print(f"Velocidad Máxima: {self.__velocidad_maxima} km/h")


class Equipo:
    __tiempo_total = 0

    def __init__(self, nombre, pais):
        self.__nombre = nombre
        self.__pais = pais
        self.__ciclistas = []

    def get_nombre(self):
        return self.__nombre

    def get_pais(self):
        return self.__pais

    def get_tiempo_total(self):
        return self.__tiempo_total

    def añadir_ciclista(self, ciclista):
        self.__ciclistas.append(ciclista)
        Equipo.__tiempo_total += ciclista.get_tiempo_acumulado()

    def imprimir_datos_equipo(self):
        print(f"Equipo: {self.__nombre}, País: {self.__pais}")
        print(f"Tiempo Total del Equipo: {Equipo.__tiempo_total} minutos")

    def listar_ciclistas(self):
        print("Ciclistas del equipo:")
        for ciclista in self.__ciclistas:
            print(f"- {ciclista.get_nombre()}")

    def imprimir_ciclista_por_id(self, identificador):
        for ciclista in self.__ciclistas:
            if ciclista.get_identificador() == identificador:
                ciclista.imprimir_datos()
                return
        print("Ciclista no encontrado.")
