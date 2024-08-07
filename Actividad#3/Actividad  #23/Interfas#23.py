import tkinter as tk
from tkinter import messagebox
from EcuacionSegundoGrado import EcuacionSegundoGrado 

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolución de Ecuación de Segundo Grado")

        tk.Label(root, text="Coeficiente a:").grid(row=0, column=0, padx=10, pady=5)
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Coeficiente b:").grid(row=1, column=0, padx=10, pady=5)
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Coeficiente c:").grid(row=2, column=0, padx=10, pady=5)
        self.c_entry = tk.Entry(root)
        self.c_entry.grid(row=2, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            ecuacion = EcuacionSegundoGrado(a, b, c)
            resultado = ecuacion.calcular_soluciones()

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, resultado)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para los coeficientes.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()