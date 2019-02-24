import calculos as calculo
import os
import math
import datetime
import sys

# borrado de pantalla
os.system("clear")

#vamos a usar las funciones de calculo
calculo.suma()
calculo.resta()
calculo.mult()
calculo.div()
calculo.expo()
x=int(input("Numero:"))
y=math.log10(x)
print ("El logaritmo de base 10 de ",x," es " , y , " La fecha de hoy es: " , datetime.date.today())
print ("La ruta de PYTHONPATH:",os.path,"\n") 
