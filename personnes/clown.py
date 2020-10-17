from personnage import Personnage
import random

class Clown(Personnage):
    """ Cette classe représente un clown qui raconte des blagues au joueur lorsqu'il arrive sur la même case
    Le clown a une humeur et si celle-ci est triste, il retire de l'énergie au joueur. """

    def __init__(self, humeur):
        """ Constructeur. Paramètres :
        - humeur : humeur du clown (chaine de caractères)
        """
        self._humeur = humeur

    def description(self):
        """ Renvoie la description du clown."""
        return "Un clown " + self._humeur

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur."""
        if self._humeur == "heureux":
            discours = " souhaite vous faire rire"
        elif self._humeur == "triste":
            discours = " souhaite vous faire du mal"
        print("Un clown "+self._humeur + discours)
        input()

    def parler(self, joueur):
        """ Le clown dit des blagues aléatoire s'il est d'humeur heureuse """
        if self._humeur == "heureux":
            print("Clown "+self._humeur+": Pouet pouet je suis un petit blagueur ! Veux tu une blague? [O/N]")
            entree = input("#>")
            if entree in ['O', 'o', 'OUI', 'oui', 'Oui', 'OUi']:
                blague = ["pouet", "paf", "pif"]
                print("Clown " + self._humeur + ": " + blague[random.randint(0,len(blague) - 1)])
            else:
                print("Clown " + self._humeur + ": Snif...")
                self._humeur = "triste"

        else:
            print("Clown " + self._humeur + ": Snif...")