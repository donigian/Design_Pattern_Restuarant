from Order import Order

class Waitress:
    def __init__(self):
        pass

    def take_order(self, order):
        print("Waitress take order")
        self.order = order

    def place_order(self):
        print("Waitress place order")
        self.order.execute()