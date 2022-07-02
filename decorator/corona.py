from decorator.luchadorDecorator import LuchadorDecorator
from Luchador.luchador import Luchador


class Corona(LuchadorDecorator):
    def __init__(self, luchador: Luchador):
        super(Corona, self).__init__(luchador)

    def get_hp(self) -> float:
        return super(Corona, self).get_hp() * 1.75

    def get_def(self) -> float:
        return super(Corona, self).get_def() * 0.95
