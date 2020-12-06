import random
from personnes.zombie.zombieClass import zombieClass
from labyrinthe.labyrinthe import Case

from themaze.joueur import Joueur

"""
Classe faite par : Mathieu et Romain 
"""

class Brutus(zombieClass):
    """ Cette classe représente un Brutus. Le brutus est un zombie se déplaçant seul. """
    def __init__(self):
        super().__init__()
        self.__caseCourante = Case()
        self._vie = 5
        self._degat = 3
        self._chanceEsquive = 7
        self._mort = False

    def getCaseCourante(self):
        return self.__caseCourante

    def setCaseCourante(self, case):
        self.__caseCourante.supprimerBrutus()
        self.__caseCourante = case
        case.ajouterBrutus(self)

    def avancerAleatoirement(self):
        caseCourante = self.__caseCourante
        print(caseCourante)
        deplacement = random.randint(0,3)
        if deplacement == 0:
            if caseCourante.estOuvertNord():
                self.setCaseCourante(caseCourante.getCaseNord())
                print("déplacé nord")
            else:
                deplacement += 1

        elif deplacement == 1:

            if caseCourante.estOuvertSud():
                self.setCaseCourante(caseCourante.getCaseSud())
                print("déplacé sud")

            else:

                deplacement += 1

        elif deplacement == 2:

            if caseCourante.estOuvertEst():
                self.setCaseCourante(caseCourante.getCaseEst())
                print("déplacé Est")

            else:

                deplacement += 1

        elif deplacement == 3:

            if caseCourante.estOuvertOuest():
                self.setCaseCourante(caseCourante.getCaseOuest())
                print("déplacé Ouest")

            else:

                deplacement = 0




    def avancerNord(self):
        caseCourante = self.__caseCourante
        print(caseCourante)
        if caseCourante.estOuvertNord():
            self.setCaseCourante(caseCourante.getCaseNord())
            print("déplacé nord")
    def avancerSud(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertSud():
            self.setCaseCourante(caseCourante.getCaseSud())
            print("déplacé sud")

    def avancerEst(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertEst():
            self.setCaseCourante(caseCourante.getCaseEst())
            print("déplacé Est")

    def avancerOuest(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertOuest():
            self.setCaseCourante(caseCourante.getCaseOuest())
            print("déplacé Ouest")

    def description(self):
        """ Renvoie la description du brutus."""
        if self._mort == False:
            return "Un zombie immense vous court après"
        else:
            return "Un cadavre de brutus"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        if self._mort == False:
            discours = ['vous charge', 'crie', 'vous cours dessus', 'hurle']
            print("Un Brutus " + " " + discours[random.randint(0, 3)])
            input()
        else:
            return "Rien ne se passe"


    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        if self._mort == False:
            print("Le brutus tape sur le mur")
        else:
            print("Vous tentez de parler à un cadavre... Il est temps que vous sortiez de ce labyrinthe")





