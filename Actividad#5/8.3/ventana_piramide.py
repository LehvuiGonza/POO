import tkinter as tk
from tkinter import messagebox
from figuras import Piramide

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)

        self.base_label = tk.Label(self, text="Base (cms):")
        self.base_label.place(x=20, y=20)
        self.base_entry = tk.Entry(self)
        self.base_entry.place(x=120, y=20)

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50)
        self.altura_entry = tk.Entry(self)
        self.altura_entry.place(x=120, y=50)

        self.apotema_label = tk.Label(self, text="Apotema (cms):")
        self.apotema_label.place(x=20, y=80)
        self.apotema_entry = tk.Entry(self)
        self.apotema_entry.place(x=120, y=80)

        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=120, y=110)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=140)

        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            piramide = Piramide(base, altura, apotema)
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
