from Command import Command
from Cook import Cook

class Order(Command):
    def __init__(self, cook, func=None):
        if func:
            self.execute = func
        self.cook = cook

    def execute(self):
        print("Regular order ready")

    def cook(self):
        print("Order class: Cooking")

