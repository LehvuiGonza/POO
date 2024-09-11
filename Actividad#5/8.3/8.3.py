import tkinter as tk
from ventana_cilindro import VentanaCilindro
from ventana_esfera import VentanaEsfera
from ventana_piramide import VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)

        self.cilindro_btn = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.cilindro_btn.place(x=20, y=50)

        self.esfera_btn = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.esfera_btn.place(x=125, y=50)

        self.piramide_btn = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        self.piramide_btn.place(x=225, y=50)

    def abrir_cilindro(self):
        VentanaCilindro(self).grab_set()

    def abrir_esfera(self):
        VentanaEsfera(self).grab_set()

    def abrir_piramide(self):
        VentanaPiramide(self).grab_set()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
