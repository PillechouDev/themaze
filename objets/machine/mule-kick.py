"""
Permet de transporter plus d'objet => Inclure limite au sac

"""
from objets.machine.Machine import Machine

class muleKick(Machine):

    def __init__(self):
        self.prix = 2000

    def acheter(self, joueur, elec):
        if elec.getEtat() == True:  # Dans le cadre où la classe/méthode éléctricité existe.
            if joueur.removeArgent(self.prix):
                joueur.getSac.value += 15 #en admettant que le sac a une taille par défaut, voir dans joueur
            else:
                return "Désolé vous n'avez pas assez d'argent."
        else:
            return "Le courant n'est pas activé."