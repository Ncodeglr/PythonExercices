"""
Le joueur a 5 jarres devant lui. Il doit choisir (en console) une des 5 jarres.
4 jarres contiennent une clé magique et 1 jarre contient un serpent.
Le but est de ne pas tomber sur la jarre contenant le serpent.
Il existe 3 niveaux de difficulté : 1, 2 et 3, qui impactent le nombre de serpents.
Le joueur part avec 1 clé. À 3 clés, il gagne et devient le roi du temple.
"""
import random as rd

print("-----------------------------Bienvenue dans le jeu-----------------------")
print("Vous disposez de 5 jarres devant vous, vous devez choissir entre la 1, 2, 3,4, 5")


#--Saisie du choix de level entre 1 2 et 3
level = 0 #Niveau de difficulté
while level<1 or level>3:
        level= int(input("Niveau de difficulté (1, 2 ou 3)"))
print("")
#--

nbKey = 1 #Nombre de clé de départ que le jouer possède
while(nbKey <3):
    
    #--Saisie du choix entre 1 et 5
    choix = 0
    while choix<1 or choix>5:
        choix= int(input("Donne moi un chiffre entre 1 et 5 : "))
    print("")
    #--

    #--Création d'une liste contenant 4 clé magique et un serpent
    if(level == 1):
        list_jarre = ["Clé"] * 4 + ["Serpent"]*1
    elif (level ==2):
        list_jarre = ["Clé"] * 3 + ["Serpent"]*2
    else:
        list_jarre = ["Clé"] * 1 + ["Serpent"]*4
    
    
    rd.shuffle(list_jarre)
    print(list_jarre)
    print(list_jarre[choix-1])
    #--
    
    
    #--Affichage Résultat
    if(list_jarre[choix-1] == "Clé"):
        print("C'est gagné !!!")
        for i,s in enumerate(list_jarre):
            if (s == "Serpent"):
                print("La jarre infecté était la n°" +str(i+1))
        nbKey+=1
    else:
        print("Dommage, c'est perdu")
        nbKey-=1
        if(nbKey<0):
            break
    
    print("")
    print("Mon trousseau = " + str(nbKey))
    print("")

if(nbKey == 3):
    print("Tu deviens le roi du temple")




