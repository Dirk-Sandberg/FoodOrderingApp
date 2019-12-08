class FoodItem():
    name = ""
    cost = 0.0

    def __init__(self, name, cost, source=""):
        """
        :param name: Name of the consumable (string)
        :param cost: The price of the consumable (float)
        :param source: Path to an image of the consumable (string)
        """
        self.name = name
        self.cost = cost
        self.source = source


class Side(FoodItem):
    pass


class Drink(FoodItem):
    pass


class Meal(FoodItem):
    entree_cost = 0.0
    side = Side("", 0.0)
    drink = Side("", 0.0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side = Side("", 0.0)
        self.drink = Drink("", 0.0)

    def get_total_cost(self):
        side_cost = self.side.cost if self.side else 0.0
        drink_cost = self.drink.cost if self.drink else 0.0
        return self.cost + side_cost + drink_cost


