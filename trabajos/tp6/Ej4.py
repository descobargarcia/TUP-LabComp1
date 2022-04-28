#4. A partir de dos listas A y B, generar dos nuevas listas: una de ellas llamada 
# “intersección” con los elementos presentes en A y en B, la otra llamada “restante” 
# que tenga los elementos de A y B que no están en ambas listas.

#Listas:
#A = [1,2,3,4,5,6], B = [2,3,4,10,11,12] 
#Resultado:
#intersección = [2,3,4] 
#restante = [1,5,6,10,11,12]

A = [1,2,3,4,5,6]
B = [2,3,4,10,11,12]
Intersec = []
Restantes = []

for elemA in A:
    for elemB in B:
        if elemA == elemB:
            Intersec.append(elemA)

for elem in A:
    if elem not in Intersec:
        Restantes.append(elem)

for elem in B:
    if elem not in Intersec:
        Restantes.append(elem)

print(f'{Intersec= }')
print(f'{Restantes= }')
