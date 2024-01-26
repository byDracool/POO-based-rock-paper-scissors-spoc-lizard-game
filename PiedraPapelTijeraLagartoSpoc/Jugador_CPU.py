from Jugador import *
import random


class Jugador_CPU(Jugador):
    nombre = str

    def jugar(self):
        random_hand = random.randint(0, (len(Jugador.hand_types)) - 1)
        bot_hand = Jugador.hand_types[random_hand]
        return super().from_str_to_hand(bot_hand)