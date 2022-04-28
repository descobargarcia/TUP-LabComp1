from random import randint

listaX = []
listaY = []

for iter in range(100):
    x = randint (-5000, 5000)/1000
    y = 2*x**2 - 10
    y = round (y,3)
    listaX.append(x)
    listaY.append(y)

print(f'\n{listaX= }\n')
print(f'\n{listaY= }\n')
