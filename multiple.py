#Parent class 1

class Item():
    def __init__(self, sku):
        self.sku=sku

    def print_sku(self):
        print("The sku is {}".format(self.sku))

#parent class 2

class Garment():
    def __init__(self, section, type):
        self.section=section
        self.type=type

    def print_sku(self):
        print("The is in section {}".format(self.section, self.type))

#child class

class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name=name
        self.color=color
        Item.__init__(self,sku)
        Garment.__init__(self,section,type)

        def print_shirt(self):
            print("{} {} on sale".format(self.color, self.name))

Blouse = Shirts("001", 45, "Tops", "Formal Blouse", "White")

Blouse.print_sku()




