from Luchador.Luchador import Luchador
from Luchador.Luchador1 import Luchador1
from Luchador.Luchador2 import Luchador2
from Luchador.Luchador3 import Luchador3
from Luchador.Luchador4 import Luchador4
import random
from typing import List


opcion: int = 0


def combate(personaje1: Luchador, personaje2: Luchador):
    opcion_combate = 0
    orden_ataque: List
    if personaje1.get_velocidad() > personaje2.get_velocidad():
        orden_ataque: List = [personaje1, personaje2]
    else:
        if personaje1.get_velocidad() == personaje2.get_velocidad():
            aleatorio = random.randint(1, 2)
            if aleatorio == 1:
                orden_ataque: List = [personaje1, personaje2]
            else:
                orden_ataque: List = [personaje2, personaje1]
        else:
            orden_ataque: List = [personaje2, personaje1]
    while opcion_combate != 2:
        print('---------------------------------------------------------------------------------')
        print('1. Atacar\n2. Salir')
        opcion_combate = int(input('Ingrese la opción: '))
        if opcion_combate == 1:
            primero = orden_ataque.__getitem__(0)
            segundo = orden_ataque.__getitem__(1)
            segundo.reduce_hp(primero.compute_damage(segundo))
            primero.reduce_hp(segundo.compute_damage(primero))
            print('---------------------------------------------------------------------------------')
            print(f'Personaje 1 -> Puntos de vida: {primero.get_hp()}')
            print(f'Personaje 2 -> Puntos de vida: {segundo.get_hp()}')
            if primero.get_hp() == 0:
                print('---------------------------------------------------------------------------------')
                print(f'Partida terminada - Ha muerto {primero.__class__.__name__} (Jugador 1)')
                print(f'Ganador: {segundo.__class__.__name__} (Jugador 2)')
                opcion_combate = 2
            if segundo.get_hp() == 0:
                print('---------------------------------------------------------------------------------')
                print(f'Partida terminada - Ha muerto {segundo.__class__.__name__} (Jugador 2)')
                print(f'Ganador: {primero.__class__.__name__} (Jugador 1)')
                opcion_combate = 2
        else:
            print('Terminando combate...')


def crear_personaje(opcion_personaje: int) -> Luchador:
    if opcion_personaje == 1:
        return Luchador1(30, 40, 30)
    elif opcion_personaje == 2:
        return Luchador2(40, 22, 25)
    elif opcion_personaje == 3:
        return Luchador3(40, 10, 63)
    elif opcion_personaje == 4:
        return Luchador4(50, 35, 21)


while opcion != 2:
    print('-----------------------Bienvenido al sistema de ataques B^2----------------------')
    print('1.- Jugar\n2.- Salir')
    opcion = int(input('Digite el número de la opción que desea ejecutar: '))
    if opcion == 1:
        print('---------------------------------------------------------------------------------')
        print('Seleccionar personaje jugador 1')
        print('1. Luchador 1\n2. Luchador 2\n3. Luchador 3\n4. Luchador 4')
        opcion_personaje1 = int(input('Ingrese el número de la opción del personaje que desea utilizar el Jugador 1: '))
        opcion_personaje2 = int(input('Ingrese el número de la opción del personaje que desea utilizar el Jugador 2: '))
        personaje_1 = crear_personaje(opcion_personaje1)
        personaje_2 = crear_personaje(opcion_personaje2)
        combate(personaje_1, personaje_2)
    elif opcion == 2:
        print('Cerrando sesión...')
    else:
        print('Ingrese una opción válida')
