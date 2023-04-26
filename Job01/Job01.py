class Personne: 
    def __init__(self,age):
        self.age=age
    
    def afficher_Age(self):
        print(self.age)

    def bonjour(self):
        print("bonjour")

    def modifierAge(self,newage):
        self.age=newage

class Eleve(Personne):
    def afichageAge(self):
        print("J'ai",self.age,"ans")

    def Allerencours(self):
        print("Je vais en cours")
    

class Professeur(Personne):
    def __init__(self,matiereEnseignee,age=30):
        super().__init__(age)
        self.__matiereEnseignee=matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne=Personne(14)
eleve=Eleve(14)
print("Age de l'eleve par defaut : ")
eleve.afficher_Age()