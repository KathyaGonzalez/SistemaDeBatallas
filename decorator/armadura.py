from decorator.luchadorDecorator import LuchadorDecorator
from luchador.luchador import Luchador


class Armadura(LuchadorDecorator):
    # Aumenta una estadistica y disminuye otra
    def __init__(self, luchador: Luchador):
        super(Armadura, self).__init__(luchador)

    def get_def(self) -> float:
        return super(Armadura, self).get_def() * 2

    def get_velocidad(self) -> float:
        return super(Armadura, self).get_velocidad() * 0.8
