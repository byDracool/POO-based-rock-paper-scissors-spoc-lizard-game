from Jugador import *
import os


class Jugador_Humano(Jugador):
    nombre = str

    def jugar(self):
        os.system("cls")
        print("\nElige tu mano:\n")
        for hand in enumerate(Jugador.hand_types):
            print(hand[0], hand[1])
        player_hand = Jugador.hand_types[(int(input("Seleccion: ")))]
        return super().from_str_to_hand(player_hand)

