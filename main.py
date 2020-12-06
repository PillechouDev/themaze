import os
import random

from config import Config
from joueur import Joueur
from labyrinthe.labyrinthe import Labyrinthe
from objets.boite import Boite
from objets.machine.Electricite import Electricite
from objets.potion import Potion

from objets.machine.doubleTap import DoubleTap
from objets.machine.juggerNog import JuggerNog
from objets.machine.muleKick import MuleKick
from objets.machine.quickRevive import QuickRevive



from personnes.Cadavre import Cadavre
from personnes.Dempsey import Dempsey
from personnes.Maxis import Maxis
from personnes.Nikolai import Nikolai
from personnes.Richtofen import Richtofen
from personnes.Takeo import Takeo
from personnes.zombie.brutus import Brutus
from personnes.zombie.dog import Dog
from personnes.zombie.gullum import Gullum
from personnes.zombie.zombie import Zombie


def avancerNord():
    try:
        joueur.avancerNord()
        brutus.avancerAleatoirement()

    except:
        print("Ouch, ce mur fait mal...")
        input()

def avancerSud():
    try:
        joueur.avancerSud()
        brutus.avancerAleatoirement()
    except:
        print("Ouch, ce mur fait mal...")
        input()

def avancerEst():
    try:
        joueur.avancerEst()
        brutus.avancerAleatoirement()


    except:
        print("Ouch, ce mur fait mal...")
        input()

def avancerOuest():
    try:
        joueur.avancerOuest()
        brutus.avancerAleatoirement()

    except:
        print("Ouch, ce mur fait mal...")
        input()


def regarder():
    case = joueur.getCaseCourante()
    personnages = case.getPersonnages()
    objets = case.getObjets()
    if (len(personnages) == 0 and len(objets) == 0):
        print(random.choice([
            "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
            "Des toiles d'araignées un peu partout.",
            "C'ets déseperement vide..."
        ]))
    else:
        print("Je vois :")
        for objet in objets:
            print(" - " + objet.description())
        for personnage in personnages:
            print(" - " + personnage.description())
    input()

def ramasser():
    case = joueur.getCaseCourante()
    if len(case.getObjets()) == 0:
        print("Mais... il n'y a rien à ramasser !")
    else:
        print("J'ai ramassé :")
        for objet in case.getObjets():
            objet.ramasser(joueur)
            print(" - " + objet.description())
        case.getObjets().clear()  # On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...
    input()

def sac():
    sac = joueur.getSac()
    if (len(sac)) == 0:
        print("Le sac est vide")
        input()
    else:
        print("Le sac contient: ")
        index = 0
        for obj in sac:
            print(str(index + 1) + " - " + obj.description())
            index += 1
        choice = input("Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
        try:
            num = int(choice)
            obj = sac[num - 1]
            sac.remove(obj)
            obj.utiliser(joueur)
        except:
            pass  # En cas d'erreur, c'est que l'entrée est invalide, on ne fait rien

def parler():
    personnages = joueur.getCaseCourante().getPersonnages()
    if len(personnages) == 0:
        print("Allo ? allo allo allo allo allo répète l'écho")
    else:
        for personnage in personnages:
            personnage.parler(joueur)
    input()

def combattre():
    personnages = joueur.getCaseCourante().getPersonnages()
    if len(personnages) == 0:
        print("Vous essayez de combattre votre ombre... L'ombre a gagné")
    else:
        for personnage in personnages:
            personnage.combattre(joueur)
    input()

def execute(param):
    return param()



def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# options de choix du joueur
choixJoueur = {
    "n" : avancerNord,
    "s" : avancerSud,
    "e" : avancerEst,
    "o" : avancerOuest,
    "regarder" : regarder,
    "ramasser" : ramasser,
    "sac" : sac,
    "parler" : parler,
    "combattre" : combattre
}
# now, to clear the screen

cls()

print("""

   .____
   |    |    ____
   |    |  _/ __ \
   |    |__\  ___/
   |_______ \___  >
           \/   \/
.____          ___.                 .__        __  .__
|    |   _____ \_ |__ ___.__._______|__| _____/  |_|  |__   ____
|    |   \__  \ | __ <   |  |\_  __ \  |/    \   __\  |  \_/ __ \
|    |___ / __ \| \_\ \___  | |  | \/  |   |  \  | |   Y  \  ___/
|_______ (____  /___  / ____| |__|  |__|___|  /__| |___|  /\___  >
        \/    \/    \/\/                    \/          \/     \/


""")
joueur = Joueur("X",100)

play=False
while play==False:
    try:
        entree = int(input("   Menu Principal \n    ___________\n 1. Jouer \n 2.Paramètres \n 3.Quitter \n \n"))

        if (entree == 1):
            play = True
        elif (entree == 2):
            Config.getInstance().showMenu(joueur)
        elif (entree == 3):
            play = False
            exit()
        cls()
    except ValueError:
        print("Mauvaise Valeur")
cls()

# Création des objets
# TODOCHECK: récupérer les attributs via un menu de configuration
l = Labyrinthe(Config.getInstance().getWidth(),Config.getInstance().getHeight())





#On dépose les personnages prncipaux
l.deposerJoueurAleatoirement(joueur)
l.deposerPersonneAleatoirement(Nikolai.getInstance())
l.deposerPersonneAleatoirement(Takeo.getInstance())
l.deposerPersonneAleatoirement(Dempsey.getInstance())
l.deposerPersonneAleatoirement(Richtofen.getInstance())
l.deposerPersonneAleatoirement(Maxis.getInstance())


# Generation de 70 potions aléatoirement
for i in range(70):
    potion = Potion(random.randint(5,10))
    l.deposerObjetAleatoirement(potion)


# Ajouter des zombies un peu partout
brutus = Brutus()
l.deposerBrutusAleatoirement(brutus)

for i in range(10):
    zombie = Zombie()
    cadavre = Cadavre()
    l.deposerPersonneAleatoirement(cadavre)
    l.deposerPersonneAleatoirement(zombie)
for i in range(7):
    dog = Dog()
    l.deposerPersonneAleatoirement(dog)
for i in range(5):
    gollum = Gullum()
    l.deposerPersonneAleatoirement(gollum)


#On dépose toutes les machines
#TODO : Prob atout ?
"""
doubletap = DoubleTap()
electricité = Electricite()
juggernog = juggerNog()
"""
for i in range(2):
    boite = Boite()
    l.deposerObjetAleatoirement(boite)

#Déposer les atouts
doubleTap = DoubleTap()
l.deposerObjetAleatoirement(doubleTap)

juggerNog = JuggerNog()
l.deposerObjetAleatoirement(juggerNog)

muleKick = MuleKick()
l.deposerObjetAleatoirement(muleKick)

quickRevive = QuickRevive()
l.deposerObjetAleatoirement(quickRevive)




while Maxis.getInstance().getEndgame()==False:
    #cls()  # Effacer la console
    joueur.printEnergie()
    print()
    l.afficher()
    print()

    action = input("Que dois-je faire ? ")
    if action in choixJoueur:
        execute(choixJoueur[action])

    else:
        print("Moi pas comprendre...")
        print("Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")
        input()

    joueur.perdreEnergie()
