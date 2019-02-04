# numero de datos en la lista
rango = int(input("numero de palabras que poner en la lista: "))
if rango > 0:
    # lista que mas tarde se mostrara
    lista =  []
    # bucle que funciona mientras haya elementos
    while len(lista) < rango:
        lista.append(input("introduce una palabra "))
    print("la lista es: {}".format(lista) )
    print("la lista inversa es: {}".format(list(reversed(lista)) ))
else:
    print("el numero de elementos tiene que se superior a 0")


    
