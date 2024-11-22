"""                                 Gestion d'un parking
D = Une place disponible 
V = Une place contenant véhicule 
H = Une place pour les personnes à mobilités réduites
"""
import random as rd
import string

print("Bienvenue au Parking, que souhaitez-vous faire ? ")
print("----------------------------------------------")

sizeParking = 3
data = ['D','V']
list_parking1,list_parking2,list_parking3 = [],[],[]
k=0
#--Génération d'état sur les places des parking
while(k<sizeParking):
    list_parking1.append(rd.choice(data))
    list_parking2.append(rd.choice(data))
    list_parking3.append(rd.choice(data))
    k+=1

PARKING = [list_parking1,list_parking2,list_parking3]
for k,liste in enumerate(PARKING,start=1):
    print("Parking n°" + str(k) + " --> " + str(liste))

print("----------------------------------------------")
print("")
print("")
#---

def askchoixParking(PARKING):
    choix = 0
    while choix not in [1, 2, 3]:
        try:
            choix = int(input("Tapez votre choix concernant le numéro du parking, soit 1, 2 ou 3 : "))
        except ValueError:
            print("Veuillez entrer un nombre valide s'il vous plaît.")
    if(choix == 1):
         return PARKING[0]
    elif (choix == 2):
         return PARKING[1]
    else: 
        return PARKING[2]
    


def askAction():
    choix = 0
    while choix not in [1, 2]:
        try:
            choix = int(input("Taper 1 pour garer la voiture // Taper 2 pour récupérer la voiture : "))
        except ValueError:
            print("Veuillez entrer un nombre valide s'il vous plaît.")
    return choix



def gestionParking(parking: list, askUser: int,dico_code):
    if(askUser == 1):
        placeDispo = []
        for i in range(len(parking)):
            if(parking[i]=='D'):
                placeDispo.append(i)
        print("")
        print("Voici les numéros des places actuellement disponible sur la parking")
        print(placeDispo)
        if(placeDispo == []):
            print("Place indisponible")
            return 0
        while(1):
            choiceUser = int(input("Taper le n° sur lequel vous voulez garer votre véhicule"))
            if(parking[choiceUser] != 'V'):
                print(codes_déblocage["cle"])
                parking[choiceUser] = 'V'
                
                break
            else:
                print("Attention place déja prise")
                print(placeDispo)
    elif (askUser == 2):
        placeIndispo = []
        for i in range(len(parking)):
            if(parking[i] == 'V'):
                placeIndispo.append(i)
        print("")
        print("Voici les numéros des places où sont garer les voitures")
        print(placeIndispo)
        while(1):
            choiceUser = int(input("Taper le n° sur lequel vous voulez récupérer votre véhicule"))
            if(parking[choiceUser] == 'V'):
                askKey = ''
                while askKey != dico_code["cle"]:
                    try:
                        askKey = input("Donnez moi la clé de déblocage : ")
                    except ValueError:
                        print("Code de déblocage incorrect")
                print("Validation du déblocage") 
                parking[choiceUser] ="D"
                break
            else:
                print("Attention place vide")
                print(placeIndispo)
    print(parking)
    print("À bientôt")


def getKey(length):
    """Générer une chaîne aléatoire de longueur fixe"""
    str1 = string.ascii_uppercase
    str2=''
    for i in range(length):
        str2 += str(rd.randint(0,9))
    str3 = string.ascii_uppercase
    str_final = ''.join(rd.choice(str1) for i in range(length)) +'-'+ str2+'-'+''.join(rd.choice(str3) for i in range(length))
    return str_final
    



#--Dictionnaire stokant la valeur du code de déblocage 
codes_déblocage = {"cle":getKey(4)}

#Resultats
gestionParking(askchoixParking(PARKING),askAction(),codes_déblocage)

