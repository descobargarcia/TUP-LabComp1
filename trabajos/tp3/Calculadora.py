print('\nCALCULADORA ARITMETICA\n')
print('Debe ingresar dos numeros e indicar una operacion:')
print('suma, resta, multiplicacion o division\n')
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion aritmetica a realizar: ")
if operacion == 'suma':
    resultado = n1 + n2 
elif operacion == 'resta':
    resultado = n1 - n2
elif operacion == 'multiplicacion':
    resultado = n1*n2
elif operacion == 'division':
    if n2 == 0:
        exit('\nERROR: no se puede dividir por cero\n')
    resultado = n1/n2
else:
    exit('\n OPERACION INVALIDA \n')
print (f'Resultado: {resultado}')
