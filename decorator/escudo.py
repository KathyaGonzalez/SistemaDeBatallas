from decorator.luchadorDecorator import LuchadorDecorator
from Luchador.luchador import Luchador


class Escudo(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Escudo, self).__init__(luchador)

    def get_def(self) -> float:
        return super(Escudo, self).get_def() * 1.5

    def get_atq(self) -> float:
        return super(Escudo, self).get_atq() * 0.9
