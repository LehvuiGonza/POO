import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} - {self.apellidos} - {self.telefono} - {self.direccion}"

class ListaPersonas:
    def __init__(self):
        self.lista_personas = []

    def anadir_persona(self, persona):
        self.lista_personas.append(persona)

    def eliminar_persona(self, indice):
        if 0 <= indice < len(self.lista_personas):
            del self.lista_personas[indice]

    def borrar_lista(self):
        self.lista_personas.clear()

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lista = ListaPersonas()
        self.title("Gestión de Personas")
        self.geometry("270x350")
        self.resizable(False, False)
        
        self.nombre_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.direccion_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nombre:").place(x=20, y=20)
        tk.Entry(self, textvariable=self.nombre_var).place(x=105, y=20, width=135)
        
        tk.Label(self, text="Apellidos:").place(x=20, y=50)
        tk.Entry(self, textvariable=self.apellidos_var).place(x=105, y=50, width=135)
        
        tk.Label(self, text="Teléfono:").place(x=20, y=80)
        tk.Entry(self, textvariable=self.telefono_var).place(x=105, y=80, width=135)
        
        tk.Label(self, text="Dirección:").place(x=20, y=110)
        tk.Entry(self, textvariable=self.direccion_var).place(x=105, y=110, width=135)

        tk.Button(self, text="Añadir", command=self.anadir_persona).place(x=105, y=150, width=80)
        tk.Button(self, text="Eliminar", command=self.eliminar_persona).place(x=20, y=280, width=80)
        tk.Button(self, text="Borrar Lista", command=self.borrar_lista).place(x=120, y=280, width=120)

        self.modelo = tk.StringVar(value=[])
        self.lista_nombres = tk.Listbox(self, listvariable=self.modelo, selectmode=tk.SINGLE)
        self.lista_nombres.place(x=20, y=190, width=220, height=80)
        
    def anadir_persona(self):
        nombre = self.nombre_var.get()
        apellidos = self.apellidos_var.get()
        telefono = self.telefono_var.get()
        direccion = self.direccion_var.get()

        if not (nombre and apellidos and telefono and direccion):
            messagebox.showwarning("Advertencia", "Complete todos los campos.")
            return
        
        persona = Persona(nombre, apellidos, telefono, direccion)
        self.lista.anadir_persona(persona)
        
        self.actualizar_lista()
        self.limpiar_campos()

    def eliminar_persona(self):
        seleccion = self.lista_nombres.curselection()
        if seleccion:
            self.lista.eliminar_persona(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una persona para eliminar.")

    def borrar_lista(self):
            self.lista.borrar_lista()
            self.actualizar_lista()

    def actualizar_lista(self):
        self.modelo.set([str(persona) for persona in self.lista.lista_personas])

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.apellidos_var.set("")
        self.telefono_var.set("")
        self.direccion_var.set("")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
