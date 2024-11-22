"""
    Machine à Laver
"""
import math,time

def demarrer_machine():
    print("La machine a démarré")
    # Démarrer le chronomètre
    start_time = time.time()
    
    machineTime = 35
    while(machineTime > 0):
        print(str(machineTime) +'s')
        machineTime -=1
        time.sleep(1)

    # Arrêter le chronomètre
    end_time = time.time()

    # Calculer la durée
    elapsed_time = end_time - start_time
    print(f"Temps écoulé : {elapsed_time:.2f} secondes")
    print("Ouverture de la machine à laver")
    return elapsed_time

#--Définition de la class Lave_Linge
class Lave_Linge:
    def __init__(self) -> None:
        print("Ouverture de la machine à laver")
        print("")
        
    
    def info(self):
        quantiteLinge = input("Quantité de linge en Kg ? : ")
        try:
            Linge =float(quantiteLinge) 
            print(math.ceil(Linge*2/16),"nombre de machine")
            print(math.ceil(Linge*2/16)*60,"Litre pour ",math.ceil(Linge*2/16),"machine")
        except ValueError:
            print("Vous devez rentrer un nombre")

    
    def démarrage(self):
        print("Lancement de la machine")
        demarrer_machine()
    
    def stop(self):
        print("Stope de la machine")
    
    def fermer(self):
        print("Fermeture de la machine")

#---Instanciation de la class Lave_Linge
laveLinge1 = Lave_Linge()
laveLinge1.info()
laveLinge1.démarrage()



