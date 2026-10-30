# import random pour choisir un monstre au hasard


# liste des monstres
# chaque monstre a un nom, une attack, une defense et des hp


# liste des joueurs
# chaque monstre a un nom, une attack, une defense et des hp


# bienvenue()
#   afficher un message de bienvenue
#   demander au joueur si il veut lancer le jeu
#   recuperer sa reponse
#   mettre la reponse en minuscule
#   si la reponse est egale a "a"
#       afficher lancement du jeu
#   sinon
#       afficher que le choix est invalide
#       fermer le programme


# afficher_menu()
#   afficher les choix du menu
#   1. Demarrer le jeu
#   2. Classement
#   3. Quitter


# recuperer_choix_valide()
#   faire une boucle pour demander le choix
#   recuperer le choix du joueur
#   verifier si le choix est valide
#   si le choix est 1, 2 ou 3
#       convertir le choix en nombre
#       retourner le choix
#   sinon
#       afficher choix invalide
#       redemander le choix


# lancer_choix_choisi(choix)
#   recuperer le choix du joueur
#   si choix = 1
#       lancer demarrer_jeu()
#   sinon si choix = 2
#       lancer afficher_classement()
#   sinon si choix = 3
#       afficher au revoir


# demarrer_jeu()
#   demander le nom du joueur
#   recuperer le nom
#   afficher bonjour + nom du joueur
#   creer une equipe
#       appeler creer_equipe()
#       recuperer l'equipe crée
#   afficher que l'equipe est prete
#   parcourir les joueurs de l'equipe
#       afficher le nom de chaque joueur
#   lancer le combat
#       appeler combat(equipe)


# afficher_classement()
#   afficher le classement des joueurs
#   afficher les noms et les temps
#   demander au joueur d'appuyer sur M pour revenir au menu
#   attention pour le moment le M ne fait rien
#   il faudra recuperer la touche et faire le retour au menu


# afficher_joueurs_disponibles(joueurs)
#   afficher le titre personnages disponibles
#   parcourir la liste des joueurs
#   recuperer le numero et le nom de chaque joueur
#   afficher le numero + le nom du joueur


# demander_choix_joueur(max_index)
#   faire une boucle tant que le choix est pas valide
#   demander au joueur de choisir un personnage
#   essayer de convertir le choix en nombre entier
#   enlever 1 au choix pour avoir l'index de la liste
#   verifier si l'index existe
#   si le choix est valide
#       retourner l'index
#   sinon
#       afficher choix invalide
#       recommencer
#   si le joueur rentre autre chose qu'un nombre
#       afficher entrez un nombre valide
#       recommencer


# creer_equipe()
#   copier la liste des joueurs disponibles
#   creer une equipe vide
#
#   tant que l'equipe contient moins de 3 joueurs
#       afficher les joueurs disponibles
#           appeler afficher_joueurs_disponibles()
#       demander le choix du joueur
#           appeler demander_choix_joueur()
#           envoyer le nombre de joueurs disponibles
#       recuperer le personnage choisi
#       enlever le personnage de la liste des joueurs dispo
#       ajouter le personnage dans l'equipe
#       afficher le nom du personnage ajouté
#
#   retourner l'equipe quand les 3 joueurs sont selectionnés


# get_monstre_aleatoire()
#   aller chercher dans la liste des monstres
#   choisir un monstre au hazard avec random
#   faire une copie du monstre
#   retourner le monstre choisi


# calculer_degats(attacker, defender)
#   recuperer l'attaque de celui qui attaque
#   recuperer la defense de celui qui se fait attaquer
#   calculer les degats
#       attaque - defense
#   si les degats sont inferieur a 1
#       mettre les degats a 1 minimum
#   retourner les degats calculés


# attaquer(attacker, defender)
#   calculer les degats
#       appeler calculer_degats()
#       envoyer l'attaquant et le defenseur
#   enlever les degats aux hp du defenseur
#   afficher qui attaque qui et combien de degats sont fait


# get_joueur_vivant(equipe)
#   parcourir les joueurs de l'equipe
#   regarder les hp de chaque joueur
#   si les hp sont superieur a 0
#       retourner le joueur vivant
#       arreter la recherche
#   si aucun joueur est vivant
#       retourner None


# combat(equipe)
#   choisir un monstre au hasard
#       appeler get_monstre_aleatoire()
#   afficher le nom du monstre qui apparait
#
#   tant que les hp du monstre sont superieur a 0
#
#       chercher un joueur vivant dans l'equipe
#           appeler get_joueur_vivant(equipe)
#
#       si aucun joueur est vivant
#           afficher que tous les joueurs sont morts
#           arreter le combat
#
#       le joueur attaque le monstre
#           appeler attaquer(joueur, monstre)
#           calculer les degats
#           enlever les hp au monstre
#
#       verifier si le monstre est mort
#           si ses hp sont inferieur ou egal a 0
#               afficher que le monstre est vaincu
#               arreter le combat
#
#       si le monstre est toujours vivant
#           le monstre attaque le joueur
#               appeler attaquer(monstre, joueur)
#               calculer les degats
#               enlever les hp au joueur
#
#       verifier si le joueur est mort
#           si ses hp sont inferieur ou egal a 0
#               afficher que le joueur est mort
#
#       recommencer le tour
#       chercher un joueur vivant
#       continuer le combat tant que le monstre est vivant


# main()
#   afficher le message de bienvenue
#       appeler bienvenue()
#
#   afficher le menu
#       appeler afficher_menu()
#
#   recuperer le choix du joueur
#       appeler recuperer_choix_valide()
#       recuperer le choix retourné
#
#   lancer la fonction qui correspond au choix
#       appeler lancer_choix_choisi(choix)


# lancemnt du programme
#   appeler main()
#   commencer le deroulement du jeu
#
#   bienvenue
#       ↓
#   afficher le menu
#       ↓
#   recuperer le choix
#       ↓
#   lancer la fonction correspondante
#       ↓
#   demarrer le jeu / classement / quitter
# code : 
import random # afin de pouvoir faire des choix aléatoires pour les monstres et les joueurs dans le jeu de combat

# liste des monstres
liste_monstres = [
    {"name": "Gobelin", "attack": 10, "defense": 5, "hp": 50},
    {"name": "Orc", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Dragon", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Zombie", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Troll", "attack": 25, "defense": 15, "hp": 200},
]

# liste des joueurs
liste_joueurs = [
    {"name": "Amir", "attack": 10, "defense": 5, "hp": 50},
    {"name": "lyna", "attack": 20, "defense": 8, "hp": 120},
    {"name": "Amiré", "attack": 35, "defense": 20, "hp": 300},
    {"name": "Amyr", "attack": 12, "defense": 6, "hp": 70},
    {"name": "Amiro", "attack": 25, "defense": 15, "hp": 200},
]

#le 09/03 version squeltte fait sans ia rien du tt 
# fonction dec en plusieurs fonctions pour une meilleure orga/compréhension du code et une meilleure lisibilité

#-------------------------------------------------gestion menu-------------------------------------

def bienvenue(): # Afficher un message de bienvenue et demander à l'utilisateur de lancer le jeu avc A sinon le jeu se ferme
    print("Bienvenue dans le jeu de combat entre joueurs et monnstres ! cliquez sur A pour Lancer ")
    if input().lower() == 'a':
        print("Lancement du jeu...")
    else :
        print("Choix invalid, le jeu va se fermeer cheh .")
        exit()


def afficher_menu(): # Afficher le menu principl 
    print("1. Démarrer le jeu")
    print("2. Classement")
    print("3. Quitter")


def demarrer_jeu():
    username = input("Entrez votre nom : ")
    print(f"Bonjour {username} !")
    equipe = creer_equipe()
    print("\nVotre équipe est prête !")

    for joueur in equipe:
        print(joueur["name"])
    combat(equipe)



def afficher_classement(): # Afficher le classement des joueurs
    print("Voici le classement des jpuers : Amir : 32 secondes, ines : 45 secondes, Anas : 50 secondes")
    print("clique sur M pour revenir sur le Menu des choix")
    


#-------------------------------------------------gestion menu-------------------------------------

def recuperer_choix_valide(): # Récupérer le choix de l'utilisateur et vérifier sa validité
    while True:
        choix = input("Ton choix : ")
        if choix in ["1", "2", "3"]:
            return int(choix)
        else:
            print("Choix invalide, veuillez réessayer.")

def lancer_choix_choisi(choix): # Lancer la fonction correspdt au choix de luser
    if choix == 1:
        demarrer_jeu()
    elif choix == 2:
        afficher_classement()
    elif choix == 3:
        print("Au revoir") 
        
#-------------------------------------------------gestion equipe-------------------------------------

def afficher_joueurs_disponibles(joueurs):# permret daficher les joueurs dispoo dans la luste
    print("\nPersonnages disponibles :")
    for i, joueur in enumerate(joueurs):
        print(i + 1, "-", joueur["name"], ) 


def demander_choix_joueur(max_index):
    while True:
        try:
            choix = int(input("Choisissez un personnage : ")) - 1
            if 0 <= choix < max_index:
                return choix
            else:
                print("Choix invalide")
        except:
            print("Entrez un nombre valide")
        

def creer_equipe():
    joueurs_disponibles = liste_joueurs.copy()
    equipe = []

    while len(equipe) < 3:
        afficher_joueurs_disponibles(joueurs_disponibles)
        choix = demander_choix_joueur(len(joueurs_disponibles))
        joueur_choisi = joueurs_disponibles.pop(choix)
        equipe.append(joueur_choisi)
        print(joueur_choisi["name"], "ajouté à l'équipe")

    return equipe
#-------------------------------------------------gestion combat----------------------------------------------
def get_monstre_aleatoire():
    monstre = random.choice(liste_monstres)
    return monstre.copy()

def calculer_degats(attacker, defender):
    degats = attacker["attack"] - defender["defense"]
    if degats < 1:
        degats = 1
    return degats

def attaquer(attacker, defender):
    degats = calculer_degats(attacker, defender)
    defender["hp"] -= degats
    print(attacker["name"], "attaque", defender["name"], "et inflige", degats, "degats")

def get_joueur_vivant(equipe):

    for joueur in equipe:
        if joueur["hp"] > 0:
            return joueur
    return None

def combat(equipe):
    monstre = get_monstre_aleatoire()
    print("\nUn", monstre["name"], "apparait !")
    while monstre["hp"] > 0:

        joueur = get_joueur_vivant(equipe)
        if joueur is None:
            print("Tous les joueyurs sont morts !")
            return

        attaquer(joueur, monstre)
        if monstre["hp"] <= 0:
            print(monstre["name"], "est vaincu !")
            return

        attaquer(monstre, joueur)
        if joueur["hp"] <= 0:
            print(joueur["name"], "est mort !")


#-------------------------------------------------gestion main deroulment-------------------------------------
def main(): 
   # Afficher un message de bienvenue
    bienvenue() 

    # Afficher le menu de choix
    afficher_menu()

    # Récupérer le choix de l'utilisateur valide
    choix = recuperer_choix_valide()

    # Gérer les choix de l'utilisateur
    lancer_choix_choisi(choix)

main()
    






























#def bienvenue():
    #print('Bienvenue sur  le jeu des monstros')