from gun import Gun

class Galil (Gun):

    def __init(self):
        """ ici on défni les dégats et les munitions de base """
        self.damage = 20
        self.munition = 40

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "Galil (un fusil d'assault puissant de calibre 5,56)"

    def getMunition(self):
        """ ici on récupère les munitions """
        return self._munition
