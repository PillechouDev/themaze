"""
Double dégat sur les armes
"""
from perk import perk

class doubleTap(perk):

    def __init(self):
        self.prix = 2000

    
    def acheter(self, joueur):
        if(joueur.argent >= self.prix):
            joueur.degatsArmes *= 2
        else:
            return "Vous n'avez pas assez d'argent." 