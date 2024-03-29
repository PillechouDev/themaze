import random

from exceptions import AbstractMethodCallException
from objets.gun.M14 import M14
from objets.gun.Galil import Galil
from objets.gun.L96A1 import L96A1
from objets.gun.thunderGun import ThunderGun

class Boite:

    def __init(self):
        self.prix = 950

    def description(self):
        return "ceci est la fameuse boite magique"

    def ramasser(self, joueur):
        """ Cette métode est appellée lorsque le joueur veut utiliser la boite"""

        if joueur.removeArgent(950):

            contenus = ['M14 (fusil tactique)', 'L96A1 (sniper)', 'Galil', 'ThunderGun', 'rien du tout']
            print("vous avez eu :"+ contenus[random.randint(0,4)])
            if contenus == 'M14 (fusil tactique)':
                m14 = M14()
                joueur.mettreObjetDansLeSac(m14)

            elif contenus == 'L96A1 (sniper)':
                l96a1 = L96A1()
                joueur.mettreObjetDansLeSac(l96a1)

            elif contenus == 'Galil':
                galil = Galil()
                joueur.mettreObjetDansLeSac(galil)

            elif contenus == 'ThunderGun':
                thundergun = ThunderGun()
                joueur.mettreObjetDansLeSac(thundergun)

            elif contenus == 'rien du tout':
                print("vous vous etes bien fais avoir par cette foutue boite ...")
        else:
            print("vous n'avez pas assez d'argent")
            input()
