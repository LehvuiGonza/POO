from Cuenta import CuentaAhorros, CuentaCorriente

print("Cuenta de ahorros")
saldo_inicial_ahorros = float(input("Ingrese saldo inicial= $"))
tasa_ahorros = float(input("Ingrese tasa de interés= "))

cuenta_ahorros = CuentaAhorros(saldo_inicial_ahorros, tasa_ahorros)

cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
cuenta_ahorros.consignar(cantidad_depositar)

cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
cuenta_ahorros.retirar(cantidad_retirar)

cuenta_ahorros.extracto_mensual()
cuenta_ahorros.imprimir()

print("\nCuenta corriente")
saldo_inicial_corriente = float(input("Ingrese saldo inicial= $"))
tasa_corriente = float(input("Ingrese tasa de interés= "))

cuenta_corriente = CuentaCorriente(saldo_inicial_corriente, tasa_corriente)

cantidad_depositar_corriente = float(input("Ingresar cantidad a consignar: $"))
cuenta_corriente.consignar(cantidad_depositar_corriente)

cantidad_retirar_corriente = float(input("Ingresar cantidad a retirar: $"))
cuenta_corriente.retirar(cantidad_retirar_corriente)

cuenta_corriente.extracto_mensual()
cuenta_corriente.imprimir()