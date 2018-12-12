jugador_uno = {'1': "", '2': "", '3': "2", '4': "", '5': "2", '6': "2", 'E': "5", 'F': "2", 'P': "2", 'G': "2",'D': "2"}

def chequeador_de_tabla_completa(jugador_uno):
    tabla_completa = True
    for tablas in jugador_uno:
        if(len(jugador_uno[tablas])==0):
            tabla_completa = False
            return tabla_completa
    return tabla_completa

def chequeador_de_juegos(jugador_uno):
    for valor in jugador_uno:
        if jugador_uno[valor]=="":
            print("El juego o número disponible para anotar es", valor)


#Prueba de código
#tablero=chequeador_de_tabla_completa(jugador_uno)
#juegos=chequeador_de_juegos(jugador_uno)
#print(tablero)


