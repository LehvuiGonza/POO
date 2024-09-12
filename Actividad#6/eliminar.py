import os

class Eliminar:
    def __init__(self, file_name="friendsContact.txt"):
        self.file_name = file_name
        self.temp_file_name = "temp.txt"

    def delete_friend(self, input_name):
        try:
            if not os.path.exists(self.file_name):
                return "El archivo no existe."

            found = False

            with open(self.file_name, "r") as file, open(self.temp_file_name, "w") as temp_file:
                for line in file:
                    name, number = line.strip().split("!")
                    if name == input_name:
                        found = True
                        continue
                    temp_file.write(line)

            if found:
                os.replace(self.temp_file_name, self.file_name)
                return "Amigo eliminado."
            else:
                os.remove(self.temp_file_name)
                return "El nombre ingresado no existe."

        except IOError as e:
            return f"Error al manejar el archivo: {e}"
