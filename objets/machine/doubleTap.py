"""
Double dégat sur les armes
"""
from objets.machine.Electricite import Electricite
from objets.machine.Machine import Machine


class DoubleTap(Machine):

    def __init__(self):
        self.prix = 2000

    def description(self):
        return "Une boisson spéciale offrant des capacités supplémentaires (double tap) "
    def ramasser(self, joueur):
        electricite = Electricite()
        if electricite.getEtat() == True or joueur.getArgent() >= self.prix:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
                doubleTap = DoubleTap()
                joueur.mettreObjetDansLeSac(doubleTap)
            else:
                return "Vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."
