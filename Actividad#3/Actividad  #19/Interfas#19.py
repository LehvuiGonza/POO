import tkinter as tk
from tkinter import messagebox
from TrianguloEquilatero import TrianguloEquilatero

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Triángulo Equilátero")

        tk.Label(root, text="Lado del triángulo:").grid(row=0, column=0, padx=10, pady=5)
        self.lado_entry = tk.Entry(root)
        self.lado_entry.grid(row=0, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            lado = float(self.lado_entry.get())

            triangulo = TrianguloEquilatero(lado)
            perimetro, altura, area = triangulo.mostrar_informacion()

            result = (f"Perímetro: {perimetro:.2f}\n"
                      f"Altura: {altura:.2f}\n"
                      f"Área: {area:.2f}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()