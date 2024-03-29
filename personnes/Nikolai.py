from objets.Vodka import Vodka
from personnage import Personnage
import random


"""
Classe faite par Yohan Widogue
"""
class Nikolai(Personnage):
    """ Cette classe représente Nikolai Belinski un des 4 personnages à rencontrer pour finir le jeu , fait en singleton car il y'a qu'une seule instance sur le jeu """

    instance = None

    @staticmethod
    def getInstance():
        """
        :return: Instance de Nikolai
        """
        if Nikolai.instance is None:
            Nikolai.instance = Nikolai()
        return Nikolai.instance

    def __init__(self):
        self.__argent = False # Permet de savoir si l'argent est déjà donnée dans l'easter egg

    def description(self):
        """Retourne la description"""
        return "Nikolai Belinski"

    def rencontrer(self, joueur):
        """Lors de la rencontre un discours aléatoire est prononcé"""
        discours = ["Nikolai est plus fort qu'une muraille , hé sa rime ! ", "Vodka pour tout le monde !", "On boit de la vodka ce soiiiiiir !"]
        print("Nikolai : "+ discours[random.randint(0,2)])


    def parler(self, joueur):
        """Permet de lancer un dialogue entre le joueur et Nikolai et de récupérer l'object"""
        sac = joueur.getSac()
        #On fait une condition pour savoir si le sac est vide afin de ne pas boucler sur du vide
        if (len(sac)) == 0:
            print("Nikolai : Faut que j'arrête de boire... Tiens ma vodka c'est ma dernière")
            entree = input("#> Voulez vous prendre sa vodka ? [o/n]")
            if entree in ['o', 'O', 'OUI', 'oui']:
                joueur.mettreObjetDansLeSac(Vodka.getInstance())  #Mise en place de l'instance dans le sac
                print("vous avez à present une bouteille de vodka dans votre sac")
            elif entree in ['n','N','NON','non']:
                print("vous avez refusé l'objet")
            else:
                print("Je n'ai pas compris camarade ! ")
                self.parler(joueur) #Relance de la methode
        else:
            #si le sac n'est pas vide, on fait une boucle pour savoir si la bouteille est déjà présente
            obtenu = False
            for obj in sac:
                if obj == Vodka.getInstance():
                    obtenu = True

            if obtenu == True and self.__argent is False:
                print("Salut camarade , je viens de donner ce que j'avais ... \n Oh mince peut être que le Capitalisme te met dans le rouge ? \n Tiens voici 500 $")
                joueur.addArgent(500)
                self.__argent = True
            elif obtenu == True and self.__argent is True:
                print("Salut camarade , je viens de donner ce que j'avais ... \n et en plus tu m'as ruinée")
            else:
                print("Nikolai : Faut que j'arrête de boire... Tiens ma vodka c'est ma dernière")
                entree = input("#> Voulez vous prendre sa vodka ? [o/n]")
                if entree in ['o', 'O', 'OUI', 'oui']:
                    joueur.mettreObjetDansLeSac(Vodka.getInstance())  # Mise en place de l'instance dans le sac
                    print("vous avez à present une bouteille de vodka dans votre sac")
                elif entree in ['n', 'N', 'NON', 'non']:
                    print("vous avez refusé l'objet")
                else:
                    print("Je n'ai pas compris camarade ! ")
                    self.parler(joueur)  # Relance de la methode



