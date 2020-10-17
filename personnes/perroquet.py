from personnage import Personnage
import random

class Perroquet(Personnage):
    """ Cette classe représente un Perroquet qui salue le joueur lorsqu'il arrive sur la même case, et qui répète
    bêtement ce qu'on lui dit. Le perroquet a une couleur qu'on lui passe à la création dans le constructeur. """

    def __init__(self, couleur):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """
        self._couleur = couleur

    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un perroquet " + self._couleur

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        TODO: on pourrait avoir un message de salutation plus varié en le tirant aléatoirement ici, ou dans le constructeur pour qu'un même perroquet salue toujours de la même façon.
        """
        print("Un perroquet "+self._couleur+" vous salue bien bas")
        input()

    def parler(self, joueur):
        """ Le perroquet répète ce qu'on lui dit avec son accent de perroquet (en accentuant les voyelles). """
        print("Peroquet "+self._couleur+": Saaaluuuut, noble aventuuurier. Quue me veuuuuux-tuuuuu ?")
        entree = input("#>")
        repetition = ""
        for lettre in entree:
            if lettre in ['a','e','i','o','u']:
                repetition += lettre*random.randint(1,5) # Si c'est une voyelle, on la répète plusieurs fois
            else:
                repetition += lettre # Si ce n'est pas une voyelle, on ne la répète qu'une fois
        print(repetition)