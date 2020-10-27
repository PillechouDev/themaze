from exceptions import AbstractMethodCallException


class Boite:

    def __init(self):
        self.prix = 950

    def description(self):
        raise AbstractMethodCallException()

    def utliser(self, joueur):
        """ Cette métode est appellée lorsque le joueur veut utiliser la boite"""
        raise AbstractMethodCallException()

        if(joueur.argent >= self.prix):

            contenus = ['M14 (arme de poing)', 'L96A1 (sniper)', 'Galil', 'ThunderGun', 'rien du tout']
            print("vous avez eu :"+ discours[random.randint(0,3)])
            if contenus == 'M14 (arme de poing)':
                joueur.mettreObjetDansLeSac(M14.getInstance())

            elif contenus == 'L96A1 (sniper)':
                joueur.mettreObjetDansLeSac(L96A1.getInstance())

            elif contenus == 'Galil':
                joueur.mettreObjetDansLeSac(Galil.getInstance())

            elif contenus == 'ThunderGun':
                joueur.mettreObjetDansLeSac(ThunderGun.getInstance())

            elif contenus == 'rien du tout':
                print("vous vous etes bien fais avoir par cette foutue boite ...")
        else:
            print("vous n'avez pas assez d'argent")
            input()
