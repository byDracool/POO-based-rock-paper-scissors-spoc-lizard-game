from Hand import *
from Resultado_partida import *

class Papel(Hand):

    def name(self):
        return "Papel"

    def jugar(self, bot_hand: Hand):
        return bot_hand.jugar_contra_Papel(Hand)

    def jugar_contra_Piedra(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "pierde"
        resultado_partida.mensaje = "Papel envuelve Piedra"
        return resultado_partida

    def jugar_contra_Papel(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "empate"
        resultado_partida.mensaje = ""
        return resultado_partida

    def jugar_contra_Tijera(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "gana"
        resultado_partida.mensaje = "Tijera corta Papel"
        return resultado_partida

    def jugar_contra_Lagarto(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "gana"
        resultado_partida.mensaje = "Lagarto devora Papel"
        return resultado_partida

    def jugar_contra_Spoc(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "gana"
        resultado_partida.mensaje = "Spoc desautoriza Papel"
        return resultado_partida