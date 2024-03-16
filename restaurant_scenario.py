class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_total_price(self):
        return self.price
    
class Appetizers(MenuItem):
    def __init__(self, name:str, price:int, servings:int):
        super().__init__(name, price)
        self.servings = servings

class Soups(MenuItem):
    def __init__(self, name:str, price:int, type:str):
        super().__init__(name, price)
        self.type = type #cream or soup

class Salads(MenuItem):
    def __init__(self, name:str, price:int, dressing:bool):
        super().__init__(name, price)
        self.dressing = dressing

class MainCourse(MenuItem):
    def __init__(self, name:str, price:int, portion_size:int):
        super().__init__(name, price)
        self.portion_size = portion_size

class Desserts(MenuItem):
    def __init__(self, name:str, price:int, flavor:str):
        super().__init__(name, price)
        self.flavor = flavor

class Beverages(MenuItem):
    def __init__(self, name:str, price:int, alcoholic:bool):
        super().__init__(name, price)
        self.alcoholic = alcoholic

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.calculate_total_price() for item in self.items)
        return total
    
menu_items = [
    Appetizers("Carpaccio", 25000, 1),
    Appetizers("Shrimps", 35000, 1),
    Appetizers("Cheese plate", 30000, 3),
    Soups("Onion soup", 25000, "soup"),
    Soups("Tomato soup", 30000, "Cream"),
    Soups("Mushrooms soup", 25000, "Cream"),
    Salads("Cesar salad", 20000, True),
    Salads("Smoked salmon salad", 35000, False),
    Salads("Caprese salad", 25000, True),
    MainCourse("steak with wine sauce", 60000, "Medium"),
    MainCourse("Seafood risotto", 50000, "Big"),
    MainCourse("Duck in red fruits", 65000, "Small"),
    Desserts("Chocolate cake", 25000, "Chocolate"),
    Desserts("Creme brulee", 20000, "Milk"),
    Desserts("Souffle", 30000, "Red fruits"),
    Beverages("Water", 8000, False),
    Beverages("Soda", 12000, False),
    Beverages("Bottle of wine", 120000, True),
    Beverages("Bottle of champagne", 250000, True)
    ]
    
order = Order()
order.add_item(menu_items[1])
order.add_item(menu_items[4])
order.add_item(menu_items[7])
order.add_item(menu_items[11])
order.add_item(menu_items[14])
order.add_item(menu_items[15])
order.add_item(menu_items[18])

print ("Order: ")
for item in order.items:
    print("\n",(item.name, item.price))
print("\nTotal bill: ", order.calculate_total(), "COP\n")