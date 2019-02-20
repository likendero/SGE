from math import log10
# metodo que sirver para introducir dos numeros
def introducir_numeros():
    # bloque try que controla los posibles errores que hallan sucedido
    try:
        numero1 = int(input("introduzca el primer numero: "))
        numero2 = int(input("introduzca el segundo numero: "))
    except ValueError:
        print("se ha introducido un valor distinto a un numero")
        return 0,0
    return numero1,numero2


#funcion que suma dos numeros pasados por teclado
def sumar():
    # introduccion de los numeros
    numero1,numero2 = introducir_numeros()
    # realizacion de la suma
    print("suma {} + {} = {}".format(numero1,numero2,(numero1 + numero2))) 
# caso de restar
def resta():
    # introduccion de los numeros
    numero1,numero2 = introducir_numeros()
    # realizacion de la suma
    print("resta {} - {} = {}".format(numero1,numero2,(numero1 - numero2))) 
# caso de dividir
# el segundo numero no puede ser 0
def division():
    # introduccion de los numeros
    numero1,numero2 = introducir_numeros()
    # realizacion de la suma
    if numero2 != 0:
        print("division {} / {} = {}".format(numero1,numero2,(numero1 / numero2)))
    else:
        print("error, division por 0")

# caso de multiplicacion
def multiplicar():
    # introduccion de los numeros
    numero1,numero2 = introducir_numeros()
    # realizacion de la suma
    print("multiplicacion {} * {} = {}".format(numero1,numero2,(numero1 * numero2))) 

# caso de exponente
def exponente():
    # introducir numeros
    numero1,numero2 = introducir_numeros()
    # salida de la potencia
    print("potencia {} ^ {} = {} ".format(numero1,numero2,(numero1**numero2)))
# caso de logaritmo
def logaritmo():
    try:
        numero1 = input("introduce un numero")
    except ValueError:
        print("solo se pueden introducir numeros")
    # salida de la potencia
    print("logaritmo base 10 de {} es {}".format(numero1,log10(2)))