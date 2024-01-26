from __future__ import annotations
from abc import ABC, abstractmethod
from Hand import *
from Resultado_partida import *


class Hand(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def jugar(self, bot_hand: Hand) -> Resultado_partida:
        pass

    @abstractmethod
    def jugar_contra_Piedra(self, bot_hand: Hand) -> Resultado_partida:
        pass

    @abstractmethod
    def jugar_contra_Papel(self, bot_hand: Hand) -> Resultado_partida:
        pass

    @abstractmethod
    def jugar_contra_Tijera(self, bot_hand: Hand) -> Resultado_partida:
        pass

    @abstractmethod
    def jugar_contra_Lagarto(self, bot_hand: Hand) -> Resultado_partida:
        pass

    @abstractmethod
    def jugar_contra_Spoc(self, bot_hand: Hand) -> Resultado_partida:
        pass
















