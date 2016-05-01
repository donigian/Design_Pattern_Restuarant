class Order_Status(object):
    status = None

class Ready_To_Order(Order_Status):
    def __init__(self):
        print("Customer ready to order...")

    def ready_to_order(self):
        self.state = Order_Taken

class Order_Taken(Order_Status):
    def __init__(self):
        print("Server took order...")

class Preparing_Order(Order_Status):
    def __init__(self):
        print("Cook preparing order...")

class Order_Prepared(Order_Status):
    def __init__(self):
        print("Cook prepared order...")

order = Ready_To_Order()
order.status = order.ready_to_order()