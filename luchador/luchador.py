from __future__ import annotations
import abc


class Luchador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_velocidad(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_hp(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_atq(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_def(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def reduce_hp(self, damage: float):
        raise NotImplementedError

    @abc.abstractmethod
    def compute_damage(self, enemy: Luchador):
        raise NotImplementedError
