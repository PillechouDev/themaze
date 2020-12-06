from objets.Katana import Katana
from personnage import Personnage
import random


"""
Classe faite par Mathieu Legrand
Faite par Legrand Mathieu
"""


class Takeo(Personnage):
    """ Cette classe représente Takeo Masaki un des 4 personnages à rencontrer pour finir le jeu , fait en singleton car il y'a qu'une seule instance sur le jeu """

    instance = None

    @staticmethod
    def getInstance():
        """
        :return: Instance de Takeo
        """
        if Takeo.instance is None:
            Takeo.instance = Takeo()
        return Takeo.instance

    def __init__(self):
        self.__argent = False  # Permet de savoir si l'argent est déja donnée dans l'easter egg

    def description(self):
        """Retourne la description"""
        return "Takeo Masaki"

    def rencontrer(self, joueur):
        """Lors de la rencontre un discours aléatoire est prononcée"""
        discours = ["Comme un récent proverbe le dit, pas de munitions, pas de vie.",
                    "Mon nom est Takeo, un guerrier n'a pas besoin de munitions", "Ton maître ne t'a donc pas enseigné les bonnes manières ?"]
        print("Takeo : " + discours[random.randint(0, len(discours))])

    def parler(self, joueur):
        """Permet de lancer un dialogue entre le joueur et Takeo et de récupérer l'object"""
        sac = joueur.getSac()
        # On fait une condition pour savoir si le sac est vide afin de ne pas boucler sur du vide
        if (len(sac)) == 0:
            print(
                "Takeo : Tu as fait breuve de beaucoup de courage, Voici mon Katana. Utilise le pour découper un maximum de zombies")
            entree = input("#> Voulez vous prendre le Katana ? [o/n]")
            if entree in ['o', 'O', 'OUI', 'oui']:
                # Mise en place de l'instance dans le sac
                joueur.mettreObjetDansLeSac(Katana.getInstance())
                print("vous avez à present un Katana dans votre sac")
            elif entree in ['n', 'N', 'NON', 'non']:
                print("vous avez refusé l'objet")
            else:
                print("Je n'ai pas compris camarade ! ")
                self.parler(joueur)  # Relance de la methode
        else:
            # si le sac n'est pas vide, on fait une boucle pour savoir si le Katana est déjà présent
            obtenu = False
            for obj in sac:
                if obj == Katana.getInstance():
                    obtenu = True


            if obtenu == True and self.__argent is False:
                print("Même un Samourai peut être dans le besoin, mets ta fierté de côté et prends ces 500 $")
                joueur.addArgent(500)
                self.__argent = True

            elif obtenu == True and self.__argent is True:
                print("Je t'ai donné tout ce que j'avais, apprends à te débrouiller seul !")

            else:
                print("Takeo : Tu as fait breuve de beaucoup de courage, Voici mon Katana. Utilise le pour découper un maximum de zombies")
                entree = input("#> Voulez vous prendre le Katana ? [o/n]")
                if entree in ['o', 'O', 'OUI', 'oui']:
                    # Mise en place de l'instance dans le sac
                    joueur.mettreObjetDansLeSac(Katana.getInstance())
                    print("vous avez à present un Katana dans votre sac")
                elif entree in ['n', 'N', 'NON', 'non']:
                    print("vous avez refusé l'objet")
                else:
                    print("Je n'ai pas compris camarade ! ")
                    self.parler(joueur)  # Relance de la methode

