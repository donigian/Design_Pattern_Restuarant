from Beverage import Beverage
import abc

class CondimentDecorator(Beverage):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_beverage_description(self):
        pass