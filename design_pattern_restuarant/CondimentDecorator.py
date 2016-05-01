import abc

from design_pattern_restuarant.Beverage import Beverage


class CondimentDecorator(Beverage):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_beverage_description(self):
        pass