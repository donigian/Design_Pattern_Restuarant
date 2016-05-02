class Customer:
    def __init__(self, name):
        self.name = name
        self.name_of_pizza = ''

    def pay_bill_by_cc(self, amount):
        print('Finished paying {0} by credit card').format(amount)
        return True

    def ready_to_order(self, name_of_pizza):
        self.name_of_pizza = name_of_pizza
        print('Customer ready to order %s') % (name_of_pizza)
        return True