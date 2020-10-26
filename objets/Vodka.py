from objet import ObjetRamassable


class Vodka(ObjetRamassable):
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
