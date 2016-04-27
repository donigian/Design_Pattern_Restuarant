from Beverage import Beverage

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"
        self.price = 1.99

    def cost(self):
        return self.price