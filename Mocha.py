from CondimentDecorator import CondimentDecorator
from Beverage import Beverage

class Mocha(CondimentDecorator):
    def __init__(self, Beverage):
        self.beverage = Beverage
        self.price = .20

    def get_beverage_description(self):
        return self.beverage.get_beverage_description() + " Mocha"

    def cost(self):
        return self.price + float(self.beverage.cost())