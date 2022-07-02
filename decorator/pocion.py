from decorator.luchadorDecorator import LuchadorDecorator
from Luchador.luchador import Luchador


class Pocion(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Pocion, self).__init__(luchador)

    def get_hp(self) -> float:
        return super(Pocion, self).get_hp() * 2

    def get_atq(self) -> float:
        return super(Pocion, self).get_atq() * 0.90
