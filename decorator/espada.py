from decorator.luchadorDecorator import LuchadorDecorator
from luchador.luchador import Luchador


class Espada(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Espada, self).__init__(luchador)

    def get_atq(self):
        return super(Espada, self).get_atq() * 2

    def get_velocidad(self) -> float:
        return super(Espada, self).get_velocidad() * 0.8
