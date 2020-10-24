"""
CLASSE MERE DES ZOMBIE

"""
from personnage import Personnage
import random

class MobZombie(Personnage):
    """ Cette classe représente un zombie classique. Le zombie attaque le joueur. Les intéractions sociales entre le joueur et le zombie
    sont limitées du fait que le zombie et par définition violent et dénué de parole"""

    def __init__(self):
        """ Constructeur. Paramètres :
        - vie: les points de vie du zombie
        - dégat: les dégats que le zombie inflige
        """
        self._vie = 20
        self._degat = 5

    def description(self):
        """ Renvoie la description du zombie."""
        return "Un zombie vous regarde alléché"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
        print("Un zombie " + " " + discours[random.randint(0,3)])
        input()

    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        print("Le zombie ne semble pas vous écouter")

    def attaquer(self, joueur):
        joueur.perdreEnergie(self._degat)

    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
        # self._vie = """
