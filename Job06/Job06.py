class Vehicule:
    def __init__(self,marque,annee,prix):
        self.marque=marque
        self.annee=annee
        self.prix=prix
    
    def informationVehicule(self):
        print("Marque = ", self.marque)
        print("Année = ", self.annee)
        print("Prix = ", self.prix)
    
class Voiture(Vehicule):
    def __init__(self, marque,model, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.model=model
        self.portes = portes
    
    def informationVehicule(self):
        super().informationVehicule()
        print("Model = ",self.model)
        print("Nombre de portes = " ,self.portes)
    
    def demarrer(self):
        print("La voiture démarre !")

vo=Voiture("Mercedes","Class S",2020,18500)
vo.informationVehicule()
vo.demarrer()
print()

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roues=2):
        super().__init__(marque, annee, prix)
        self.roues = roues
        
    def informationsVehicule(self):
        super().informationVehicule()
        print(f"Nombre de roues : {self.roues}")

    def demarrer(self):
        print("La moto démarre !")

mo=Moto("Harley Davidson",2019,10000)
mo.informationVehicule()
mo.demarrer()