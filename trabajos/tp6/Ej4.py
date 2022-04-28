A = [1,2,3,4,5,6]
B = [2,3,4,10,11,12]
Intersec = []
Restantes = []

for elem in A:
    if elem in B:
        Intersec.append(elem)

for elem in A:
    if elem not in Intersec:
        Restantes.append(elem)

for elem in B:
    if elem not in Intersec:
        Restantes.append(elem)

print(f'{Intersec= }')
print(f'{Restantes= }')
