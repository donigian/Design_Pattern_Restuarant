from Order import Order
from Menu_Distributor import Menu_Distributor

class Server(Menu_Distributor):
    def __init__(self, name):
        Menu_Distributor.__init__(self)
        self.name = name
        self.order = None
        self._is_busy = False

    def __str__(self):
        return "{0}: '{1}' is_busy: {2}".format(type(self).__name__, self.name, self._is_busy)

    @property
    def is_busy(self):
        return self._is_busy

    @is_busy.setter
    def is_busy(self, new_value):
        print('Server is busy...')
        try:
            self._is_busy = new_value
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()

    def hand_out_menu(self):
        print('Server hands out Menu')

    def take_order(self, order):
        self.order = order
        print('Server takes customer order')

    def serve_order(self, order):
        return order

    def bring_bill(self):
        pass