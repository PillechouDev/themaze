from objet import ObjetRamassable

class CleInvoc(ObjetRamassable):

    instance = None

    @staticmethod
    def getInstance():
        if CleInvoc.instance is None:
            CleInvoc.instance = CleInvoc()
        return CleInvoc.instance

    def ramasser(self, joueur):
        """ Met l'objet dans le sac du joueur si il est par terre. """
        joueur.mettreObjetDansLeSac(self)

    def description(self):
        return "ClefInvocation"
