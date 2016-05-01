from unittest import TestCase

from HouseBlend import HouseBlend

from design_pattern_restuarant.Mocha import Mocha


class BeverageTest(TestCase):

    def test_create_drink(self):
        # Arrange
        beverage_description = 'House Blend Mocha'
        beverage_cost = 2.189

        # Act
        beverage = HouseBlend()
        beverage = Mocha(beverage)
        print(beverage.get_beverage_description(), " ", beverage.cost())

        # Assert
        self.assertEquals(beverage.get_beverage_description(), beverage_description)
        self.assertAlmostEqual(round(beverage.cost(), 2), round(beverage_cost, 2))
