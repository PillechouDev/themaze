from objet import ObjetRamassable

"""
Classe faite par : Yohan Widogue
"""
class Vodka(ObjetRamassable):
    """ Cette classe représente la bouteille donnée par Nikolia , fait en singleton car il y'a qu'une seule et unique instance sur le jeu """

    instance = None

    @staticmethod
    def getInstance():
        if Vodka.instance is None:
            Vodka.instance = Vodka()
        return Vodka.instance

    def ramasser(self, joueur):
        """ Met l'objet dans le sac du joueur. """
        joueur.mettreObjetDansLeSac(self)

    def description(self):
        return "Vodka"
