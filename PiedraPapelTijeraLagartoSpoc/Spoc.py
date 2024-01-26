from Hand import *
from Resultado_partida import *

class Spoc(Hand):

    def name(self):
        return "Spoc"

    def jugar(self, bot_hand: Hand):
        return bot_hand.jugar_contra_Spoc(Hand)

    def jugar_contra_Piedra(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "pierde"
        resultado_partida.mensaje = "Spoc vaporiza Piedra"
        return resultado_partida

    def jugar_contra_Papel(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "gana"
        resultado_partida.mensaje = "Spoc desautoriza Papel"
        return resultado_partida

    def jugar_contra_Tijera(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "pierde"
        resultado_partida.mensaje = "Spoc rompe Tijera"
        return resultado_partida

    def jugar_contra_Lagarto(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "gana"
        resultado_partida.mensaje = "Lagarto envenena Spoc"
        return resultado_partida

    def jugar_contra_Spoc(self, bot_hand: Hand):
        resultado_partida = Resultado_partida()
        resultado_partida.resultado = "empate"
        resultado_partida.mensaje = ""
        return resultado_partida