import os

class Leer:
    def __init__(self, file_name="friendsContact.txt"):
        self.file_name = file_name
        self.temp_file_name = "temp.txt"

    def buscar_contacto(self, nombre_buscado):
        try:
            if not os.path.exists(self.file_name):
                return "El archivo no existe. Creando archivo vacío."

            with open(self.file_name, "r") as file:
                for line in file:
                    name, number = line.strip().split("!")
                    if name == nombre_buscado:
                        return number
            
            return "El nombre ingresado no existe."

        except IOError as e:
            return f"Error al manejar el archivo: {e}"
        except ValueError:
            return "Error: Formato incorrecto en el archivo."
