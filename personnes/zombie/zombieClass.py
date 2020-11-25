"""
CLASSE MERE DES ZOMBIE

"""
from personnage import Personnage
import random

from themaze.exceptions import AbstractMethodCallException


class zombieClass(Personnage):



    def __init__(self):
        """ Constructeur. attribut :
        - vie: les points de vie du zombie
        - dégat: les dégats que le zombie inflige
        - vitesse : vitesse du zombie que l'on compare à celle du joueur pour savoir qui attaque en premier
        - agilité: plus l'agilité est faible plus le zombie a de chance d'esquiver la balle (voir la méthode esquive)
        """
        self._vie = 10
        self._degat = 1
        self._vitesse = 1
        self._agilite = 10

    def rencontrer(self, joueur):
        """ Cette méthode est appelée dès que le joueur arrive sur la même case que la personne."""
        raise AbstractMethodCallException()  # Méthode abstraite

    def parler(self, joueur):
        """ Cette méthode est appelée lorsque le joueur fait l'action de parler avec la personne."""
        raise AbstractMethodCallException()  # Méthode abstraite

    def description(self):
        """ Renvoie une description de la personne, pour pouvoir l'afficher. """
        raise AbstractMethodCallException()  # Méthode abstraite


    def attaquer(self, joueur):
        """le zombie attaque le joueur selon ses dégâts"""
        joueur.perdreEnergie(self._degat)

    def esquive(self, joueur):
        """lorsque le joueur attaque, le zombie a une chance d'esquiver la balle
        ici, on considère qu'il a une chance sur 10 d'esquiver la balle"""
        chance = random.randint(1, self._agilite)
        if chance == 1:
            # le zombie esquive la balle
            print("le zombie esquive la balle")
        else:
            # le zombie se prend la balle
            print("le zombie se prend la balle")

    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
    # self._vie = """

    def combat(self,joueur):
        #todo : Systeme de combat