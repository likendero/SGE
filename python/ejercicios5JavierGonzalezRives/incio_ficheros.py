import fichero as fich
import os
fichero = None
control = True;

while control:
    os.system("clear")
    seleccion = fich.menu()
    os.system("clear")
    # crear el fichero
    if seleccion == 1:
        fichero = fich.crear_fichero()
    elif seleccion == 2:
        fich.escribir_contenido(fichero)
    elif seleccion == 3:
        fich.leer(fichero)
    elif seleccion == 9:
        seleccion == 9
        control = False