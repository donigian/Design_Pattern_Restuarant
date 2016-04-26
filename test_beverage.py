from unittest import TestCase
from Beverage import Beverage
from Expresso import Expresso
from HouseBlend import HouseBlend
from Mocha import Mocha

class BeverageTest(TestCase):

    def test_create_drink(self):
        beverage_description = 'House Blend Mocha'
        beverage_cost = 2.189

        second_beverage = HouseBlend()
        second_beverage = Mocha(second_beverage)
        print(second_beverage.get_beverage_description(), " ", second_beverage.cost())

        self.assertEquals(second_beverage.get_beverage_description(), beverage_description)
        self.assertAlmostEqual(round(second_beverage.cost(),2), round(beverage_cost,2))
