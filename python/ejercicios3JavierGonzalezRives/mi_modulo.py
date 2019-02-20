import calculos as calc
from os import system
import os
from datetime import date

# ejercicio 1
calc.sumar()
calc.resta()
calc.multiplicar()
calc.division()
calc.exponente()
input("pulsa una tecla para continuar con el ejercicio 2 ...")
# ejercicio 2
system("clear")
calc.logaritmo()
hoy = date.today()
print("hoy es: {}".format(hoy))
print("directorios de python: {}".format(os.sys.path))
