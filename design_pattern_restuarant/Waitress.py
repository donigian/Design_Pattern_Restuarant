from Order import Order
from Menu_Distributor import Menu_Distributor

class Waitress(Menu_Distributor):
    def __init__(self, name):
        Menu_Distributor.__init__(self)
        self.name = name
        self._is_busy = 0

    def __str__(self):
        return "{}: '{}' is_busy: {}".format(type(self).__name__, self.name, self._is_busy)

    @property
    def is_busy(self):
        return self._is_busy

    @is_busy.setter
    def is_busy(self, new_value):
        try:
            self._is_busy = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()

    def take_order(self, order):
        print("Waitress take order")
        self.order = order

    def place_order(self):
        print("Waitress place order")
        self.order.execute()