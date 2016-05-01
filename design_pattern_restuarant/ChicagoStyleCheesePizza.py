from Pizza import Pizza

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style"
        self.description = "Chicago Style Deep Dish Cheese Pizza"
        self.toppings.append('Cheese', 'Tomato')
        self.is_vegan = False
        self.price = 10.0

    def cut(self):
        print("Cutting into square pieces")