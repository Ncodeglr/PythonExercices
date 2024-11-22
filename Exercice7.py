""""
-Gestionnaire de taches en POO
"""
class Task:
    def __init__(self):
       self.dicoTask = {}
    
    def newTask(self):
        newTask = input("Give me your new task : ")
        self.dicoTask["task"+str(len(self.dicoTask)+1)] = newTask
        print("Ajout de la tache")
        print(self.dicoTask)

    def pushTask(self):
        namePushTask = ""
        while namePushTask not in self.dicoTask.keys():
            try:
                namePushTask = input("Provide the task you wish to delete : ")
            except ValueError:
                print("It's not a name valid")
        del self.dicoTask[namePushTask]
        print(self.dicoTask)
        
        # Réorganiser les clés
        print("Reorganizing tasks...")
        new_dico = {} #Il faut un nouveau dico pour changer le nom de l'ensemble des clés 
        for i, key in enumerate(self.dicoTask.keys(), start=1):
            new_dico[f"task{i}"] = self.dicoTask[key]
        self.dicoTask = new_dico
       

    def getTask(self):
        return self.dicoTask


task = Task()
task.newTask()
task.newTask()
task.pushTask()

print(task.getTask())

