import os
import random
from Resultado_partida import *
from Hand import *
from Jugador_Humano import *
from Jugador_CPU import *



def get_result(resultado):
    if resultado == "gana":
        print("Enhorabuena, has ganado la partida")
    elif resultado == "empate":
        print("Empate")
    else:
        print("Perdiste, intentalo de nuevo")





def main():
    print("\nBienvenido al juego\n")
    print("Piedra, Papel, Tijera, Lagarto, Spoc\n"
          "*by Sheldon Cooper\n")
    while True:
        game_selection = input("[1] Jugar\n"
                                    "[Q] Salir\n"
                                    "Su seleccion: ")
        if game_selection == 1:
            jugador1 = Jugador_Humano()
            jugador2 = Jugador_CPU()
            hand1 = jugador1.jugar()
            hand2 = jugador2.jugar()
            print (f"\n{hand1.name()} vs {hand2.name()}\n")
            resultado_partida = hand1.jugar(hand2)
            print(resultado_partida.mensaje)
            print (resultado_partida.resultado + "\n")


        elif game_selection == "Q":
            exit()
        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()