"""
CLASSE MERE DES ZOMBIE

"""

import random
from themaze.personnes.zombie.zombieClass import zombieClass


class Zombie(zombieClass):
    """ Cette classe représente un zombie classique. Le zombie attaque le joueur. Les intéractions sociales entre le joueur et le zombie
    sont limitées du fait que le zombie et par définition violent et dénué de parole"""
    def __init__(self):
        super().__init__()


    def description(self):
        """ Renvoie la description du zombie."""
        if self._mort == False:
            return "Un zombie vous regarde alléché"
        else:
            return "Un cadavre de zombie"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        if self._mort == False:
            discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
            print("Un zombie " + " " + discours[random.randint(0, 3)])
            input()
        else:
            return "Rien ne se passe"


    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        if self._mort == False:
            print("Le zombie ne semble pas vous écouter")
        else:
            print("Vous tentez de parler à un cadavre... Il est temps que vous sortiez de ce labyrinthe")





