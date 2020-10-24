"Classe mère perk"
from exceptions import AbstractMethodCallException
""" Cette interface représente un atout que l'on peut acheter et que le joueur peut consommer"""
class perk :
    """ On peut acheter à la machine """
    def acheter(self, joueur):
        """ Cette métode est appellée lorsque le joueur veut acheter un atout"""
        raise AbstractMethodCallException()

