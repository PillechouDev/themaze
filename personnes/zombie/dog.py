from personnes.zombie.zombieClass import zombieClass

class Dog(zombieClass):
    """ Cette classe représente un zombie chien.
    Les zombies chiens sont beaucoup plus rapide qu'un zombie classique"""

    def __init__(self):
        """ Constructeur.
        - _vitesse : on ne change que la vitesse du chien
        """
        super().__init__()
        self._vitesse = 2

    def description(self):
        """ Renvoie la description du chien zombie."""
        return "Un chien zombie vous regarde alléché"

    def rencontrer(self, joueur):
        """ Affiche un message de salutation au joueur.
        """
        #Je pense qu'il manque des interraction (Elif des différenters situtation)
        discours = ['vous attaque', 'crie', 'vous cours dessus', 'hurle']
        print("Un chien zombie " + " " + discours[random.randint(0,3)])
        input()

    def parler(self, joueur):
        """ Un zombie ne peut pas parler donc lorsque le joueur voudra lancer un dialogue avec celui ci
        un message d'erreur lui sera retourné"""
        print("Le chien zombie ne semble pas vous écouter")


    def caresser(self, joueur):
        """caresser un chien zombie ne semble pas être une bonne idée... Sauf si on possède de la chair putréfiée"""
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




    # def subir(self, joueur):
    """
    TODO: Faire une méthode sur le joueur qui permet au joueur d'attaquer un zombie
    """
        # self._vie = """