from abc import ABC, abstractmethod
from Piedra import *
from Papel import *
from Tijera import *
from Lagarto import *
from Spoc import *
from Hand import *

class Jugador(ABC):
    nombre = str
    hand_types = ["Tijera", "Papel", "Piedra", "Lagarto", "Spoc"]

    @abstractmethod
    def jugar(self) -> Hand:
        pass

    def from_str_to_hand (self, mano):
        if mano == "Tijera":
            return Tijera()
        elif mano == "Piedra":
            return Piedra()
        elif mano == "Papel":
            return Papel()
        elif mano == "Lagarto":
            return Lagarto()
        elif mano == "Spoc":
            return Spoc()
        raise ValueError