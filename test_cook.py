from unittest import TestCase
from Cook import Cook

class TestCook(TestCase):
    def test_activity(self):
        current_activity = "Cooking"
        cook = Cook(current_activity)

        self.assertEquals(cook.activity, current_activity)
