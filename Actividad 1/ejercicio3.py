horas_tabajadas = 48    
valor_hora = 5000
salario_bruto = horas_tabajadas * valor_hora
retencion =  float(salario_bruto * 0.125)
salario_neto = float(salario_bruto) - retencion
print("Horas trabajadas : "+str(horas_tabajadas))
print("Valor de hora : "+str(valor_hora))
print("El salario bruto es : "+str(salario_bruto))
print("El salario neto es : "+str(salario_neto))
print("La retencion en la fuente es : "+str(retencion))