from perk import perk
"""
le joueur à plus de vie
"""

class juggerNog(perk):

    def __init__(self):
        self.prix = 2500
        self.electricity = False


    def acheter(self, joueur):
        if(self.electricity == True): #En attendant
            if(joueur.argent >= self.prix):
                joueur.vie *= 2
            else:
                return "Désolé, vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."