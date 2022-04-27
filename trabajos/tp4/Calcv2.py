print("""
CALCULADORA ARITMETICA
Este programa simula una calculadora aritmetica que trabaja
con dos numeros reales por operacion
    
    MENU DE OPCIONES
    1: Suma
    2: Resta
    3: Multiplicar
    4: Dividir
    5: Salir""")
while True:
    opcion = int(input('\nIngrese una opcion valida: '))    
    if (opcion <1 or opcion >5):
        print('Opcion invalida. Intente de nuevo')
        continue
    if (opcion == 5):
        exit('FIN!\n')
    num1 = float(input('Primer numero: '))
    num2 = float(input('Segundo numero: '))
    if opcion == 1:
        resultado = num1 + num2 
    elif opcion == 2:
        resultado = num1 - num2
    elif opcion == 3:
        resultado = num1*num2
    else:
        if num2 == 0:
            print('\nERROR: no se puede dividir por cero')
            continue
        resultado = num1/num2
    print (f'{resultado = }')
