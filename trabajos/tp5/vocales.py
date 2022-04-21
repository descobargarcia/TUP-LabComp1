print('\nPROGRAMA QUE MUESTRA SOLO LAS VOCALES DE UNA FRASE\n')
frase = input('Ingrese una frase: ')
vocalesMinus = ['a', 'e', 'i', 'o', 'u']
vocalesMayus = ['A', 'E', 'I', 'O', 'U']
for char in frase:
    if (char in vocalesMayus or char in vocalesMinus):
        vocal = char
        print (vocal, end = ' ')
print()
