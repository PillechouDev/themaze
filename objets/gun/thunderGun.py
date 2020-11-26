from gun import Gun


class ThunderGun (Gun):

    def __init(self):
    """ ici on défni les dégats et les munitions de base """
        self.damage = 100
        self.munition = 5

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "ThunderGun (la célèbre arme légendaire !)"

    def getMunition(self):
        """ ici on récupère les munitions """
        return self._munition
