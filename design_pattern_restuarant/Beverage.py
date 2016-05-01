import abc

class Beverage(object):
    __metaclass__ = abc.ABCMeta

    description = "Some Beverage"

    def __init__(self, name, size):
        self.name = name
        self.size = size


    def get_beverage_description(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass