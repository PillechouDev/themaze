
"""

Classe faite par Yohan Widogue
"""
class Config:
    """
    Classe de configuration pour le jeu en singleton car il y'a qu'une seule instence de Config
    """
    instance = None


    @staticmethod
    def getInstance():
        if Config.instance is None:
            Config.instance = Config()
        return Config.instance

    def __init__(self):
        self.difficulte = 1  #Diffuculté du jeu ( 0 easy , 1 normal , 2 hard )


    def getWidth(self):
        """
        :return: Largeur du labyrinthe en fonction de la difficulté
        """
        if self.difficulte ==0:
            return 10
        elif self.difficulte ==1:
            return 20
        elif self.difficulte == 2:
            return 30

    def getHeight(self):
        """
        :return: Hauteur du labyrinthe en fonction de la difficulté
        """
        if self.difficulte == 0:
            return 5

        elif self.difficulte == 1:
            return 10

        elif self.difficulte == 2:
            return 25

    def getMaxEnergie(self):
        """
        :return: Le maximum d'énérgie que le joueur peut avoir de base
        """
        if self.difficulte == 0:
            return 80
        elif self.difficulte == 1:
            return 70
        elif self.difficulte == 2:
            return 60

    def showMenu(self,joueur):
        """
        Permet d'afficher le menu des paramètres
        :param joueur: Le joueur
        :return: Menu de config
        """
        print('PARAMETRE DE JEU : \n ______________\n')
        print("1.Difficulté")
        print("2.Pseudo")
        try:
            choix=int(input("\nVotre choix ?"))
            if choix == 1:
                print('Difficulté : \n ______________\n')
                print("0.Facile")
                print("1.Moyen")
                print("2.Difficile")
                choix=int(input())
                if 2 >= choix >= 0:
                    self.difficulte=choix
                else:
                    raise ValueError
            elif choix == 2:
                joueur.setNom(str(input("Veuillez saisir votre pseudo : ")))
            else:
                raise ValueError
        except ValueError:
            print("Entrez une valeur correct")
            self.showMenu(joueur)
