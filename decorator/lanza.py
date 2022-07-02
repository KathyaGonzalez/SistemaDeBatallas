from decorator.luchadorDecorator import LuchadorDecorator
from Luchador.luchador import Luchador


class Lanza(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Lanza, self).__init__(luchador)

    def get_atq(self) -> float:
        return super(Lanza, self).get_atq() * 1.5

    def get_def(self) -> float:
        return super(Lanza, self).get_def() * 0.95
