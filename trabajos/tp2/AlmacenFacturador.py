print ('\nPara cada producto comprado, ingrese el nombre del artículo (corrido) \
y precio (solo numeros).') 
print ('Solo deje 1 separacion entre nombre y precio')
print ('\nEJEMPLO: NombreProd1 175.00\n')
nombre1, precio1 = input('Producto Nº1. Ingrese nombre y precio: ').split()
nombre2, precio2 = input('Producto Nº2. Ingrese nombre y precio: ').split()
nombre3, precio3 = input('Producto Nº3. Ingrese nombre y precio: ').split()
precio1 = float(precio1)
precio2 = float(precio2)
precio3 = float(precio3)
subtotal = precio1 + precio2 + precio3
total_IVA = subtotal*1.21
print ('\n-----------------------------------\n')
print ('TICKET DE COMPRAS\n')
print(f'{nombre1:.15s} \t \t {precio1:.2f} pesos')
print(f'{nombre2:.15s} \t \t {precio2:.2f} pesos')
print(f'{nombre3:.15s} \t \t {precio3:.2f} pesos')
print('--------------------------------------')
print(f'SUBTOTAL: \t \t {subtotal:.2f} pesos')
print(f'TOTAL + IVA: \t \t {total_IVA:.2f} pesos\n')