
print('\nEste programa muestra los números enteros positivos desde')
print('"n" hasta "2n-1", siendo "n" ingresado por el usuario\n')
while True: 
    n = int(input('Ingresar "n", entero positivo: '))
    if n <= 0:
        print('Numero invalido')
        continue
    else:
        break
print ()
for num in range (n, 2*n):
    print (f'{num}')

