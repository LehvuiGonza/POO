import tkinter as tk
from tkinter import messagebox
from Comparador import Comparador  
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Valores")

        tk.Label(root, text="Valor de A:").grid(row=0, column=0, padx=10, pady=5)
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)


        tk.Label(root, text="Valor de B:").grid(row=1, column=0, padx=10, pady=5)
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)


        self.compare_button = tk.Button(root, text="Comparar", command=self.comparar)
        self.compare_button.grid(row=2, column=0, columnspan=2, pady=10)


        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def comparar(self):
        try:

            a = float(self.a_entry.get())
            b = float(self.b_entry.get())


            comparador = Comparador(a, b)
            resultado = comparador.comparar()


            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, resultado)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()