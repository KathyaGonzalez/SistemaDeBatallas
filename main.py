from luchador.luchador import Luchador
from luchador.luchador1 import Luchador1
from luchador.luchador2 import Luchador2
from luchador.luchador3 import Luchador3
from luchador.luchador4 import Luchador4
import random
from typing import List
from decorator.armadura import Armadura
from decorator.escudo import Escudo
from decorator.espada import Espada
from decorator.lanza import Lanza
from decorator.hechizo import Hechizo
from decorator.zapatos import Zapatos
from decorator.pocion import Pocion
from decorator.corona import Corona


opcion: int = 0
items: dict = {
            1: 'Armadura    def +100% || vel -20%',
            2: 'Escudo      def +50%  || atq -10%',
            3: 'Espada      atq +100% || vel -20%',
            4: 'Lanza       atq +50%  || def -5%',
            5: 'Hechizo     vel +120% || hp  -30%',
            6: 'Zapatos     vel +50%  || atq -10%',
            7: 'Pocion      hp  +100% || atq -10%',
            8: 'Corona      hp  +75%  || def -5%'
        }


def combate(personaje1: Luchador, personaje2: Luchador):
    opcion_combate = 0
    orden_ataque: List
    print(f'Velocidad de Jugador 1: {personaje1.get_velocidad()}')
    print(f'Velocidad de Jugador 2: {personaje2.get_velocidad()}')
    if personaje1.get_velocidad() > personaje2.get_velocidad():
        print('Jugador 1 ataca primero')
        orden_ataque: List = [personaje1, personaje2]
    else:
        if personaje1.get_velocidad() == personaje2.get_velocidad():
            aleatorio = random.randint(1, 2)
            if aleatorio == 1:
                orden_ataque: List = [personaje1, personaje2]
                print('Jugador 1 ataca primero (aleatorio)')
            else:
                orden_ataque: List = [personaje2, personaje1]
                print('Jugador 2 ataca primero (aleatorio)')
        else:
            print('Jugador 2 ataca primero')
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


def agregar_decorador(opcion_decorador: int, luchador: Luchador) -> Luchador:
    nuevo_luchador: Luchador
    if opcion_decorador == 1:
        luchador_decorated = Armadura(luchador)
    elif opcion_decorador == 2:
        luchador_decorated = Escudo(luchador)
    elif opcion_decorador == 3:
        luchador_decorated = Espada(luchador)
    elif opcion_decorador == 4:
        luchador_decorated = Lanza(luchador)
    elif opcion_decorador == 5:
        luchador_decorated = Hechizo(luchador)
    elif opcion_decorador == 6:
        luchador_decorated = Zapatos(luchador)
    elif opcion_decorador == 7:
        luchador_decorated = Pocion(luchador)
    else:
        luchador_decorated = Corona(luchador)
    return luchador_decorated


def seleccionar_decorador(luchador: Luchador) -> Luchador:
    continuar: int = 1
    seleccion_items: dict = items.copy()
    while continuar:
        for i in seleccion_items:
            print(f'{i}.-', items[i])
        opcion_item: int = int(input(f'Seleccione el item que desea utilizar: '))
        if seleccion_items.__contains__(opcion_item):
            seleccion_items.pop(opcion_item)
            luchador = agregar_decorador(opcion_item, luchador)
            if len(seleccion_items) == 0:
                continuar = 0
            else:
                continuar = int(input('¿Desea seleccionar otro?\n1.- No\n2.- Si\n: ')) - 1
        else:
            print('Selección no válida')
    return luchador


while opcion != 2:
    print('-----------------------Bienvenido al sistema de ataques B^2----------------------')
    print('1.- Jugar\n2.- Salir')
    opcion = int(input('Digite el número de la opción que desea ejecutar: '))
    if opcion == 1:
        print('---------------------------------------------------------------------------------')
        print('Seleccionar personaje jugador 1')
        print('1. luchador 1\n2. luchador 2\n3. luchador 3\n4. luchador 4')
        opcion_personaje1 = int(input('Ingrese el número de la opción del personaje que desea utilizar el Jugador 1: '))
        opcion_personaje2 = int(input('Ingrese el número de la opción del personaje que desea utilizar el Jugador 2: '))
        personaje_1 = crear_personaje(opcion_personaje1)
        personaje_2 = crear_personaje(opcion_personaje2)
        print('---------------------------------------------------------------------------------')
        print('Seleccion de Items - Jugador 1')
        personaje_1 = seleccionar_decorador(personaje_1)
        print('---------------------------------------------------------------------------------')
        print('Seleccion de Items - Jugador 2')
        personaje_2 = seleccionar_decorador(personaje_2)
        combate(personaje_1, personaje_2)
    elif opcion == 2:
        print('Cerrando sesión...')
    else:
        print('Ingrese una opción válida')
