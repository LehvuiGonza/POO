from inmuebles import ApartamentoFamiliar, Apartaestudio

apto1 = ApartamentoFamiliar(
    id_inmobiliario=103067, 
    area=120,
    direccion="Avenida Santander 45-45",
    num_habitaciones=3,
    num_banos=2,
    valor_administracion=200000  
)

print("Datos apartamento familiar")
print(f"Precio de venta: {apto1.calcular_valor_compra()}")  
apto1.imprimir()

aptestudio1 = Apartaestudio(
    id_inmobiliario=12354,  
    area=50,
    direccion="Avenida Caracas 30-15"
)

print("Datos apartaestudio")
print(f"Precio de venta: {aptestudio1.calcular_valor_compra()}") 
aptestudio1.imprimir()