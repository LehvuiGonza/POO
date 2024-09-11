import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0] * 5

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = sum((nota - promedio) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("300x350")

        self.notas = Notas()

        self.labels = []
        self.entries = []

        for i in range(5):
            label = tk.Label(self, text=f"Nota {i+1}:")
            label.grid(row=i, column=0, padx=10, pady=5)
            self.labels.append(label)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.calcular_btn.grid(row=5, column=0, columnspan=2, pady=10)

        self.limpiar_btn = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar_btn.grid(row=6, column=0, columnspan=2, pady=10)

        self.resultados = {
            "Promedio": tk.Label(self, text="Promedio = "),
            "Desviación": tk.Label(self, text="Desviación = "),
            "Mayor": tk.Label(self, text="Nota mayor = "),
            "Menor": tk.Label(self, text="Nota menor = ")
        }

        for i, (key, label) in enumerate(self.resultados.items()):
            label.grid(row=7+i, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            self.notas.lista_notas = [float(entry.get()) for entry in self.entries]
            promedio = self.notas.calcular_promedio()
            desviacion = self.notas.calcular_desviacion()
            menor = self.notas.calcular_menor()
            mayor = self.notas.calcular_mayor()

            self.resultados["Promedio"].config(text=f"Promedio = {promedio:.2f}")
            self.resultados["Desviación"].config(text=f"Desviación = {desviacion:.2f}")
            self.resultados["Mayor"].config(text=f"Nota mayor = {mayor:.2f}")
            self.resultados["Menor"].config(text=f"Nota menor = {menor:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para todas las notas.")

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        for label in self.resultados.values():
            label.config(text="")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
