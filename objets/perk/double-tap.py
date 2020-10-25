"""
Double dégat sur les armes
"""
from perk import perk

class doubleTap(perk):

    def __init(self):
        self.prix = 2000
        self.electricity = False #En attendant
    
    def acheter(self, joueur):
        if(self.electricity == True): #Dans le cadre où la classe/méthode éléctricité existe.
            if(joueur.argent >= self.prix):
                joueur.degatsArmes *= 2
            else:
                return "Vous n'avez pas assez d'argent." 
        else:
            return "Le courant n'est pas activé."