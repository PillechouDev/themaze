"""
Double dégat sur les armes
"""
from objets.machine.Electricite import Electricite
from objets.machine.Machine import Machine


class DoubleTap(Machine):

    def __init__(self):
        self.prix = 2000

    def ramasser(self, joueur):
        electricite = Electricite()
        if electricite.getEtat() == True:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
                joueur.addAtout("doubleTap")
            else:
                return "Vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."
