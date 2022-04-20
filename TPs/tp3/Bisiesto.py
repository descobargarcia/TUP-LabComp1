# Un año bisiesto debe ser divisible por 4 (condicion necesaria pero no suficiente). 
# Si es divisible por 100 pero no por 400, no se considera bisiesto.

print('\nCALCULADORA DE ANIOS BISIESTOS\n')
año = int(input("Ingrese un anio: "))
if (año%4 != 0) or (año%100 == 0 and año%400 != 0):
    print('\nNO es bisiesto\nFIN')
else:
    print('\nSI es bisiesto\nFIN')
