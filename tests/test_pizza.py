import unittest
from unittest import TestCase
from design_pattern_restuarant.Pasadena_Restuarant import Pasadena_Restuarant

class TestPizza(TestCase):
    def test_prepare_pizza(self):
        # Arrange
        pizza_price = 12.0
        pasadena_CPK = Pasadena_Restuarant("Pasadena CPK")

        # Act
        pizza = pasadena_CPK.order_pizza("NYStyle")

        # Assert
        self.assertEquals(pizza.name, "NY Style")
        self.assertEquals(pizza.price, pizza_price)

if __name__ == "__main__":
    unittest.main()
