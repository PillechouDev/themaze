import random
from personnes.zombie.zombieClass import zombieClass

"""
Classe faite par : Romain 
"""

class Gullum(zombieClass):
    """ Cette classe représente un gullum. Le gullum est un zombie infligeant plus de dégat mais ayant moins de vie. """
    def __init__(self):
        super().__init__()
        self._vie = 50
        self._degat = 3
        self._chanceEsquive = 7
        self._mort = False


    def description(self):
        """ Renvoie la description du gullum."""
        if self._mort == False:
            return "Un gullum vous observe"
        else:
            return "Un cadavre de gullum"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        if self._mort == False:
            discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
            print("Un gullum " + " " + discours[random.randint(0, 3)])
            print("Un combat se lance")
            self.combattre(joueur)
        else:
            print("Un gollum mort")


    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        if self._mort == False:
            print("Le gullum ne semble pas vous écouter")
        else:
            print("Vous tentez de parler à un cadavre... Il est temps que vous sortiez de ce labyrinthe")





