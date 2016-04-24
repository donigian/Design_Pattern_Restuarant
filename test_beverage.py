from unittest import TestCase
from Beverage import Beverage

class BeverageTest(TestCase):

    def test_create_drink(self):
        coke = "CocaCola"
        drink_size = "Large"
        drink = Beverage(coke, drink_size)
        self.assertEquals(drink.name, coke)
        self.assertEquals(drink.size, drink_size)
