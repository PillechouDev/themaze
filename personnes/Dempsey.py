from personnage import Personnage
from joueur import Joueur
from objets.Cleinvoc import CleInvoc
import random




class Dempsey (Personnage):
    """ Cette classe représente un Perroquet qui salue le joueur lorsqu'il arrive sur la même case, et qui répète
    bêtement ce qu'on lui dit. Le perroquet a une couleur qu'on lui passe à la création dans le constructeur. """

    

    def description(self):
        return "Tank Dempsey"

    def rencontrer(self, joueur):
        discours = ['Ici tank Dempsey UUUUHHHAAA !!', "sniff sniff, wooow sa fouette !! Nikolai c'est toi ?", "wow t'est tellement moche que j'ai failli te confondre avec un mort vivant"]
        print("Dempsey : "+ discours[random.randint(0,2)])
        input()


    def parler(self, joueur):
        sac = joueur.getSac()
        #On fait une condition pour savoir si le sac est vide afin de ne pas boucler sur du vide
        if (len(sac)) == 0:
            print("Dempsey : tiens j'ai trouvé quelque chose qui pourrait etre utile camarade")
            entree = input("#> Voulez vous prendre l'objet de forme sphérique qu'il vous tend ? [o/n]")
            if entree in ['o', 'O', 'OUI', 'oui']:
                joueur.mettreObjetDansLeSac(CleInvoc())
                print("vous avez à present une clef spécial dans votre sac")
            else:
                print("vous avez refusé l'objet")
        else:
            #si le sac n'est pas vide, on fait une boucle pour savoir si la clé d'invocation est déjà présente
            for obj in sac:
                if obj.description() == "ClefInvocation":
                    print("Dégage !! je t'ai deja donné ce que j'avais")
                else:
                    print("Dempsey : tiens j'ai trouvé quelque chose qui pourrait etre utile camarade")
                    entree = input("#> Voulez vous prendre l'objet de forme sphérique qu'il vous tend ? [o/n]")
                    if entree in ['o', 'O', 'OUI', 'oui']:
                        joueur.mettreObjetDansLeSac(CleInvoc())
                        print("vous avez à present une clef spécial dans votre sac")
                    else:
                        print("vous avez refusé l'objet")
