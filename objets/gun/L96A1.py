from objet import ObjetRamassable



class L96A1(ObjetRamassable):

    def __init(self):
        self._damage = 50
        self._munition = 10

    def description(self):
        return "L96A1 (sniper)"

    def getDamage(self, joueur):
        for t in joueur.getAtout():
            if t == "doubleTap":
                return self._damage * 2
            else:
                return self._damage

    def getMunition(self):

        return self._munition
