import random

def jugar(cambia):
    puertas = {1, 2, 3}

    puertaGanadora = random.choice(list(puertas))
    eleccionJugador = random.choice(list(puertas))

    if puertaGanadora == eleccionJugador:
        puertas.remove(puertaGanadora)
        puertaVacia = random.choice(list(puertas))


        gana = not cambia
    else:
        puertas.remove(puertaGanadora)
        puertas.remove(eleccionJugador)
        puertaVacia = puertas.pop()

        gana = cambia

    print(f'Jugador: {eleccionJugador}; Auto: {puertaGanadora}; Vacía: {puertaVacia}; Gana: {gana} (Cambió? {cambia})')

    return gana
        

if __name__ == '__main__':
    tiradas = 5000

    jugadorCambia = [jugar(True) for x in range(1, tiradas + 1)] 
    vecesGanaCambia = [x for x in jugadorCambia if x]

    print(f'Frecuencia cuando cambia:    {len(vecesGanaCambia) / tiradas}')

    jugadorNoCambia = [jugar(False) for x in range(1, tiradas + 1)] 
    vecesGanaNoCambia = [x for x in jugadorNoCambia if x]

    print(f'Frecuencia cuando no cambia: {len(vecesGanaNoCambia) / tiradas}')