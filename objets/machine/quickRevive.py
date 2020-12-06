"""
Permet une seconde chance au joueur sans vie
"""
from objets.machine.Machine import Machine
from objets.machine.Electricite import Electricite

class QuickRevive(Machine):

    def __init__(self):
        self.prix = 3000


    def description(self):
        return "Une boisson spéciale offrant des capacités supplémentaires (quick revive) "

    def ramasser(self, joueur):
        #electricite = Electricite()
        print(joueur.getArgent())
        if joueur.getArgent() >= self.prix:  # Dans le cadre où la classe/méthode éléctricité existe.
            joueur.removeArgent(self.prix)
            print("yes")
            while joueur.vie >= 0:
                if(joueur.vie <= 0):
                    joueur.vie = 100  # à modfier plus tard avec les vraies valeurs de joueur
                    break
                else:
                    continue
        else:
            return "Vous n'avez pas assez d'argent"
