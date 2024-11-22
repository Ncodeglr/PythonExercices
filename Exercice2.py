print("Bienvenue au cinéma, voici les films à l'affiche : ")
print("")

FILM1 = "Voyage au centre de la salle"
FILM2 = "Les 9jsons cachés"
FILM3 = "Algobox"

#---Partie1 : Avec une liste
liste_films = [FILM1,FILM2,FILM3]
for compteur, film in enumerate(liste_films, start=1):  # start=1 pour commencer à 1 au lieu de 0
    print("Film : " + film + " --> Salle n°" + str(compteur))
#---

#--Partie 2 : Avec une liste de dico stockant les data telles que : Nom du film,horaire et nombre de places 
list_de_dico = [
    {#Film1
        "titre" : FILM1,
        "seance" : "18h05",
        "places" : 200

    },
    {#Film2
        "titre" : FILM2,
        "seance" : "19h30",
        "places" : 0

    },
    {#Film3
        "titre" : FILM3,
        "seance" : "21h00",
        "places" : 120

    }
]

#Affichage de la liste de dico avec le format suivant : 
for numero,film in enumerate(list_de_dico,start=1):
    titre = film["titre"]
    seance = film["seance"]
    places = film["places"]
    print("Film n°{} : {} : seance : {} ({} places dispo)".format(numero,titre,seance,places))
    print("Film n°{} : {} : seance : {} ({} places dispo)".format(numero,titre,seance,places))


#Gestion des Places :
print("")
choix = False
while(choix!=True):
    choixUser = int(input("Choisir le numéro de films que vous souhaitez voir : "))
    for numero,film in enumerate(list_de_dico,start=1):
        titre = film["titre"]
        seance = film["seance"]
        places = film["places"]
        if(choixUser == numero and places !=0):
            places-=1
            print("Votre choix a été prise en compte")
            print("Nombre de places restantes : ",places)
            choix = True
        else:
            print("Le film est complet")
            print("")
            break
#---  
    
    
    
