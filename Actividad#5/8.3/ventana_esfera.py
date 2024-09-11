import tkinter as tk
from tkinter import messagebox
from figuras import Esfera

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)

        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20)
        self.radio_entry = tk.Entry(self)
        self.radio_entry.place(x=100, y=20)

        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=100, y=50)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=90)

        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            esfera = Esfera(radio)
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
