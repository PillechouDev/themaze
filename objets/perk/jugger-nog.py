from perk import perk
"""
le joueur à plus de vie
"""

class juggerNog(perk):

    def __init__(self):
        self.prix = 2500


    def acheter(self, joueur):
        if(joueur.argent >= self.prix):
            joueur.vie *= 2
        else:
            return "Désolé, vous n'avez pas assez d'argent."