"""
Permet une seconde chance au joueur sans vie
"""
from perk import perk


class quickRevive(perk):

    def __init__(self):
        self.prix = 3000
        self.electricity = False  # en attendant le courant

    def acheter(self, joueur):
        if(self.electricity == True):
            if(joueur.argent >= self.prix):
                while joueur.vie >= 0:
                    if(joueur.vie <= 0):
                        joueur.vie = 100  # à modfier plus tard avec les vraies valeurs de joueur
                        break
                    else:
                        continue
            else:
                return "Désolé vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."
