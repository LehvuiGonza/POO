import os

class Actualizar:
    def __init__(self, file_name="friendsContact.txt"):
        self.file_name = file_name
        self.temp_file_name = "temp.txt"

    def update_friend(self, name_to_update, new_number):
        try:
            new_number = str(new_number)
            
            if not os.path.exists(self.file_name):
                return "El archivo no existe."

            if not new_number.isdigit():
                return "Error: El número de teléfono debe ser un valor numérico."

            with open(self.file_name, "r") as file:
                lines = file.readlines()

            found = False
            with open(self.file_name, "w") as file:
                for line in lines:
                    name, number = line.strip().split("!")
                    if name == name_to_update:
                        file.write(f"{name_to_update}!{new_number}\n")
                        found = True
                    else:
                        file.write(line)

            if not found:
                return "El nombre no fue encontrado para actualizar."
                
            return "Amigo actualizado."

        except IOError as e:
            return f"Error al manejar el archivo: {e}"
