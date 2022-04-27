print('\nPROGRAMA QUE MUESTRA SOLO LAS VOCALES DE UNA FRASE\n')
frase = input('Ingrese una frase: ')
vocalesMinus = ['a', 'e', 'i', 'o', 'u']
for char in frase:
    if (char.lower() in vocalesMinus):
        vocal = char
        print (vocal, end = ' ')
print()
