from Order import Order

class Server:
    def __init__(self, name):
        self.name = name
        self.order = None

    def hand_out_menu(self):
        print('Server hands out Menu')

    def take_order(self, order):
        self.order = order
        print('Server takes customer order')

    def serve_order(self, order):
        return order

    def bring_bill(self):
        pass