"""
CLASSE MERE DES ZOMBIE

"""

import random
from themaze.personnes.zombie.zombieClass import zombieClass


class zombie(zombieClass):
    """ Cette classe représente un zombie classique. Le zombie attaque le joueur. Les intéractions sociales entre le joueur et le zombie
    sont limitées du fait que le zombie et par définition violent et dénué de parole"""

    #ATTENTION CETTE CLASSE C EST LA CLASSE MERE DONC ELLE CONTIENT JUSTE UN PERSONNAGE DE TYPE ZOMBIE ET PAS UN ZOMBIE
    #Note : ce n'est pas perdu juste à mouve
    def __init__(self):
        super().__init__()


    def description(self):
        """ Renvoie la description du zombie."""
        return "Un zombie vous regarde alléché"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
        print("Un zombie " + " " + discours[random.randint(0, 3)])
        input()

    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        print("Le zombie ne semble pas vous écouter")

    # Plutot avoir une methode de combat : combat() avec calcul de prob de toucher le mob , et l'attaque du zombie

    def attaquer(self, joueur):
        """le zombie attaque le joueur selon ses dégâts"""
        joueur.perdreEnergie(self._degat)

    def esquive(self, joueur):
        """lorsque le joueur attaque, le zombie a une chance d'esquiver la balle
        pour le zombie normal, on considère qu'il a une chance sur 10 d'esquiver la balle"""
        chance = random.randint(1, self._agilite)
        if chance == 1:
            # le zombie esquive la balle
            print("le zombie esquive la balle")
        else:
            # le zombie se prend la balle
            print("le zombie se prend la balle")

    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
    # self._vie = """
