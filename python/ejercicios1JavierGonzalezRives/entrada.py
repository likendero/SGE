num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))
nombre = input("introduce tu nombre: ")
# comprovaciones para la salida
if num1 > num2:
    print("{} es mayor que {}".format(num1,num2))
elif num2 > num1:
    print("{} es mayor que {}".format(num2,num1))
else:
    print("{} son iguales {}".format(num1,num2))

print("Tu nombre es: {}".format(nombre))
