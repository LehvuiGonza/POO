from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat):
        self.nombre_cientifico = nombre_cientifico
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


class Canido(Animal):
    pass


class Felino(Animal):
    pass


class Perro(Canido):
    def __init__(self):
        super().__init__("Canis lupus familiaris", "Ladrido", "Carnívoro", "Doméstico")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Lobo(Canido):
    def __init__(self):
        super().__init__("Canis lupus", "Aullido", "Carnívoro", "Bosque")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Leon(Felino):
    def __init__(self):
        super().__init__("Panthera leo", "Rugido", "Carnívoro", "Pradera")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat


class Gato(Felino):
    def __init__(self):
        super().__init__("Felis silvestris catus", "Maullido", "Ratones", "Doméstico")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat