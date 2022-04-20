# Hacer un programa que muestre los números pares entre 0 y un numero 
# ingresado por el usuario.

print ("\nPROGRAMA QUE MUESTRA LOS NUM. PARES DESDE 0")
print ("HASTA UN NUM. ENTERO INGRESADO")
numEntrada = int(input("\nIngrese un número entero: "))
numPar = 0
print ('\nLos números pares son:\n')
if (numEntrada >= 0):
    while (numPar <= numEntrada):
        print(f'{numPar:>4}')
        numPar += 2
else:
    while (numPar >= numEntrada):
        print(f'{numPar:>4}')
        numPar -= 2
