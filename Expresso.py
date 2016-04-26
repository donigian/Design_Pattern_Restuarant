from Beverage import Beverage

class Expresso(Beverage):
    def __init__(self):
        self.description = "Expresso"

    def cost(self):
        return 2.99