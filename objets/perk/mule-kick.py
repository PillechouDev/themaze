"""
Permet de transporter plus d'objet => Inclure limite au sac

"""
from perk import perk

class muleKick(perk):

    def __init__(self):
        self.prix = 2000

    
    def acheter(self, joueur):
        if(joueur.argent >= self.prix):
            joueur.getSac.value += 15 #en admettant que le sac a une taille par défaut, voir dans joueur
        else:
            return "Désolé vous n'avez pas assez d'argent."