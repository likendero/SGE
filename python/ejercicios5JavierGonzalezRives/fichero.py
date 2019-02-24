# metodo que crea un fichero
def crear_fichero():
    intro = input("intruce un nombre para el fichero .txt : ")
    resultado = None
    if len(intro) > 0:
        intro = "{}.txt".format(intro)
        resultado = open(intro,"w")
        resultado.write("")
    else:
        print("es necesario introducir un numbre");
        
    input("introduzca una tecla para continuar...")
    if resultado is None:
        return resultado
    return intro
# metodo que escribe en el interior de un fichero
def escribir_contenido(fichero = ""):
    if len(fichero) > 0 or fichero is None:
        intro = input("que desea introducir?: ")
        if len(intro) > 0:
            escritor = open(fichero,"a")
            escritor.write("{}\n".format(intro))
        else:
            print("no hay contenido que escribir")
    else:
        print("no se ha creado ningun fichero")
    input("pulse una tecla para continuar...")
# leer contenido del fichero
def leer(fichero = ""):
    if len(fichero) > 0 or fichero is None:
        lector = open(fichero,"r")
        for i in lector.readlines():
            print(i)
    else:
        print("no hay ningun fichero")
    input("pulse una tecla para continuar......................")
def menu():
    print("1. crear un fichero")
    print("2. escribir en el fichero")
    print("3. leer contendio del fichero")
    print("9. salir del programa")
    entrada = 0
    try:
        entrada = int(input("Que deseas hacer: "))
    except:
        print("solo numeros")
        entrada = -1

    return entrada