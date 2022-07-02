from Luchador.luchador import Luchador


class LuchadorDecorator(Luchador):
    def __init__(self, luchador: Luchador):
        self.luchador: Luchador = luchador
        self.atq = None

    def get_atq(self) -> float:
        return self.luchador.get_atq()

    def get_hp(self) -> float:
        return self.luchador.get_hp()

    def get_def(self) -> float:
        return self.luchador.get_def()

    def get_velocidad(self) -> float:
        return self.luchador.get_velocidad()

    def reduce_hp(self, damage: float):
        self.luchador.reduce_hp(damage)

    def compute_damage(self, enemy: Luchador):
        return self.luchador.compute_damage(enemy)

    def modificar(self, ataque, defensa, velocidad):
        pass
