from objets.gun.gun import Gun


class L96A1(Gun):

    def __init(self):
        """ ici on défni les dégats et les munitions de base """
        self._damage = 50
        self._munition = 10

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "L96A1 (un sniper très puissant de calibre 7,62)"

    def getMunition(self):
        """ ici on récupère les munitions """
        return self._munition
