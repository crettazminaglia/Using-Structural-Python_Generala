import random


def dame_un_dado():
    return random.randrange(1, 7)


def dame_tirada(cantidad_dados):  # La cantidad de dados es igual al número de dados que el usuario elige+1.
    # Comentario: esta función sirve para generar una lista de números al azar.
    tirada = []
    for dado in range(1, cantidad_dados):
        tirada.append(dame_un_dado())
    return sorted(tirada)


def generala_servida(tirada):
    # Comentario: esta función sirve para evaluar si hay generala servida. Si sale, finaliza el juego.
    if (tirada[0] == tirada[1] and tirada[1] == tirada[2] and tirada[2] == tirada[3] and tirada[3] == tirada[4]):
        #print("ES GENERALA SERVIDA. GANÓ EL JUEGO.")
        return True
    else:
        print("NO TIENE GENERALA SERVIDA.")
        return False


def escalera_servida(tirada, jugador_uno):
    # Comentario: esta función sirve para evaluar si hay escalera servida. Suma 25 puntos.
    #jugador_uno = {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", 'E': "", 'F': "", 'P': "", 'G': "", 'D': ""}
    if (sorted(tirada) == [1, 2, 3, 4, 5] or sorted(tirada) == [2, 3, 4, 5, 6]):
        anotar_escalera = "25"
        jugador_uno['E']=anotar_escalera
        print("ES ESCALERA SERVIDA. Anota 25 puntos.La tabla de puntaje parcial es", jugador_uno)
        return True
    else:
        print("NO TIENE ESCALERA SERVIDA.")
        return False


def poker_servido(tirada, jugador_uno):
    # Comentario: esta función sirve para evaluar si hay poker servida. Suma 45 puntos.
    #jugador_uno = {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", 'E': "", 'F': "", 'P': "", 'G': "", 'D': ""}
    if (sorted(tirada)[0] == sorted(tirada)[1] and sorted(tirada)[1] == sorted(tirada)[2] and sorted(tirada)[2] ==
            sorted(tirada)[3] or sorted(tirada)[1] == sorted(tirada)[2] and sorted(tirada)[2] == sorted(tirada)[
                3] and sorted(tirada)[3] == sorted(tirada)[4]):
        anotar_escalera = "45"
        jugador_uno['P']=anotar_escalera
        print("ES POKER SERVIDO. Anota 45 puntos.La tabla de puntaje parcial es", jugador_uno)
        return True
    else:
        print("NO TIENE POKER SERVIDO.")
        return False


def full_servido(tirada, jugador_uno):
    # Comentario: esta función sirve para evaluar si hay full servido. Suma 35 puntos.
    #jugador_uno = {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", 'E': "", 'F': "", 'P': "", 'G': "", 'D': ""}
    if (sorted(tirada)[0] == sorted(tirada)[1] and sorted(tirada)[1] == sorted(tirada)[2] and sorted(tirada)[3] ==
            sorted(tirada)[4] or sorted(tirada)[0] == sorted(tirada)[1] and sorted(tirada)[2] == sorted(tirada)[
                3] and sorted(tirada)[3] == sorted(tirada)[4]):
        anotar_escalera = "35"
        jugador_uno['F']=anotar_escalera
        print("ES FULL SERVIDO. Anota 35 puntos.La tabla de puntaje parcial es", jugador_uno)
        return True
    else:
        print("NO TIENE FULL SERVIDO.")
        return False

def lanzamientos_dados(tirada):
    pregunta = input("¿Desea realizar un segundo lanzamiento? S/N ")
    if (pregunta.upper() == "S"):
        cantidad_dados = int(input("¿Cuántos dados desea volver a lanzar? "))
        dados_elegidos = []
        for i in range(1, (6 - cantidad_dados)):
            pregunta2 = int(input("Seleccione el dado ELEGIDO " + str(i) + " "))
            dados_elegidos.append(pregunta2)
        dados_rechazados = []
        for i in range(1, (cantidad_dados + 1)):
            pregunta3 = int(input("Seleccione el dado que desea LANZAR " + str(i) + " "))
            dados_rechazados.append(pregunta3)
        segundo_lanzamiento = dame_tirada(len(dados_rechazados) + 1)
        dados_candidatos = segundo_lanzamiento + dados_elegidos
        #print("Los dados seleccionados son" + str(dados_elegidos))
        #print("Los dados rechazados son" + str(dados_rechazados))
        print("Su segundo lanzamiento es", dados_candidatos)             # out put segundo lanzamiento
        pregunta_dos = input("¿Desea realizar un tercer lanzamiento? S/N ")
        if (pregunta_dos.upper() == "S"):
            cantidad_dados = int(input("¿Cuántos dados desea volver a lanzar? "))
            dados_elegidos = []
            for i in range(1, (6 - cantidad_dados)):
                pregunta2 = int(input("Seleccione el dado ELEGIDO " + str(i) + " "))
                dados_elegidos.append(pregunta2)
            dados_rechazados = []
            for i in range(1, (cantidad_dados + 1)):
                pregunta3 = int(input("Seleccione el dado que desea LANZAR " + str(i) + " "))
                dados_rechazados.append(pregunta3)
            segundo_lanzamiento = dame_tirada(len(dados_rechazados) + 1)
            dados_candidatos = segundo_lanzamiento + dados_elegidos
            print("Su tercer y último lanzamiento es", dados_candidatos)       # out-put tercer lanzamiento
            return dados_candidatos
        else:
            return dados_candidatos
    else:
        return tirada

# Prueba del código
#lanzamiento= dame_tirada(6)       #Se debe agregar el número de dados a lanzar.
#evaluar_generala_servida= generala_servida(lanzamiento)
#print(lanzamiento)
#hola=lanzamientos_dados(lanzamiento)
#print(hola)
