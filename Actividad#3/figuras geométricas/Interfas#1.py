import tkinter as tk
from tkinter import messagebox
from figuras import Circulo, Rectangulo, Cuadrado, TrianguloRectangulo

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas")

        tk.Label(root, text="Radio del círculo:").grid(row=0, column=0, padx=10, pady=5)
        self.radio_entry = tk.Entry(root)
        self.radio_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Base del rectángulo:").grid(row=1, column=0, padx=10, pady=5)
        self.base_rect_entry = tk.Entry(root)
        self.base_rect_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Altura del rectángulo:").grid(row=2, column=0, padx=10, pady=5)
        self.altura_rect_entry = tk.Entry(root)
        self.altura_rect_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Lado del cuadrado:").grid(row=3, column=0, padx=10, pady=5)
        self.lado_cuad_entry = tk.Entry(root)
        self.lado_cuad_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Base del triángulo:").grid(row=4, column=0, padx=10, pady=5)
        self.base_tri_entry = tk.Entry(root)
        self.base_tri_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Altura del triángulo:").grid(row=5, column=0, padx=10, pady=5)
        self.altura_tri_entry = tk.Entry(root)
        self.altura_tri_entry.grid(row=5, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            base_rect = float(self.base_rect_entry.get())
            altura_rect = float(self.altura_rect_entry.get())
            lado_cuad = float(self.lado_cuad_entry.get())
            base_tri = float(self.base_tri_entry.get())
            altura_tri = float(self.altura_tri_entry.get())

            circulo = Circulo(radio)
            rectangulo = Rectangulo(base_rect, altura_rect)
            cuadrado = Cuadrado(lado_cuad)
            triangulo = TrianguloRectangulo(base_tri, altura_tri)

            resultados = []
            resultados.append(circulo.mostrar_informacion())
            resultados.append(rectangulo.mostrar_informacion())
            resultados.append(cuadrado.mostrar_informacion())
            resultados.append(triangulo.mostrar_informacion())

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "\n\n".join(resultados))

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()