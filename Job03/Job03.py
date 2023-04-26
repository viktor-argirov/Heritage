class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur=largeur

    def perimetre(self):
        print((self.__longueur + self.__largeur)*2)
    
    
    def surface(self):
        print(self.__longueur*self.__largeur) 
    
    
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def set_longueur(self,newlongueur):
        self.__longueur=newlongueur
    def set_largeur(self,newlargeur):
        self.__largeur=newlargeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self.hauteur=hauteur
        
    def volume(self,longueur,largeur,hauteur):
        self.__longueur=longueur
        self.__largeur=largeur
        self.hauteur=hauteur
        print((self.__longueur * self.__largeur * self.hauteur))

rect=Rectangle(5,5)
rect.perimetre()
rect.surface()
para=Parallelepipede(3,5,42)
para.volume(3,5,42)