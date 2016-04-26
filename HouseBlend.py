from Beverage import Beverage

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"

    def cost(self):
        return 1.99