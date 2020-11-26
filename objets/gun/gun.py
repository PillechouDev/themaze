from exceptions import AbstractMethodCallException
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
        """ Cette méthode est appelée lorsque le joueur utilise un objet. """
        raise AbstractMethodCallException() # Méthode abstraite

    def getDamage(self, joueur):
        """ Verifie si le joueur à l'atout double tap qui permet de doubler les dégats """
        for t in joueur.getAtout():
            if t == "doubleTap":
                return self._damage * 2
            else:
                return self._damage
