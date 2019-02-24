import os
# funciones del programa
# funcion para capturar si o no
def siono():
    while True:
        sn = str(input("seguro que desea borrar(s/n): ")).lower()
        #comprovacion del resultado
        if sn[0] == "s":
            return True
        if sn[0] == "n":
            return False

#funcion para añadir elementos en el diccionario

def annadir_elemento(diccionario = dict()):
    # variable para saber cuantos elementos hay
    numero_elementos = len(diccionario) 
    # captura del valor a introducir
    nuevo_valor = input("que clave deseas introducir: ")

    if len(nuevo_valor) > 0:
        diccionario["valor{}".format(numero_elementos)] = nuevo_valor
        print("introduccion de {1} en {0} se ha realizado con exito".format("valor{}".format(numero_elementos),diccionario["valor{}".format(numero_elementos)]))
    else:
        print("valor no valido, no se ha introducido nada")
    
    input("pulsa una tecla para continudar")
# funcion para borra un elemento del diccionario
def borrar_elemento(diccionario=dict()):
    # captura del valor que se desea eliminar
    numero_elemento = int(input("introduce el numero del elemento que deseas borrar: "))
    # comprovacion de el valor existe en el diccionario
    if "valor{}".format(numero_elemento) in diccionario:
        # si o no para comporvar si se sigue deseando la eliminacion
        if siono():
            diccionario.pop("valor{}".format(numero_elemento))
            mostrar_elementos(diccionario)
    else:
        print("ese elemento no se encuentra en la libreria")
    
def borrar_diccionario(diccionario = dict()):
    # confirmacion del borrado
    if siono():
        diccionario = dict()
        print("borrado relizado con exito")
    return diccionario

# funcion para mostrar elementos del diccionario
def mostrar_elementos(diccionario = dict()):

    for valor,dato in diccionario.items():
        
        print("{} -> {}".format(valor,dato))
    input("pulsa una tecla para continuar...")
#     
def mostrar_inversa(diccionario = dict()):
    contador = len(diccionario)
    print()
    if contador < 1:
        print("no hay elementos")
    else:
        for i in range(contador, -1, -1):
            if diccionario.get(("valor"+str(i))):
                print(("valor"+str(i)+":"),diccionario.get(("valor"+str(i))))

    input("\nPulsa enter para salir de la opcion")
    return


# menu de seleccion
def menu():
    print("MENU")
    print("1. annadir elementos")
    print("2. quitar elemento")
    print("3. mostrar diccionario")
    print("4. borrar diccionario")
    print("5. imprimir inversa")
    print("9. salir")
    seleccion = str(input("cual es su seleccion: "))
    if len(seleccion) == 0 or not seleccion.isdigit():
        return -1
    if int(seleccion) == 9:
        return False
    return int(seleccion)



