print('\nIngrese 3 numeros enteros\n')
n1 = int(input('n1= '))
n2 = int(input('n2= '))
n3 = int(input('n3= '))
if n3>n2 and n2>n1:
    Nmayor = n3
elif n2>n1 and n1>n3:
    Nmayor = n2
else:
    Nmayor = n1
print (f'\nEl mayor entero es: {Nmayor}')