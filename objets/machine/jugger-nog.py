from objets.machine.Machine import Machine
"""
le joueur à plus de vie
"""

class JuggerNog(Machine):

    def __init__(self):
        self.prix = 2500

    def acheter(self, joueur, elec):
        if elec.getEtat() == True:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
                joueur.setEnergie(joueur.getEnergie()+40)
            else:
                return "Désolé, vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."