print('\nCALCULADORA ARITMETICA')
print('Este programa simula una calculadora aritmética que trabaja')
print('con dos números reales por operación')
print ('\nMENÚ DE OPCIONES')
print ('1: Suma')
print ('2: Resta')
print ('3: Multiplicar')
print ('4: Dividir')
print ('5: Salir')
opcion = int(0)
while (opcion !=5):
    opcion = int(input('\nIngrese una opción válida: '))    
    if (opcion <1 or opcion >5):
        print('Opción inválida. Intente de nuevo')
        continue
    if (opcion == 5):
        exit('¡FIN!')
    num1 = float(input('Primer numero: '))
    num2 = float(input('Segundo numero: '))
    if opcion == 1:
        Resultado = num1 + num2 
    elif opcion == 2:
        Resultado = num1 - num2
    elif opcion == 3:
        Resultado = num1*num2
    else:
        if num2 == 0:
            print('\nERROR: no se puede dividir por cero')
            continue
        Resultado = num1/num2
    print (f'{Resultado = }')
print()
