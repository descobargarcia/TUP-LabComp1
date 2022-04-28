# Hacer un programa que muestre los números pares entre 0 y un numero 
# ingresado por el usuario.

print ("""
PROGRAMA QUE MUESTRA LOS NUMEROS PARES DESDE 0
HASTA UN NUMERO ENTERO INGRESADO""")
numEntrada = int(input("\nIngrese un numero entero: "))
absEntrada = abs(numEntrada)
signo = 1 if numEntrada >= 0 else -1
incremento = signo*2
numPar = 0
print ('Los numeros pares son:\n')
while abs(numPar) <= absEntrada:
    print(f'{numPar:>4}') # alineacion: 4 espacios --->
    numPar += incremento 
print()
