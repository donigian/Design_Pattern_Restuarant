from Restuarant import Restuarant
from NYStyleCheesePizza import NYStyleCheesePizza
from ChicagoStyleCheesePizza import ChicagoStyleCheesePizza

class Pasadena_Restuarant(Restuarant):

    def create_pizza(self, item):
        if item == "NYStyle":
            print("Creating NYStyle Pizza")
            return NYStyleCheesePizza()
        elif item == "ChiTownStyle":
            print("Creating ChiTownStyle Pizza")
            return ChicagoStyleCheesePizza()
        else:
            raise TypeError("Type of Pizza not available")