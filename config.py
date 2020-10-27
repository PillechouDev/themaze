from joueur import Joueur


class Config:
    """
    Classe de configuration pour le jeu
    """
    instance = None


    @staticmethod
    def getInstance():
        if Config.instance is None:
            Config.instance = Config()
        return Config.instance

    def __init__(self):
        self.difficulte = 1  #Diffuculté du jeu ( 0 easy , 1 normal , 2 hard )



    def setDifficult(self,difficult):
        self.difficulte=difficult


    def getWidth(self):
        if self.difficulte ==0:
            return 10
        elif self.difficulte ==1:
            return 20
        elif self.difficulte == 2:
            return 30

    def getHeight(self):
        if self.difficulte == 0:
            return 5

        elif self.difficulte == 1:
            return 10

        elif self.difficulte == 2:
            return 25

    def getMaxEnergie(self):
        if self.difficulte == 0:
            return 80
        elif self.difficulte == 1:
            return 70
        elif self.difficulte == 2:
            return 60

    def showMenu(self,joueur):
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




"""j = Joueur("f",70)
Config.getInstance().showMenu(j)
print(j.getNom())"""