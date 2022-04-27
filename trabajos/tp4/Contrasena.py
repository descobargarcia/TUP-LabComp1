pass1 = input("\nIngrese su contraseña: ")
intentos = 1
while (intentos <=3):
    pass2 = input("\nConfirme su contraseña: ")
    if pass2 == pass1:
        exit ("\nACCESO CORRECTO")
    print ("Contraseña invalida")
    intentos += 1
print ("\nACCESO DENEGADO")

