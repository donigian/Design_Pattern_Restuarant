import unittest
from unittest import TestCase
from Waitress import Waitress
from Cook import Cook
from Order import Order

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