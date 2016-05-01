from Pasadena_Restuarant import Pasadena_Restuarant
from Cook import Cook
from Customer import Customer
from Server import Server

class Simulation(object):

    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

    def run(self):
        pasadena_CPK = Pasadena_Restuarant("CPK Pasadena")
        print(pasadena_CPK.name)

        customer = Customer("Anderson Silva")
        server = Server('Holly Holm')
        if customer.ready_to_order('NYStyle'):
            pizza_order = pasadena_CPK.order_pizza(customer.name_of_pizza)
            server.take_order(pizza_order)
            server.serve_order()
            server.bring_bill()
            customer.pay_bill_by_cc()
