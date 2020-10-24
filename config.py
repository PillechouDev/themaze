

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

    def showMenu(self):
        print('ceci est menu de Manu')
