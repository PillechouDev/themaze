"""
Permet de transporter plus d'objet => Inclure limite au sac

"""
from objets.machine.Machine import Machine
from objets.machine.Electricite import Electricite


class MuleKick(Machine):

    def __init__(self):
        self.prix = 2000

    def description(self):
        return "Une boisson spéciale offrant des capacités supplémentaires (mule kick) "

    def ramasser(self, joueur):
        electricite = Electricite()

        if electricite.getEtat() == True or joueur.getArgent() >= self.prix:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
                joueur.getSac.value += 15 #en admettant que le sac a une taille par défaut, voir dans joueur
            else:
                return "Désolé vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."