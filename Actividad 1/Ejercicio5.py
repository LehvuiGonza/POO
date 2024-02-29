import math

radio = float(input())
area=math.pi*pow(radio,2)
longitud=2*math.pi+radio

print("el circulo con radio = "+str(radio)+" tiene: \nArea = "+str(round(area, 2))+"\nLongitud de circunferencia = 7"+str(round(longitud, 2)))