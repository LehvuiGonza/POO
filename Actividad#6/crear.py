import os

class Crear:
    def __init__(self, file_name="friendsContact.txt"):
        self.file_name = file_name
        self.temp_file_name = "temp.txt"

    def add_friend(self, new_name, new_number):
        try:
            new_number = str(new_number)
            
            if not os.path.exists(self.file_name):
                with open(self.file_name, "w") as file:
                    pass

            if not new_number.isdigit():
                return "Error: El número de teléfono debe ser un valor numérico."

            with open(self.file_name, "r+") as file:
                for line in file:
                    name, number = line.strip().split("!")
                    if name == new_name:
                        return "El nombre ya existe."

                file.write(f"{new_name}!{new_number}\n")
            return "Amigo añadido."

        except IOError as e:
            return f"Error al manejar el archivo: {e}"
