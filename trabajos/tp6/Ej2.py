from random import uniform as ru

listaX = []
listaY = []
listaXred = []
listaYred= []

for iter in range(100):
    x = ru (-5, 5)
    y = 2*x**2 - 10
    xRed = round (x, 2)
    yRed = round (y, 2)
    listaX.append(x)
    listaY.append(y)
    listaXred.append(xRed)
    listaYred.append(yRed)

print(f'\n{listaXred= }\n')
print(f'\n{listaYred= }\n')

