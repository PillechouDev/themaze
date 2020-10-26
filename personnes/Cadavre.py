from personnage import Personnage
import random


class Cadavre(Personnage):
    """
    Classe d'un cadavre , que l'on peux fouiller , c'est un personnage mais qui ne bouge pas
    """

    def __init__(self):
        self._argent = random.randint(0, 500)
        # self._arme = [] #En attendant les armes

    def rencontrer(self, joueur):
        """Phase de rencontre avec le joueur"""
        print("Vous trouvez un cadavre par terre\nVoulez-vous le fouillez ? (oui/non)")
        try:
            imput = input()
            if (imput == "oui"):
                self.fouiller(joueur)
            elif (imput == "non"):
                print("D'accord vous ne voulez pas le fouiller")
            else:
                print("Je n'ai pas bien compris veuillez reessayer")
                self.rencontrer(joueur)
        except ValueError:
            print("Je n'ai pas bien compris veuillez reessayer")
            self.rencontrer(joueur)

    def parler(self, joueur):
        """Un cadavre ca parle ? """
        print("...")

    def description(self):
        """Renvoie une description"""
        return "Un cadavre puant"

    def fouiller(self, joueur):
        """Methode pour ajouter l'argent au joueur"""
        print("Le cadavre possède " + str(self._argent) + " $")
        joueur.addArgent(self._argent)
        print("Vous possédez " + joueur._argent + " $")
        self._argent = 0
