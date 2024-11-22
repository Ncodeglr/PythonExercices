"""
-Machine à sous avec des probabilités d'apparitions 
"""
import random as rd
import numpy as np

print("---------------------------------------------------------------------------------------------------")
print("                             Benvenue dans la machine à sous")
print("")

liste_fruit = ["Ananas","Cerise","Orange","Pasteque","Pomme_dore"]
liste_proba = [0.2, 0.25, 0.4, 0.1, 0.05]

#fruit_hasard = rd.choices(liste_fruit,k=3) #Permet de selectionner 3 fruits au hasard 
#print(fruit_hasard[0],fruit_hasard[1],fruit_hasard[2])




#Définition de la class Token 
class Token:
    def __init__(self,valeur: str) -> None:
        self.valeur = valeur
    
    def addToken(self,fruit: str):
        if(fruit == "Orange"):
             self.valeur +=5
             return self.valeur
        elif(fruit == "Cerise"):
             self.valeur +=15
             return self.valeur
        elif(fruit == "Ananas"):
             self.valeur +=50
             return self.valeur
        elif(fruit == "Pasteque"):
             self.valeur +=150
             return self.valeur
        elif(fruit == "Pomme_dore"):
             self.valeur +=10000
             return self.valeur


#Instanciation d'un objet de type Token
token1 = Token(100) #le joueur part avec 100 jeton 

compteur = 0
NOMBRE_SIMU = 200
while(compteur != NOMBRE_SIMU):
    tirage = np.random.choice(liste_fruit, 3, liste_proba)
    if(tirage[0] == tirage[1] == tirage[2]):
        token1.addToken(tirage[0])
        print("GAGNÉ",tirage)
        print("nombre de token =",token1.valeur)
    else:
        print("PERDU",tirage)
    compteur +=1












