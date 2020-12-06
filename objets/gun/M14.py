from objets.gun.gun import Gun

"""Class M14 représente un objet que l'on peut ramasser et que le joueur peut transporter et utiliser à partir de son sac"""

class M14 (Gun):

    def __init__(self):
        """ ici on défni les dégats et les munitions de base """
        self.damage = 10
        self._munition = 30

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        return "M14 (un fusil tactique très célèbre)"

    def getMunition(self):
        """ ici on récupère les munitions """
        return self._munition
