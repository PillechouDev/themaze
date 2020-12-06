"""
Permet une seconde chance au joueur sans vie
"""
from objets.machine.Machine import Machine


class QuickRevive(Machine):

    def __init__(self):
        self.prix = 3000

    def acheter(self, joueur, elec):
        if elec.getEtat() == True:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
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
