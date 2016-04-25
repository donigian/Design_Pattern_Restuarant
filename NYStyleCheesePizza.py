from Pizza import Pizza

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style"
        self.description = "NY Style Sauce & Cheese Pizza"
        self.toppings.append('Cheese')
        self.toppings.append('Reggiano')
        self.is_vegan = False
        self.price = 12.0

    def cut(self):
        print("Cutting into long thin pieces")
