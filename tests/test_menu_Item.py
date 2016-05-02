from unittest import TestCase
import unittest

from design_pattern_restuarant.Menu_Item import Menu_Item

class TestMenu_Item(TestCase):

    def test_name_exists(self):
        pizza_name = "New Yorker"
        menu_item = Menu_Item(pizza_name)

        self.assertEquals(menu_item.name,pizza_name)

if __name__ == "__main__":
    unittest.main()