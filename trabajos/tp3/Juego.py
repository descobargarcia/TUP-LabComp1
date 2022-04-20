from random import randint
num_secreto = randint(0,10)
print('\n ADIVINA EL NUMERO SECRETO. TIENES 3 INTENTOS\n')
n1 = int(input('1er intento: '))
if n1 == num_secreto:
    exit('\nADIVINASTE :) \n FIN\n')
elif n1 < num_secreto: 
    print ('Numero muy bajo \n')
else: 
    print ('Numero muy alto \n')
n2 = int(input('2do intento: '))
if n2 == num_secreto:
    exit('\nADIVINASTE :) \n FIN\n')
elif n2 < num_secreto: 
    print ('Numero muy bajo \n')
else: 
    print ('Numero muy alto \n')
n3 = int(input('3er intento: '))
if n3 == num_secreto:
    exit('\nADIVINASTE :) \n FIN\n')
elif n3 < num_secreto: 
    print ('Numero muy bajo \n')
else: 
    print ('Numero muy alto \n')
print (f'PERDISTE :( El num secreto era {num_secreto}\n FIN\n')