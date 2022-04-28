from random import uniform as ru

listaX = []
listaY = []
listaXred = []
listaYred= []

for iter in range(100):
    x = ru (-5, 5)
    y = 2*x**2 - 10
    listaX.append(x)
    listaY.append(y)

for index in range(len(listaX)):
    listaXred.append(float("%.2f" %listaX[index]))
    listaYred.append(float("%.2f" %listaY[index]))

print(listaXred)
print(listaYred)

