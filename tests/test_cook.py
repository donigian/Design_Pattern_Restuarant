from unittest import TestCase

from design_pattern_restuarant.Cook import Cook
from design_pattern_restuarant.Order import Order

class TestCook(TestCase):
    def test_place_order(self):
        order_to_be_placed = Order("Bob")
        cook = Cook(order_to_be_placed)

        self.assertEquals(cook.order.cook, "Bob")
