from animales import Gato, Perro, Lobo, Leon

animales = [
    Gato(),
    Perro(),
    Lobo(),
    Leon()
]

for animal in animales:  
    print(f"Nombre científico: {animal.get_nombre_cientifico()}")
    print(f"Sonido: {animal.get_sonido()}")
    print(f"Alimentos: {animal.get_alimentos()}")
    print(f"Hábitat: {animal.get_habitat()}")
    print()