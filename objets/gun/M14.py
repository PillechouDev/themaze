from objet import ObjetRamassable

class M14 (ObjetRamassable):

    instance = None

    def getInstance():
        if M14.instance is None:
            M14.instance = M14()
        return M14.instance

    def __init(self):
        damage = 10
        munition = 30

    def description(self):
        return "M14"
