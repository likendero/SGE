from random import *
def generaNumeroAleatorio(minimo,maximo):
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
        return randint(minimo,maximo)
    except TypeError:
        pritn("debes escribir numeros")
        return -1


# incio del programa
numero = generaNumeroAleatorio(1,100)
numero_actual = 0
intentos = 0
print("trata de acertar el numero entre 1 y 100")
while numero_actual != numero:
    try:
        numero_actual = int(input("intro duce un numero: "))
        intentos += 1
        # mensaje segun los posibles casos
        if numero_actual < 1 or numero_actual > 100:
            print("numero fuera de rango")
        elif numero_actual < numero:
            print("el numero es mas grande")
        elif numero_actual > numero:
            print("el numero es mas pequenno")
        else:
            print("has acertado!!!!!")
        print("numero de intentos {}".format(intentos))
    except TypeError:
        print("solo numeros por favor")
        numero_actual = 0
