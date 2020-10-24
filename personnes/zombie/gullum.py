from zombie import MobZombie

class Gollum(MobZombie):
    """ Cette classe représente un gollum.
    Les gollums sont des zombies plus agiles qui lachent du poison"""

    def __init__(self):
        """ Constructeur. Paramètres :
        - vitesse : on ne change que la vitesse du chien
        """
        self._vie = 10
        self._vitesse = 4
        self._agilite = 2

    def description(self):
        """ Renvoie la description du chien zombie."""
        return "Un gollum semble vouloir vous mordre"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
        print("Un gollum " + " " + discours[random.randint(0,3)])
        input()

    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        print("Le gollum ne semble pas comprendre ce que vous dites")

    #def poison()


    def esquive(self, joueur):
        """lorsque le joueur attaque, le zombie a une chance d'esquiver la balle
        pour le zombie normal, on considère qu'il a une chance sur deux d'esquiver la balle"""
        chance = random.randint(1,self._agilite)
        if chance == 1:
        #le zombie esquive la balle
            print("le zombie esquive la balle")
        else:
        #le zombie se prend la balle
            print("le zombie se prend la balle")

    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
        # self._vie = """