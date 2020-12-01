from objet import ObjetRamassable


class Katana(ObjetRamassable):
    instance = None

    @staticmethod
    def getInstance():
        if Katana.instance is None:
            Katana.instance = Katana()
        return Katana.instance

    def ramasser(self, joueur):
        # Met l'objet dans le sac du joueur
        joueur.mettreObjetDansLeSac(self)

    def description(self):
        return "Katana appartenant à Takéo"
