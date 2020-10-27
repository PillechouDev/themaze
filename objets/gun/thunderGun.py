from objet import ObjetRamassable

class ThunderGun (ObjetRamassable):

    instance = None

    def getInstance():
        if ThunderGun.instance is None:
            ThunderGun.instance = ThunderGun()
        return ThunderGun.instance

    def __init(self):
        damage = 100
        munition = 5

    def description(self):
        return "ThunderGun"
