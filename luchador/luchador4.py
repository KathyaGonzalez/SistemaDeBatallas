from luchador.luchador import Luchador


class Luchador4(Luchador):
    def __init__(self, atq, defensa, velocidad):
        self.__hp: float = 70
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
        if enemy.get_hp() < ((self.get_atq() / enemy.get_def())*5):
            return enemy.get_hp()
        else:
            return (self.get_atq() / enemy.get_def())*5

    def modificar(self, ataque, defensa, velocidad, hp):
        self.__atq = ataque
        self.__def = defensa
        self.__velocidad = velocidad
        self.__hp = hp
