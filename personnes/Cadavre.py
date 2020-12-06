from personnage import Personnage
import random

"""
Classe faite par : Yohan Widogue
"""


class Cadavre(Personnage):
    """
    Classe d'un cadavre , que l'on peux fouiller , c'est un personnage mais qui ne bouge pas
    """

    def __init__(self):
        self._argent = random.randint(0, 500)  # Un cadavre porte alétoirement de l'argent sur lui
        self.__fouille=False #Booleen permettant de savoir si il est déja fouillé ou non
    def rencontrer(self, joueur):
        """Phase de rencontre avec le joueur"""
        print("Vous trouvez un cadavre par terre\nVoulez-vous le fouillez ? (oui/non)")
        if not self.__fouille:
            try:
                imput = str(input())  # On force le string
                if (imput == "oui"):
                    self.fouiller(joueur)
                elif (imput == "non"):
                    print("D'accord vous ne voulez pas le fouiller")
                else:
                    print("Je n'ai pas bien compris veuillez reessayer")
                    self.rencontrer(joueur)
            except:
                # Gestion des erreur en général
                print("Je n'ai pas bien compris veuillez reessayer")
                self.rencontrer(joueur) #Relance de la méthode
        elif self.__fouille:
            print("Vous avez déja fouillé ce cadavre ! ")

    def parler(self, joueur):
        """Un cadavre ca parle ? """
        print("...")

    def description(self):
        """Renvoie une description"""
        return "Un cadavre puant"

    def fouiller(self, joueur):
        """Methode pour fouiller un cadavre"""
        try:
            print("Le cadavre possède " + str(self._argent) + " $")
            joueur.addArgent(self._argent)
            print("Vous possédez " + joueur._argent + " $")
            self._argent = 0 #Mise à zero pour le cadavre
            self.__fouille=True #Le cadavre à été fouillé et dépouillé
        except:
            pass
