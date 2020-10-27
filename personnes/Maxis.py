from objets import Cleinvoc
from objets.Katana import Katana
from objets.ObjetRichto import ObjetRichto
from objets.Vodka import Vodka
from personnage import Personnage


class Maxis(Personnage):
    """ Cette classe représente Maxis , après avoir parler et récupérer tout les objets des 4 personnage , donne fin au jeu, fait en singleton car il y'a qu'une seule instance sur le jeu """
    instance = None

    @staticmethod
    def getInstance():
        if Maxis.instance is None:
            Maxis.instance = Maxis()
        return Maxis.instance

    def __init__(self):
        """
        Les attribut permettent de savoir si le joueur ramenne bien les objets à Maxis
        """
        self.nikolai= False
        self.dempsey= False
        self.takeo= False
        self.richtofen=False


    def description(self):
        return "Maxis"

    def rencontrer(self, joueur):
        print("Maxis : J'attendais ta venue "+joueur.getNom()+ ", as-tu tous les objets de ceux fameux personanage? ")
        sac = joueur.getSac()
        entree = input("#>")
        if entree in ['o', 'O', 'OUI', 'oui']:
            print("Mmmmm ... Voyons voir ca !")

            # On fait une condition pour savoir si le sac est vide afin de ne pas boucler sur du vide
            if (len(sac)) == 0:
                print("Mais ton sac est vide , tu n'a pas le droit de me mentir ! \n")
            elif(len(sac)) >0:
                for obj in sac:
                    """
                    Ici on boucle pour savoir si les intence son présent dans le sac
                    """
                    if obj == Vodka.getInstance():
                        self.nikolai=True
                        print("Tu as la bouteille de vodka de Nikolai ! Il à sombrée dans l'alcool à cause de son désespoir ! ")
                    elif obj ==Katana.getInstance():
                        self.takeo=True
                        print("Le katana de Takeo , remplie d'histoire sombre")
                    elif obj == Cleinvoc.getInstance():
                        self.dempsey=True
                        print("La clé d'invocation ! Piece maitresse de tout une oeuvre ! ")
                    elif obj == ObjetRichto.getInstance():
                        self.richtofen=True
                        print(ObjetRichto.getInstance().description)

            if self.richtofen ==True and self.dempsey==True and self.takeo==True and self.nikolai==True:
                #Si tout les objets ont été récolté alors c'est la fin de la partie
                print("Oh tu ma tout trouvé merci beaucoup")
                #TODO : END GAME

        elif entree in['n','N',"non",'NON']:
            print("Alors dans ce cas je te laisse chercher les autres ! ")
        else:
            print("Je n'ai pas bien compris , bon reviens me voirs quand tu sera plus compréhensible")
