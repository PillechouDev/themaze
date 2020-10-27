from objet import ObjetRamassable

class L96A1 (ObjetRamassable):

    instance = None


    def getInstance():
        if L96A1.instance is None:
            L96A1.instance = L96A1()
        return L96A1.instance

    def __init(self):
        damage = 50
        munition = 10

    def description(self):
        return "L96A1 (sniper)"
