from personnes.zombie.zombieClass import zombieClass
import random

from objets.Chair import Chair

"""
Classe faite par : Romain 
"""

class Dog(zombieClass):
    """ Cette classe représente un zombie chien.
    Les zombies chiens sont beaucoup plus rapide qu'un zombie classique"""

    def __init__(self):
        """ Constructeur.
        - _agilite : on ne change que l'agilite du chien
        - _nourri : si le chien mange de la viande, il arrête de nous attaquer

        """
        super().__init__()
        self._chanceEsquive = 5
        self._nourri = False

    def description(self):
        """ Renvoie la description du chien zombie."""
        if self._mort == True:
            return "cadavre de chien zombifié"
        elif self._nourri == True:
            return "le chien zombie vous regarde joyeux"
        else:
            return "Un chien zombie vous regarde alléché"

    def rencontrer(self, joueur):
        sac = joueur.getSac()
        chair = Chair()
        if len(sac) == 0:
            if not self._mort:
                discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
                print("Un chien zombie " + " " + discours[random.randint(0, 3)])
                print("Un combat se lance")
                self.combattre(joueur)
        else:
            for obj in sac:
                if obj == chair.description():
                    print("Le chien zombie semble être attiré par la chair putréfiée dans votre sac")
                    print("Vous décidez de lui donner")
                    print("Le chien se laisse caresser tandis qu'il mange la chair de zombie")
                    print("Le chien vous laisse partir !")

                else:
                    if not self._mort:
                        discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
                        print("Un chien zombie " + " " + discours[random.randint(0, 3)])
                        print("Un combat se lance")
                        self.combattre(joueur)

                    else:
                        print("Un chien zombie mort")












    def caresser(self, joueur):
        sac = joueur.getSac()
        if (len(sac)) == 0:
            if "Chair putréfiée" in sac:
                print("Le chien vous mord la main")

            else:
                for obj in sac:
                    if obj == "Un morceau de chair de zombie":
                        print("Le chien zombie semble être attiré par la chair putréfiée dans votre sac")
                        print("Vous décidez de lui donner")
                        print("Le chien se laisse caresser tandis qu'il mange la chair de zombie")
                        print("Le chien vous laisse partir !")


    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        if self._mort == True :
            print("Parler à un chien est déjà quelque chose d'incensé. Alors à un chien zombie mort")
        if self._nourri == True:
            print("Le chien ne vous comprend pas... Logique pour un animal")
        else:
            print("Le chien zombie ne semble pas vous écouter")

