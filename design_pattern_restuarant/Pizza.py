import abc

class Pizza(object):
    __metaclass__ = abc.ABCMeta

    name = ""
    price = 0.0
    description = ""
    is_vegan = False
    toppings = []

    def prepare(self):
        pass
    def bake(self):
        pass
    def cut(self):
        pass
    def box(self):
        pass
