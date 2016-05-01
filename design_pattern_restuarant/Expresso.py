from design_pattern_restuarant.Beverage import Beverage

class Expresso(Beverage):

    def __init__(self):
        self.description = "Expresso"
        self.price = 2.99

    def cost(self):
        return self.price