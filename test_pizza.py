import unittest
from unittest import TestCase
from Pasadena_Restuarant import Pasadena_Restuarant

class TestPizza(TestCase):
    def test_prepare_pizza(self):
        # Arrange
        pasadena_CPK = Pasadena_Restuarant("Pasadena CPK")

        # Act
        pizza = pasadena_CPK.order_pizza("NYStyle")
        pizza_price = 12.0

        # Assert
        self.assertEquals(pizza.name, "NY Style")
        self.assertEquals(pizza.price, pizza_price)

if __name__ == "__main__":
    unittest.main()
