import abc


class Luchador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_velocidad(self) -> float:
        pass

    @abc.abstractmethod
    def get_hp(self) -> float:
        pass

    @abc.abstractmethod
    def get_atq(self) -> float:
        pass

    @abc.abstractmethod
    def get_def(self) -> float:
        pass

    @abc.abstractmethod
    def reduce_hp(self, damage: float):
        pass
