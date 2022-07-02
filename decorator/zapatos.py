from decorator.luchadorDecorator import LuchadorDecorator
from Luchador.luchador import Luchador


class Zapatos(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Zapatos, self).__init__(luchador)

    def get_velocidad(self) -> float:
        return super(Zapatos, self).get_velocidad() * 1.5

    def get_atq(self) -> float:
        return super(Zapatos, self).get_atq() * 0.9
