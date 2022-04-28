while True:
    palabra = input("\nIngrese una palabra: ")
    palabraMinus = palabra.lower()
    if palabraMinus == "fin":
        break        
    numLetras = len(palabra)
    print(f'{numLetras = }')
print ()
