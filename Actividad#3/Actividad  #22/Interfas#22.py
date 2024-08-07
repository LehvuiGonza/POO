import tkinter as tk
from tkinter import messagebox
from Trabajador import Trabajador  

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Salario Mensual")

        tk.Label(root, text="Nombre del trabajador:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Salario por hora:").grid(row=1, column=0, padx=10, pady=5)
        self.salario_entry = tk.Entry(root)
        self.salario_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=2, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            nombre = self.nombre_entry.get()
            salario_por_hora = float(self.salario_entry.get())
            horas_trabajadas = float(self.horas_entry.get())

            trabajador = Trabajador(nombre, salario_por_hora, horas_trabajadas)
            resultado = trabajador.mostrar_informacion()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, resultado)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para salario y horas trabajadas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()