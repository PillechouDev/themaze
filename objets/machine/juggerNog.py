from objets.machine.Machine import Machine
from objets.machine.Electricite import Electricite

"""
le joueur à plus de vie
Faite par Legrand Mathieu
"""

class JuggerNog(Machine):

    def __init__(self):
        self.prix = 2500

    def description(self):
        return "Une boisson spéciale offrant des capacités supplémentaires (jugger nog) "

    def ramasser(self, joueur):
        #electricite = Electricite()
        print(joueur.getArgent())
        if joueur.getArgent() >= self.prix:
            # Dans le cadre où la classe/méthode éléctricité existe.
            print("yes")
            joueur.removeArgent(self.prix)
            print(joueur.getEnergie())
            joueur.setEnergie(joueur.getEnergie()+25)
            print(joueur.getEnergie())
        else:
            return "Vous n'avez pas assez d'argent"