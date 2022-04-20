print ('Este programa calcula los litros de pintura requeridos')
print ('a partir de las dimensiones de una pared\n')
Ancho = float(input('Ingrese el ancho en metros: '))
Alto = float(input('Ingrese el alto en metros: '))
Area = Ancho*Alto
LitrosPintura = Area/10
print ('----')
print(f'Se requieren {round(LitrosPintura,2)} litros para pintar la pared')