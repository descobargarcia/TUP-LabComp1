from turtle import numinput


# Hacer un programa que muestre los números pares entre 0 y un numero 
# ingresado por el usuario.

print ("\nPROGRAMA QUE MUESTRA LOS NUM. PARES DESDE 0")
print ("HASTA UN NUM. ENTERO INGRESADO")
numInput = int(input("\nIngrese un número entero: "))
numPar = 0
print (" ")
if (numInput >= 0):
    while (numPar <= numInput):
        print(f'{numPar = }')
        numPar += 2
else:
    while (numPar >= numInput):
        print(f'{numPar = }')
        numPar -= 2
