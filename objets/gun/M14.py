from objet import ObjetRamassable

class M14(ObjetRamassable):

    def __init__(self):
        """ ici on défni les dégats et les munitions de base """
        self.damage = 10
        self.munition = 30

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "M14 (un fusil tactique très célèbre)"

    def getMunition(self):
        """ ici on récupère les munitions """
        return self._munition
