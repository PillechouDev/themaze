from objets.machine.Machine import Machine
from labyrinthe.case import Case
from labyrinthe.labyrinthe import Labyrinthe

class Electricite():

    def __init__(self):
        self._activated = False

    def description(self):
        return "Levier de l'electricité , activé le pour donné le courant aux différentes machines et voir un peu plus claire"

    def utliser(self,labyrinthe):
        try:
            for y in range(labyrinthe.tailleY):
                for x in range(labyrinthe.tailleX):
                    labyrinthe.getCase(x, y).decouvrir()
                for x in range(labyrinthe.tailleX):
                    labyrinthe.getCase(x, y).decouvrir()
            self._activated = True
        except:
            print("Le courant n'arrive pas à s'activé , veuillez réessayer")
            self._activated = False


    def getEtat(self):
        return self._activated
