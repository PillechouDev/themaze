from exceptions import AbstractMethodCallException

class Personnage:
    """ Cette interface représente une personne. Une personne est 'rencontrée' quand on arrive sur la même case
    qu'elle, et on peut lui parler.
    """

    def rencontrer(self, joueur):
        """ Cette méthode est appelée dès que le joueur arrive sur la même case que la personne."""
        raise AbstractMethodCallException() # Méthode abstraite

    def parler(self, joueur):
        """ Cette méthode est appelée lorsque le joueur fait l'action de parler avec la personne."""
        raise AbstractMethodCallException() # Méthode abstraite
        

    def description(self):
        """ Renvoie une description de la personne, pour pouvoir l'afficher. """
        raise AbstractMethodCallException() # Méthode abstraite

    def combattre(self):
        """ Initie un combat """
        raise AbstractMethodCallException()  # Méthode abstraite

    def caresser(self):
        """ Initie un combat """
        raise AbstractMethodCallException()  # Méthode abstraite



