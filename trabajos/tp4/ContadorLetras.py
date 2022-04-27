while True:
    palabra = input("\nIngrese una palabra: ").lower()
    if palabra == "fin":
        break        
    numLetras = len(palabra)
    print(f'{numLetras = }')
print ()
