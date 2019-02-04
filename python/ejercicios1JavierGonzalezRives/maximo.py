# introduccion de los numeros
a = int(input("introduce el primer numero:"))
b = int(input("introduce el segundo numero:"))
nombre = input("introduce tu nombre: ")
if a != b:
    print("el mayor entre {} y {} es ".format(a,b), end="")
    if a > b:
        print(a)
    elif b > a:
        print(b)
else:
    print("{} y {} son iguales".format(a,b))
    

print("mi nombre es Javier Gonzalez Rives")
