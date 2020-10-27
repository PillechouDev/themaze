
"""
Classe faite par Yohan Widogue
"""

class Electricite():
    """
    Classe pour la machine electricité permettant d'activer les autres machines et voirs tout le labyrinthe , peut en avoir plusieurs
    """
    def __init__(self):
        self._activated = False # Par défaut il est pas activé

    def description(self):
        return "Levier de l'electricité , activé le pour donné le courant aux différentes machines et voir un peu plus claire"

    def utliser(self,labyrinthe):
        """
        Permet d'activer le courant et voir le labyrinthe entier
        :param labyrinthe: L'instance de Labyrinthe
        :return:
        """
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
        """:return: Etat du panneau electrique"""
        return self._activated
