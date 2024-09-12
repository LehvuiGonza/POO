import tkinter as tk
from tkinter import messagebox
from crear import Crear
from eliminar import Eliminar
from actualizar import Actualizar
from leer import Leer

crear = Crear()
eliminar = Eliminar()
actualizar = Actualizar()
leer = Leer()

def agregar_contacto():
    nombre = nombre_entry.get()
    numero = numero_entry.get()
    if nombre and numero:
        resultado = crear.add_friend(nombre, numero)  
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese ambos campos.")

def eliminar_contacto():
    nombre = nombre_entry.get()
    if nombre:
        resultado = eliminar.delete_friend(nombre)
        messagebox.showinfo("Resultado", resultado)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre.")

def actualizar_contacto():
    nombre = nombre_entry.get()
    numero = numero_entry.get()
    if nombre and numero:
        try:
            numero = int(numero)
            resultado = actualizar.update_friend(nombre, numero)  
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showwarning("Advertencia", "El número debe ser un valor numérico.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese ambos campos.")

def mostrar_contactos():
    nombre = nombre_entry.get()
    if nombre:
        resultado = leer.buscar_contacto(nombre)
        if resultado.startswith("El nombre ingresado no existe"):
            messagebox.showinfo("Resultado", resultado)
        else:
            numero_entry.delete(0, tk.END)  
            numero_entry.insert(0, resultado) 
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre.")

def limpiar_campos():
    nombre_entry.delete(0, tk.END)
    numero_entry.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Gestión de Contactos")

nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)

nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

numero_label = tk.Label(ventana, text="Número:")
numero_label.grid(row=1, column=0, padx=5, pady=5)

numero_entry = tk.Entry(ventana)
numero_entry.grid(row=1, column=1, padx=5, pady=5)

botones_frame = tk.Frame(ventana)
botones_frame.grid(row=2, column=0, columnspan=2, pady=10)

agregar_btn = tk.Button(botones_frame, text="Agregar", command=agregar_contacto)
agregar_btn.pack(side=tk.LEFT, padx=5)

eliminar_btn = tk.Button(botones_frame, text="Eliminar", command=eliminar_contacto)
eliminar_btn.pack(side=tk.LEFT, padx=5)

actualizar_btn = tk.Button(botones_frame, text="Actualizar", command=actualizar_contacto)
actualizar_btn.pack(side=tk.LEFT, padx=5)

mostrar_btn = tk.Button(botones_frame, text="Mostrar", command=mostrar_contactos)
mostrar_btn.pack(side=tk.LEFT, padx=5)

limpiar_btn = tk.Button(botones_frame, text="Limpiar", command=limpiar_campos)
limpiar_btn.pack(side=tk.LEFT, padx=5)

ventana.mainloop()
