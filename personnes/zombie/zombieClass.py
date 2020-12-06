"""
CLASSE MERE DES ZOMBIE

"""
from personnage import Personnage
import random

from exceptions import AbstractMethodCallException

from themaze.objets.Chair import Chair


class zombieClass(Personnage):



    def __init__(self):
        """ Constructeur. attribut :
        - vie: les points de vie du zombie
        - dégat: les dégats que le zombie inflige
        - vitesse : vitesse du zombie que l'on compare à celle du joueur pour savoir qui attaque en premier
        - chanceEsquive: plus la chance d'esquiver est faible plus le zombie a de chance d'esquiver la balle
        """
        self._vie = 10
        self._degat = 1
        self._chanceEsquive = 10
        self._mort = False
        self._drop = False

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

    def _perdrevie(self, joueur):
        self._vie -= joueur.degat

    def combattre(self,joueur):
        if self._mort == False:
            print("Vous tentez d'attaquer le zombie")
            """lorsque le joueur attaque, le zombie a une chance d'esquiver la balle
            ici, on considère qu'il a une chance sur 10 d'esquiver la balle"""
            chance = random.randint(1, self._chanceEsquive)
            if chance == 1:
                # le zombie esquive la balle
                print("Le zombie esquive la balle et vous attaque")
                joueur.perdreEnergie(self._degat)
            else:
                # le zombie se prend la balle
                print("le zombie se prend la balle")
                self._perdrevie(joueur)
                if self._vie == 0:
                    print("Vous avez tué le zombie")
                    self._mort = True
                else:
                    """on conidère qu'un zombie a une chance sur deux d'attaquer après s'être prit une balle"""
                    etourdissement = random.randint(1,2)
                    if etourdissement == 1:
                        print("Le zombie est étourdit, il ne vous attaque pas")
                    else:
                        degat = self._degat
                        joueur.perdreEnergie(degat)
                        print("Le zombie vous attaque, il vous enlève votre vie")
        else:
            print("A quoi bon ? Le zombie est déjà mort...")

    def ramasser(self, joueur):
        chair = Chair()
        if self._mort == True and self._drop == False:
            joueur.mettreObjetDansLeSac(chair)
            self._drop = True


