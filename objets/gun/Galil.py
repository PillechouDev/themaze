from objet import ObjetRamassable

class Galil (ObjetRamassable):

    instance = None

    def getInstance():
        if Galil.instance is None:
            Galil.instance = Galil()
        return Galil.instance

    def __init(self):
        damage = 20
        munition = 40

    def description(self):
        return "Galil"
