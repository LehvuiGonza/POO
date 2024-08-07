import tkinter as tk
from tkinter import messagebox
from Empleado import Empleado

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Empleado")

        tk.Label(root, text="Código del empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Valor hora:").grid(row=3, column=0, padx=10, pady=5)
        self.valor_entry = tk.Entry(root)
        self.valor_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Retención (%):").grid(row=4, column=0, padx=10, pady=5)
        self.retencion_entry = tk.Entry(root)
        self.retencion_entry.grid(row=4, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular Salario", command=self.calcular_salario)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def calcular_salario(self):
        try:
            codigo = self.codigo_entry.get()
            nombre = self.nombre_entry.get()
            horas_trabajadas = float(self.horas_entry.get())
            valor_hora = float(self.valor_entry.get())
            retencion = float(self.retencion_entry.get())

            empleado = Empleado(codigo, nombre, horas_trabajadas, valor_hora, retencion)
            info = empleado.mostrar_informacion()

            result = (f"Código del empleado: {info[0]}\n"
                      f"Nombres: {info[1]}\n"
                      f"Salario bruto: {info[2]:.2f}\n"
                      f"Salario neto: {info[3]:.2f}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()