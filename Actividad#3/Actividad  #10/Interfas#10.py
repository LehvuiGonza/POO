import tkinter as tk
from tkinter import messagebox
from Estudiante import Estudiante 

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrícula")

        tk.Label(root, text="Número de inscripción:").grid(row=0, column=0, padx=10, pady=5)
        self.numero_entry = tk.Entry(root)
        self.numero_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
        self.patrimonio_entry = tk.Entry(root)
        self.patrimonio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Estrato social:").grid(row=3, column=0, padx=10, pady=5)
        self.estrato_entry = tk.Entry(root)
        self.estrato_entry.grid(row=3, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            numero_inscripcion = self.numero_entry.get()
            nombres = self.nombres_entry.get()
            patrimonio = float(self.patrimonio_entry.get())
            estrato = int(self.estrato_entry.get())

            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
            numero, nombres, pago_matricula = estudiante.mostrar_informacion()

            result = (f"El estudiante con número de inscripción {numero}\n"
                      f"y nombre {nombres}, debe pagar: ${pago_matricula:.2f}")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para patrimonio y estrato.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()