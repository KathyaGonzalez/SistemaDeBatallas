from decorator.luchadorDecorator import LuchadorDecorator
from luchador.luchador import Luchador


class Hechizo(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Hechizo, self).__init__(luchador)

    def get_velocidad(self) -> float:
        return super(Hechizo, self).get_velocidad() * 2.2

    def get_hp(self) -> float:
        return super(Hechizo, self).get_hp() * 0.70
