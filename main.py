#Comentario1: El código sirve para un solo jugador.
#Comentario2: Se da la bienvenida y se muestran las reglas, si el jugador lo desea.
from rules import rules
from cubilete import dame_tirada, generala_servida, escalera_servida, poker_servido, full_servido, lanzamientos_dados
from juegosespeciales import ordenar_tirada, anotar_puntos #anotar_juegos_servidos
from tablero import chequeador_de_tabla_completa, chequeador_de_juegos
jugador_uno={'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", 'E': "", 'F': "", 'P': "", 'G': "",'D': ""} #Diccionario que contendrá el puntaje del jugador.
#Comentario3: Primer lanzamiento
#tirada_uno = [1, 1, 1, 1, 1] #TIRADA DE PRUEBA PARA GENERALA SERVIDA.
tirada_uno = dame_tirada(6)
#Comentario4: Se evaluan los juegos especiales servidos y los imprime en pantalla al usuario.
#evaluar_generala_servida= generala_servida(tirada_uno)
tabla_completa=chequeador_de_tabla_completa(jugador_uno)
generala_servida=generala_servida(tirada_uno)
while generala_servida!=True and tabla_completa!=True:
        #Comentario5: se consulta si se desea continuar con los lanzamientos, se evalúa la tirada final y se anota el puntaje.
        tirada_uno = dame_tirada(6)
        print(tirada_uno)
        evaluar_escalera_servida= escalera_servida(tirada_uno, jugador_uno)
        evaluar_poker_servido=poker_servido(tirada_uno, jugador_uno)
        evaluar_full_servido=full_servido(tirada_uno, jugador_uno)
        #generala_servida = generala_servida(tirada_uno)
        #evaluar_generala_servida= generala_servida(tirada_uno)
        if evaluar_escalera_servida==True or evaluar_full_servido== True or evaluar_poker_servido==True:
           consulta_anotar_juego_servido = input("¿Desea anotar la jugada servida. S/N")
           if (consulta_anotar_juego_servido.upper() == "S"):
                   print("Siguiente lanzamiento")
                   tirada_uno = dame_tirada(6)
                   print(tirada_uno)
                   #evaluar_escalera_servida = escalera_servida(tirada_uno)
                   #evaluar_poker_servido = poker_servido(tirada_uno)
                   #evaluar_full_servido = full_servido(tirada_uno)
        #tabla_completa=chequeador_de_tabla_completa(jugador_uno)
        #anotar_primera_ronda = anotar_juegos_servidos(evaluar_full_servido, evaluar_poker_servido,evaluar_escalera_servida,tirada_uno)
        lanzamientos= lanzamientos_dados(tirada_uno)
        print(lanzamientos)
        mostrar_tirada=ordenar_tirada(lanzamientos)
        juegos_disponibles=chequeador_de_juegos(jugador_uno)
        anotar=anotar_puntos(lanzamientos, jugador_uno)
        tabla_completa = chequeador_de_tabla_completa(jugador_uno)
        print("Siguiente lanzamiento.")
if generala_servida==True:
    print("ES GENERALA SERVIDA. GANÓ EL JUEGO.")
    print("FIN DEL JUEGO")


