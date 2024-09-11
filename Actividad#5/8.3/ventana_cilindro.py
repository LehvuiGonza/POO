import tkinter as tk
from tkinter import messagebox
from figuras import Cilindro

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)

        self.radio_label = tk.Label(self, text="Radio (cms):")
        self.radio_label.place(x=20, y=20)
        self.radio_entry = tk.Entry(self)
        self.radio_entry.place(x=100, y=20)

        self.altura_label = tk.Label(self, text="Altura (cms):")
        self.altura_label.place(x=20, y=50)
        self.altura_entry = tk.Entry(self)
        self.altura_entry.place(x=100, y=50)

        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.place(x=100, y=80)

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=110)

        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=140)

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
