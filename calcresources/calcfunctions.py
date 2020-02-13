def sumcalc(x,y):
    return x+y


def rescalc(x,y):
    return x-y

class Animal:
    """
    First parameter is colour, the second is name, and the third is specie
    """
    def __init__(self,colour,name,specie):
        self.colour = colour
        self.name = name
        self.specie = specie    
    
    def whichis(self):
        print(f'This animal is a {self.specie} which name is {self.name} and has {self.colour} hair')