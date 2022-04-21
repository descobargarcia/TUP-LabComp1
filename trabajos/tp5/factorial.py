print('\nCALCULADORA DEL FACTORIAL DE UN ENTERO POSITIVO\n')

while True: 
    num = int(input('Ingrese un numero: '))
    if num < 0:
        print('No se puede calcular factorial de un negativo')
        continue
    else:
        break
factorial = 1
if num < 2:
    exit(f'\n{factorial = }\n')
for n in range (2, num+1):
    factorial *= n
print(f'\n{factorial = }\n')
