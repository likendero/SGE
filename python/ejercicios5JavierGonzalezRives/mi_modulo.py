# Javier Gozalez Rives
def columnitas(pal1, pal2):
    
    if len(pal1) != len(pal2):
        maslargo = max(len(pal1),len(pal2))      
        pal1 = pal1.ljust(maslargo)        
        pal2 = pal2.ljust(maslargo)
    for a, b in zip(pal1, pal2):
        print(a, b)
columnitas("Hola", "mundo")
