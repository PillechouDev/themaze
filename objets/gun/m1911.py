"""Arme de départ contenant 1 balle """
from gun import Gun
    """ Class M1911 représente une arme que l'on peut ramasser et que le joueur peut transporter et utiliser à partir de son sac """
class M1911(Gun):

    def __init(self):
    """ ici on défni les dégats et les munitions de base """
        self._damage = 5
        self._munition = 1

    def description(self):
    """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "L96A1 (une petit arme de poing banal)"

    def getMunition(self):
    """ ici on récupère les munitions """
        return self._munition
