import random

"Funcion para simular una tirada del Monty Hall"
def simularJugada(jugadorCambia, imprimirResultado = True):
    puertas = {1, 2, 3}

    puertaGanadora = random.choice(list(puertas))
    eleccionJugador = random.choice(list(puertas))

    if puertaGanadora == eleccionJugador:
        puertas.remove(puertaGanadora)
        puertaVacia = random.choice(list(puertas))

        if jugadorCambia:
            puertas.remove(puertaVacia)
            puertaCambio = puertas.pop()

            gana = False
        else:
            gana = True

    else:
        puertas.remove(puertaGanadora)
        puertas.remove(eleccionJugador)
        puertaVacia = puertas.pop()

        if jugadorCambia:
            puertaCambio = puertaGanadora
            gana = True
        else:
            gana = False

    if imprimirResultado:
        print(f'Concurso de Monty Hall:')
        print(f'Puerta elegida por el participante: {eleccionJugador}')
        print(f'Puerta abierta por el presentador:  {puertaVacia}')
        print(f'Puerta donde está el auto:          {puertaGanadora}')
        if jugadorCambia:
            print(f'Jugador cambia a:                   {puertaCambio}')
        print(f'Resultado:                          {"Gana" if gana else "Pierde"}')

    return gana


"Funcion para calcular las frecuencias sin imprimir todo el monty hall en cada tirada"
def calcularFrecuenciaDeVictorias(numeroDeTiradas, jugadorCambia):
    victorias = 0
    for _ in range(numeroDeTiradas):
        jugadorGana = simularJugada(jugadorCambia, imprimirResultado=False)
        if jugadorGana:
            victorias += 1
    
    return victorias / numeroDeTiradas


"Funcion Main del programa"
if __name__ == '__main__':
    simularJugada(True)
    print(f'')
    simularJugada(False)
    print(f'')
    for tiradas in [1_000, 10_000, 100_000]:
        print(f'Tiradas: {tiradas}')
        print(f' - Frecuencia cuando cambia:    {calcularFrecuenciaDeVictorias(tiradas, True)}')
        print(f' - Frecuencia cuando no cambia: {calcularFrecuenciaDeVictorias(tiradas, False)}')
