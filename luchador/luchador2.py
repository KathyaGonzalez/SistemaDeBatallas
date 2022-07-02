from luchador.luchador import Luchador


class Luchador2(Luchador):
    def __init__(self, atq, defensa, velocidad):
        self.__hp: float = 85
        self.__atq: float = atq
        self.__def: float = defensa
        self.__velocidad: float = velocidad

    def get_velocidad(self) -> float:
        return self.__velocidad

    def get_hp(self) -> float:
        return self.__hp

    def get_atq(self) -> float:
        return self.__atq

    def get_def(self) -> float:
        return self.__def

    def reduce_hp(self, damage: float):
        self.__hp -= damage

    def compute_damage(self, enemy: Luchador) -> float:
        if enemy.get_hp() < (self.get_atq() - enemy.get_def()):
            return enemy.get_hp()
        elif enemy.get_def() > self.get_atq():
            return self.get_atq() * 0.5
        else:
            return self.get_atq() - enemy.get_def()

    def modificar(self, ataque, defensa, velocidad):
        self.__atq = ataque
        self.__def = defensa
        self.__velocidad = velocidad
