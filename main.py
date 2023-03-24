import random

def simularJugada(jugadorCambia):
    puertas = {1, 2, 3}

    puertaGanadora = random.choice(list(puertas))
    eleccionJugador = random.choice(list(puertas))

    if puertaGanadora == eleccionJugador:
        puertas.remove(puertaGanadora)
        puertaVacia = random.choice(list(puertas))

        gana = not jugadorCambia
    else:
        puertas.remove(puertaGanadora)
        puertas.remove(eleccionJugador)
        puertaVacia = puertas.pop()

        gana = jugadorCambia

    # print(f'Jugador: {eleccionJugador}; Auto: {puertaGanadora}; Vacía: {puertaVacia}; Gana: {gana} (Cambió? {cambia})')

    return gana


def calcularFrecuenciaDeVictorias(numeroDeTiradas, jugadorCambia):
    victorias = 0
    for _ in range(numeroDeTiradas):
        if simularJugada(jugadorCambia):
            victorias += 1
    
    return victorias / numeroDeTiradas


if __name__ == '__main__':
    for tiradas in [1_000, 10_000, 100_000]:
        print(f'Tiradas: {tiradas}')
        print(f' - Frecuencia cuando cambia:    {calcularFrecuenciaDeVictorias(tiradas, True)}')
        print(f' - Frecuencia cuando no cambia: {calcularFrecuenciaDeVictorias(tiradas, False)}')