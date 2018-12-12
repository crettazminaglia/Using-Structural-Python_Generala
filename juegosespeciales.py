from cubilete import dame_tirada, generala_servida, escalera_servida, poker_servido, full_servido, lanzamientos_dados
def ordenar_tirada(lanzamientos_dados):
    #Comentario: ordena los dados
    tirada_ordenada=sorted(lanzamientos_dados)
    return tirada_ordenada

#def anotar_juegos_servidos(escalera_servida, poker_servido, full_servido,tirada):
#    if escalera_servida==True or poker_servido==True or full_servido==True:
#       consulta_anotar_juego_servido=input("¿Desea anotar la jugada servida. S/N")
#       if (consulta_anotar_juego_servido.upper() == "S"):
#           return True
#       else:



def anotar_puntos(tirada_ordenada, jugador_uno):
    #jugador_uno = {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", 'E': "", 'F': "", 'P': "", 'G': "",'D': ""}
    if(tirada_ordenada==[1,2,3,4,5] or tirada_ordenada==[2,3,4,5,6]):
        anotar_escalera="20"
        jugador_uno['E']=anotar_escalera
        return print("La tabla de puntaje parcial es", jugador_uno)
    else:
        if (tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[3]==tirada_ordenada[4] or tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[2]==tirada_ordenada[3] and tirada_ordenada[3]==tirada_ordenada[4]):
            anotar_full="30"
            jugador_uno['F']=anotar_full
            return print("La tabla de puntaje parcial es", jugador_uno)
        else:
            if(tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2]and tirada_ordenada[2]==tirada_ordenada[3] or tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[2]==tirada_ordenada[3]and tirada_ordenada[3]==tirada_ordenada[4]):
               anotar_poker= "40"
               jugador_uno['P']=anotar_poker
               return print("La tabla de puntaje parcial es", jugador_uno)
            else:
                if (tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[2]==tirada_ordenada[3] and tirada_ordenada[3]==tirada_ordenada[4]):
                    anotar_generala= "50"
                    jugador_uno['G']=anotar_generala
                    return print("La tabla de puntaje parcial es", jugador_uno)
                else:
                     print("NO TIENE JUEGOS ESPECIALES")
                     anotar_puntos= int(input("Ingrese el número de dado con el que desea anotar. Ingrese 0 si desea tachar una jugada especial o número. " ))
                     if anotar_puntos==0:
                        tachar_jugada= input("Ingrese la inicial de la jugada o número que desea tachar de acuerdo a los que le quedan disponibles")
                        if (tachar_jugada.upper()=="E"):
                            jugador_uno['E']="0"
                            print("La tabla de puntaje parcial es", jugador_uno)
                        else:
                            if (tachar_jugada.upper()=="F"):
                                jugador_uno['F']="0"
                                print("La tabla de puntaje parcial es", jugador_uno)
                            else:
                                if (tachar_jugada.upper()=="P"):
                                    jugador_uno['P']="0"
                                    print("La tabla de puntaje parcial es", jugador_uno)
                                else:
                                    if (tachar_jugada.upper()=="G"):
                                        jugador_uno['G']="0"
                                        print("La tabla de puntaje parcial es", jugador_uno)
                                    else:
                                         if (tachar_jugada.upper()=="D"):
                                            jugador_uno['D']="0"
                                            print("La tabla de puntaje parcial es", jugador_uno)
                                         else:
                                             if (tachar_jugada.upper() == "1"):
                                                 jugador_uno['1'] = "0"
                                                 print("La tabla de puntaje parcial es", jugador_uno)
                                             else:
                                                 if (tachar_jugada.upper() == "2"):
                                                     jugador_uno['2'] = "0"
                                                     print("La tabla de puntaje parcial es", jugador_uno)
                                                 else:
                                                     if (tachar_jugada.upper() == "3"):
                                                         jugador_uno['3'] = "0"
                                                         print("La tabla de puntaje parcial es", jugador_uno)
                                                     else:
                                                         if (tachar_jugada.upper() == "4"):
                                                             jugador_uno['4'] = "0"
                                                             print("La tabla de puntaje parcial es", jugador_uno)
                                                         else:
                                                             if (tachar_jugada.upper() == "5"):
                                                                 jugador_uno['5'] = "0"
                                                                 print("La tabla de puntaje parcial es", jugador_uno)
                                                             else:
                                                                 if (tachar_jugada.upper() == "6"):
                                                                     jugador_uno['6'] = "0"
                                                                     print("La tabla de puntaje parcial es",jugador_uno)
                     else:
                         if anotar_puntos==1:
                           anotar_uno= tirada_ordenada.count(1)
                           anotar= anotar_uno*1
                           jugador_uno['1']= str(anotar)
                           return print("Anota", anotar, "puntos. La tabla de puntaje parcial es", jugador_uno)
                         else:
                            if anotar_puntos==2:
                               anotar_dos= tirada_ordenada.count(2)
                               anotar= anotar_dos*2
                               jugador_uno['2']=str(anotar)
                               return print("Anota", anotar, "puntos. La tabla de puntaje parcial es", jugador_uno)
                            else:
                                if anotar_puntos==3:
                                   anotar_tres= tirada_ordenada.count(3)
                                   anotar= anotar_tres*3
                                   jugador_uno['3']=str(anotar)
                                   return print("Anota", anotar, "puntos. La tabla de puntaje parcial es", jugador_uno)
                                else:
                                    if anotar_puntos == 4:
                                       anotar_cuatro = tirada_ordenada.count(4)
                                       anotar = anotar_cuatro*4
                                       jugador_uno['4']=str(anotar)
                                       return print("Anota", anotar, "puntos. La tabla de puntaje parcial es",jugador_uno)
                                    else:
                                         if anotar_puntos == 5:
                                            anotar_cinco = tirada_ordenada.count(5)
                                            anotar = anotar_cinco*5
                                            jugador_uno['5']=str(anotar)
                                            return print("Anota", anotar, "puntos. La tabla de puntaje parcial es", jugador_uno)
                                         else:
                                             if anotar_puntos == 6:
                                                anotar_seis = tirada_ordenada.count(6)
                                                anotar = anotar_seis*6
                                                jugador_uno['6']=str(anotar)
                                                return print("Anota", anotar, "puntos. La tabla de puntaje parcial es", jugador_uno)


#Prueba del código
#lanzamiento= dame_tirada(6)
#print(lanzamiento)
#evaluar_escalera_servida= escalera_servida(lanzamiento)
#evaluar_poker_servido=poker_servido(lanzamiento)
#evaluar_full_servido=full_servido(lanzamiento)
#evaluar_generala_servida= generala_servida(lanzamiento)
#hola=lanzamientos_dados(lanzamiento)
#tirada=hola
#mostrar_tirada=ordenar_tirada(tirada)
#anotar=anotar_puntos(mostrar_tirada)