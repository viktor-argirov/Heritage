class Forme:
    def __init__(self):

       def aire(self):
            return 0

class Rectangle(Forme):
    
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    def aire(self):
        return self.largeur*self.hauteur
    
e=Forme()
r=Rectangle(8,4)
print(r.aire())
