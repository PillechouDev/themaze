from exceptions import AbstractMethodCallException
from joueur import Joueur
"""
Class mère Gun représente un objet que l'on peut ramasser et que le joueur peut transporter et utiliser à partir de son sac

.._|\______________ _,,_
.../ `-------- ' --------|
./_==©__'______-___ _|
.. ),---.(_(__) /
..// (\) ),----".'.
//___//
`------

"""

class Gun:

    def ramasser(self, joueur):
        """ Met l'objet dans le sac du joueur. """
        joueur.mettreObjetDansLeSac(self)

    def description(self):
        """ Renvoie une description de l'objet, pour pouvoir l'afficher. """
        raise AbstractMethodCallException() # Méthode abstraite

    def utiliser(self, joueur):
        joueur = Joueur()
        """ Cette méthode est appelée lorsque le joueur utilise un objet. """
        choix = input("souhaitez-vous equiper l'arme [o/n]")
        if choix in ['o', 'O', 'OUI', 'oui']:
            joueur.degat = joueur.degat + self.damage
        else : print("vous n'avez equipé aucune arme")

    def getDamage(self, joueur):
        joueur = Joueur()
        """ Verifie si le joueur à l'atout double tap qui permet de doubler les dégats """
        for t in joueur.getAtout():
            if t == "doubleTap":
                return self._damage * 2 + joueur.degat
            else:
                return self._damage + joueur.degat
