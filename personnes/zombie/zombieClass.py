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

    def _perdrevie(self, degat):
        self.__energie -= degat


    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
    # self._vie = """

    def combat(self,joueur):
        print("Vous tentez d'attaquer le zombie")
        """lorsque le joueur attaque, le zombie a une chance d'esquiver la balle
        ici, on considère qu'il a une chance sur 10 d'esquiver la balle"""
        chance = random.randint(1, self._agilite)
        if chance == 1:
            # le zombie esquive la balle
            print("Le zombie esquive la balle et vous attaque")
            joueur.perdreEnergie(self._degat)
        else:
            # le zombie se prend la balle
            print("le zombie se prend la balle")
            zombieClass._perdrevie(5)
            if zombieClass._vie == 0:
                print("Vous avez tué le zombie")
            else:
                """on conidère qu'un zombie a une chance sur deux d'attaquer après s'être prit une balle"""
                etourdissement = random.randint(1,2)
                if etourdissement == 1:
                    print("Le zombie est étourdit, il ne vous attaque pas")
                else:
                    joueur.perdreEnergie(zombieClass._degat)
                    print("Le zombie vous attaque, il vous enlève votre vie")
