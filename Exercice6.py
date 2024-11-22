"""
    Le Jeu du juste prix
"""

import random as rd
import time 

print("Bienvenue au jeu du JUSTE PRIX")
print("Tu dois deviner le prix auquel que je pense, il se situe entre 1 et 100")
print("")

nbRandom = rd.randint(1,100) #Nombre aléatoire généré compris entre 1 et 100
NB_PARTIE = 5 #Nombre de partie
flag = 0
TIME_GAME = 60 
start_time = time.time()  # Démarrer le chronomètre

while flag < NB_PARTIE:
    elapsed_time = time.time() - start_time # Vérifier le temps écoulé
    if elapsed_time > TIME_GAME:  # Temps limite (60 secondes)
        print("Temps écoulé : 60 secondes. Sortie de la boucle.")
        break
    
    # Demander une proposition
    nbUser = 0
    while not (1 <= nbUser <= 100):  # Vérifier que l'entrée est dans [1, 100]
        try:
            nbUser = int(input("Quelle est ta proposition : "))
        except ValueError:
            print("Veuillez entrer un nombre valide s'il vous plaît.")
    
    # Vérifier la proposition
    if nbUser == nbRandom:
        print("C'est gagné !")
        break
    elif nbUser > nbRandom:
        print("Trop grand.")
    else:
        print("Trop petit.")
    
    flag += 1  # Incrémenter le compteur de parties

# Si la boucle se termine sans victoire
if flag >= NB_PARTIE:
    print(f"Dommage ! Le nombre était {nbRandom}.")