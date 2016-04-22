class Order:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print("Default regular order")

def regular_order():
        print("regular order")

def modified_order():
        print("modified order")

order = Order()

regular_order = Order(regular_order)

modified_order = Order(modified_order)

regular_order.execute()