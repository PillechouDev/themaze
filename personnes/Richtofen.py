from objets.Kronorium import Kronorium
from personnage import Personnage
import random


class Richtofen(Personnage):

    instance = None

    @staticmethod
    def getInstance():

        if Richtofen.instance is None:
            Richtofen.instance = Richtofen()
        return Richtofen.instance




    def description(self):
        return "Un officier Allemand "

    def rencontrer(self, joueur):
        discours = ["a completer", "je ferais ca apres", "vive les nazombies"]
        print("Richtofen : "+ discours[random.randint(0,2)])


    def parler(self, joueur):
        sac = joueur.getSac()
        if (len(sac)) == 0:
            print("Richtofen : Prenez le Kronorium... Vous êtes le seul à pouvoir combler la faille")
            entree = input("#> Voulez vous prendre ce livre ? [o/n]")
            if entree in ['o', 'O', 'OUI', 'oui']:
                joueur.mettreObjetDansLeSac(Kronorium.getInstance())
            elif entree in ['n','N','NON','non']:
                print("Vous avez refusé le Kronorium")
            else:
                print("Nein Nein Nein! Ce n'est ni de l'allemand, ni du français, ni de l'anglais... Pouvez-vous répéter?")
                self.parler(joueur)
        else:
            for obj in sac:
                if obj == Kronorium.getInstance():
                    print("Richtofen: Je t'ai déjà donné le Kronorium... Souhaites-tu peut être t'engager pour le IIIème Reich?")
                else:
                    print("Richtofen : Prenez le Kronorium... Vous êtes le seul à pouvoir combler la faille")
                    entree = input("#> Voulez vous prendre ce livre ? [o/n]")
                    if entree in ['o', 'O', 'OUI', 'oui']:
                        joueur.mettreObjetDansLeSac(Kronorium.getInstance())
                    elif entree in ['n', 'N', 'NON', 'non']:
                        print("Vous avez refusé le Kronorium")
                    else:
                        print("Nein Nein Nein! Ce n'est ni de l'allemand, ni du français, ni de l'anglais... Pouvez-vous répéter?")
                        self.parler(joueur)

