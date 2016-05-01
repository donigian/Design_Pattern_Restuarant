import unittest
from unittest import TestCase

from Cook import Cook
from Waitress import Waitress

from design_pattern_restuarant.Order import Order


class TestOrder(TestCase):
    def test_order_pizza(self):

        # Arrange
        cook = Cook()
        order = Order(cook)
        waitress = Waitress()


        # Act
        waitress.take_order(order)
        waitress.place_order()

if __name__ == "__main__":
    unittest.main()