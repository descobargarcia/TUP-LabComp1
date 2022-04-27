
print("""
Este programa muestra los numeros enteros positivos desde
"n" hasta "2n-1", siendo "n" ingresado por el usuario
""")
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
print ()
