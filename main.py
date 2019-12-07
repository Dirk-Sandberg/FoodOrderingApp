from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from menuscreen import MenuScreen
from restaurantmanager import RestaurantScreenManager
from orderscreen import OrderScreen
from reviewscreen import ReviewScreen
from kivymd.uix.dialog import ListMDDialog
from kivymd.toast import toast


class RestaurantNavDrawer(MDNavigationDrawer):
    pass

class Side(TwoLineAvatarIconListItem):
    pass
class Drink(TwoLineAvatarIconListItem):
    pass


class MainApp(MDApp):
    sides = []
    drinks = []
    drink_popup = None
    sides_popup = None

    def on_start(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'DeepOrange'
        self.theme_cls.accent_hue = '200'
        self.create_sides()
        self.create_drinks()


    def create_drinks(self):
        drinks = [["Fountain Drink", "images/food1.jpg", "No charge"], ["Dasani", "images/food1.jpg", "0.99"], ["Lemonade", "images/food1.jpg", "0.99"]]
        for i in range(len(drinks)):
            drink = Drink()
            drink.text = drinks[i][0]
            drink.source = drinks[i][1]
            cost = 0.0 if drinks[i][2] == "No charge" else float(drinks[i][2])
            drink.cost = cost
            drink.secondary_text = "add $"+str(cost) if drinks[i][2] != "No charge" else drinks[i][2]
            self.drinks.append(drink)

    def create_sides(self):
        sides = [["White rice", "images/food1.jpg", "No charge"], ["Fried rice", "images/food1.jpg", "0.99"], ["Noodles", "images/food1.jpg", "0.99"]]
        for i in range(len(sides)):
            side = Side()
            side.text = sides[i][0]
            side.source = sides[i][1]
            cost = 0.0 if sides[i][2] == "No charge" else float(sides[i][2])
            side.cost = cost
            side.secondary_text = "add $"+str(cost) if sides[i][2] != "No charge" else sides[i][2]
            self.sides.append(side)

    def add_to_cart(self, thing, source, cost):
        print("Should have an item class")
        toast("Added " + thing + " to your cart.")
        self.root.ids.order_screen.add_order(thing, source, cost)

    def display_choose_side_menu(self, item_screen):
        if not self.sides_popup:
            self.sides_popup = ListMDDialog()
            self.sides_popup.title = "Select a side"
            self.sides_popup.size_hint = (.8, .8)
            for side in self.sides:
                side.dialog = self.sides_popup
                side.item_screen = item_screen
                self.sides_popup.ids.list_layout.add_widget(side)
        self.sides_popup.open()

    def display_choose_drink_menu(self, item_screen):
        if not self.drink_popup:
            self.drink_popup = ListMDDialog()
            self.drink_popup.title = "Select a drink"
            self.drink_popup.size_hint = (.8, .8)
            for drink in self.drinks:
                drink.dialog = self.drink_popup
                drink.item_screen = item_screen
                self.drink_popup.ids.list_layout.add_widget(drink)
        self.drink_popup.open()




MainApp().run()
