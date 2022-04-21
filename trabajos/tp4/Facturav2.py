print ('\nFACTURADOR DE ALMACÉN -versión 2\n')
print ('Para cada producto comprado, ingrese su precio en pesos') 
print ('(valor numérico).') 

numProd = int(0)
subtotal = 0.0
comprarMas = True
while comprarMas:
    numProd += 1
    precio = input(f'\nPrecio del producto {numProd}: ')
    precio = float(precio)
    subtotal += precio
    while True: 
        resp = input ('\n¿Desea comprar algo más? s/n: ')
        if (resp != 's' and resp != 'n'):
            print ('Ingrese una opción válida')
            continue
        else:
            break
    comprarMas = True if (resp == 's') else False

# Se aplica el IVA sólo al final. Menor costo computacional
total_IVA = subtotal*1.21

print ('\n\n \t TICKET DE COMPRAS \t')
print ('-------------------------------------')
print (f'COMPRA: \t \t  {numProd} productos')
print(f'SUBTOTAL: \t \t {subtotal:.2f} pesos')
print('--------------------------------------')
print(f'TOTAL + IVA: \t \t {total_IVA:.2f} pesos\n')
