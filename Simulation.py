import Restuarant
import Cook

class Simulation(object):

    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def run(self):
        restuarant = Restuarant()
        restuarant.location = "411 Arroyo Parkway"

        another_restuarant = Restuarant()
        print(another_restuarant.location)

        c = Cook("preparing BLT")
        c.prepare_meal()
