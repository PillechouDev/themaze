"Classe mère machine"
from exceptions import AbstractMethodCallException

""" Cette interface représente un atout que l'on peut acheter et que le joueur peut consommer"""

class Machine:
    """ On peut acheter à la machine """
    def description(self):
        return "Je vois une machine étrange..."

    def ramasser(self, joueur):
        """ Cette métode est appellée lorsque le joueur veut acheter un atout"""
        return "Vous avez utilisé machine étrange"
