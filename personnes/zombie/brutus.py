import random
from themaze.personnes.zombie.zombieClass import zombieClass
from labyrinthe.labyrinthe import Case


class Brutus(zombieClass):
    """ Cette classe représente un gullum. Le gullum est un zombie infligeant plus de dégat mais ayant moins de vie. """
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

    def avancerNord(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertNord():
            self.setCaseCourante(caseCourante.getCaseNord())


    def avancerSud(self):
        print("test")
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertSud():
            self.setCaseCourante(caseCourante.getCaseSud())


    def avancerEst(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertEst():
            self.setCaseCourante(caseCourante.getCaseEst())


    def avancerOuest(self):
        caseCourante = self.__caseCourante
        if caseCourante.estOuvertOuest():
            self.setCaseCourante(caseCourante.getCaseOuest())


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





