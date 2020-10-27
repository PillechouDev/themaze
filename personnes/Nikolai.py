from objets.Vodka import Vodka
from personnage import Personnage
from joueur import Joueur
import random


class Nikolai(Personnage):
    """ Cette classe représente Nikolai Belinski un des 4 personnages à rencontrer pour finir le jeu """


    def description(self):
        return "Nikolai Belinski"

    def rencontrer(self, joueur):
        discours = ["Nikolai est plus fort qu'une muraille , hé sa rime ! ", "Vodka pour tout le monde !", "On boit de la vodka ce soiiiiiir !"]
        print("Nikolai : "+ discours[random.randint(0,2)])


    def parler(self, joueur):
        sac = joueur.getSac()
        #On fait une condition pour savoir si le sac est vide afin de ne pas boucler sur du vide
        if (len(sac)) == 0:
            print("Nikolai : Faut que j'arrette de boire... Tiens ma vodka c'est ma dernière")
            entree = input("#> Voulez vous prendre sa vodka ? [o/n]")
            if entree in ['o', 'O', 'OUI', 'oui']:
                joueur.mettreObjetDansLeSac(Vodka.getInstance().ramasser(joueur))
                print("vous avez à present une bouteille de vodka dans votre sac")
            elif entree in ['n','N','NON','non']:
                print("vous avez refusé l'objet")
            else:
                print("Je n'ai pas compris camarade ! ")
                self.parler(joueur)
        else:
            #si le sac n'est pas vide, on fait une boucle pour savoir si la clé d'invocation est déjà présente
            for obj in sac:
                if obj == Vodka.getInstance():
                    print("Salut camarade , je viens de donner ce que j'avais ... \n Oh mince peut être que le Capitalisme te met dans le rouge ? \n Tien voici 500 $")
                    joueur.addArgent(500)
                else:
                    print("Nikolai : Faut que j'arrette de boire... Tiens ma vodka c'est ma dernière")
                    entree = input("#> Voulez vous prendre sa vodka ? [o/n]")
                    if entree in ['o', 'O', 'OUI', 'oui']:
                        joueur.mettreObjetDansLeSac(Vodka.getInstance().ramasser(joueur))
                        print("vous avez à present une bouteille de vodka dans votre sac")
                    elif entree in ['n', 'N', 'NON', 'non']:
                        print("vous avez refusé l'objet")
                    else:
                        print("Je n'ai pas compris camarade ! ")
                        self.parler(joueur)

