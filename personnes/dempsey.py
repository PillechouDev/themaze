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


