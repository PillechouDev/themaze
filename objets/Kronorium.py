from objet import ObjetRamassable


class Kronorium(ObjetRamassable):

        instance = None

        @staticmethod
        def getInstance():
            if Kronorium.instance is None:
                Kronorium.instance = Kronorium()
            return Kronorium.instance

        def ramasser(self, joueur):
            joueur.mettreObjetDansLeSac(self)

        def description(self):
            return "Livre contenant les récits du passé et du futur"
