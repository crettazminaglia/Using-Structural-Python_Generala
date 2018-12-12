def rules():
    leer_reglas= input("BIENVENIDO AL JUEGO DE LA GENERALA ¿Desea leer las reglas de juego? S/N ")
    if (leer_reglas.upper() == "S"):
        print ("La GENERALA es un juego de dados que consiste en adquirir la mayor cantidad de puntaje de acuerdo "+'\n'+
               "a las reglas preestablecidas. Se juega con 5 dados y pueden lanzarse como máximo 3 veces, todos ellos"+'\n'+
               "o la cantidad que deseee. Al finalizar los lanzamientos podrá optar en anotar puntos de acuerdo a los"+'\n'+
               "juegos especiales o puntaje de los dados. Los juegos especiales son: GENERALA si todos los dados son iguales,"+'\n'+
               "GENERALA SERVIDA si ocurre en el primer intento y permite finalizar el juego siendo el ganador quien obtuvo este juego,"+'\n'+
               "GENERALA DOBLE si ocurre dos veces durante el juego, POKER si hay 4 dados iguales"+'\n'+
               "FULL si se forman dos grupos de dados iguales, ESCALERA si la serie de dados es consecutiva. El puntaje de los"+'\n'+
               "dados ocurre cuando no hay juegos especiales y el usuario anota el valor del dado x la cantidad de dados de ese valor."+'\n'+
               "También, puede optarse por tachar alguno de los números o juegos especiales obteniendo el valor de cero.")
        print("Iniciar juego")
    else:
        print ("Iniciar juego")
#Prueba de codigo
reglas_de_juego=rules()
