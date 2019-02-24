import os
import ejercico2 as ejer

control = True
diccionario = dict()
while control:
    os.system("clear")
    seleccion = ejer.menu()
    os.system("clear")
    if seleccion == False:
        control = seleccion
        # anandir un elemento
    elif seleccion == 1:
        ejer.annadir_elemento(diccionario)
        # borrar un elemento
    elif seleccion == 2:
        ejer.borrar_elemento(diccionario)
        # mostrar elementos
    elif seleccion == 3:
        ejer.mostrar_elementos(diccionario)
        # borrar el diccionario
    elif seleccion == 4:
        diccionario = ejer.borrar_diccionario(diccionario)
    elif seleccion == 5:
        ejer.mostrar_inversa(diccionario);
    else:
        print("opccion no valida o implementada")


print("programa realizado por Javier Gonazalez Rives")