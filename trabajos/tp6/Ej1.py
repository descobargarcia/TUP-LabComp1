#Shortcut: List Comprehension
#listaNum = [num for num in range(0,100,6)]

#Equivalente a:
listaNum = []
for num in range (100):
    if num%2 == 0 and num%3 ==0:
        listaNum.append(num)

print(f'{listaNum}')
