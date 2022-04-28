print ("""
FACTURADOR DE ALMACEN -version 2
Para cada producto comprado, ingrese su precio en pesos 
(valor numerico)""") 

numProd = int(0)
subtotal = 0.0
comprarMas = True
while comprarMas:
    numProd += 1
    while True: 
        precio = input(f'\nPrecio del producto {numProd}: ')
        precio = float(precio)
        if precio > 0:
            break
        else:
            print('Ingrese un precio valido!')
            continue
    subtotal += precio
    while True: 
        resp = input ('Desea comprar algo mas? s/n: ').lower()
        if resp not in ('s','n'):
            print ('Ingrese una opcion valida')
            continue
        else:
            comprarMas = (resp == 's') # Booleano
            break

# Se aplica el IVA sólo al final. Menor costo computacional
total_IVA = subtotal*1.21

print (f"""
\n \t TICKET DE COMPRAS \t
-------------------------------------
COMPRA: \t \t {numProd} productos
SUBTOTAL: \t \t {subtotal:.2f} pesos
--------------------------------------
TOTAL + IVA: \t \t {total_IVA:.2f} pesos
""")
