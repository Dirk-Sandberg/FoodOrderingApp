import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from menuscreen import MenuScreen
from restaurantmanager import RestaurantScreenManager
from orderscreen import OrderScreen
from reviewscreen import ReviewScreen
from fooditem import Side, Drink, Meal
from kivymd.uix.dialog import ListMDDialog
from kivymd.toast import toast

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.behaviors.ripplebehavior import RectangularRippleBehavior
from kivymd.theming import ThemableBehavior
from kivy.uix.behaviors import ButtonBehavior
class Test(ThemableBehavior, RectangularRippleBehavior, ButtonBehavior,
                BoxLayout):
    pass

class RestaurantNavDrawer(MDNavigationDrawer):
    pass

from kivymd.uix.list import TwoLineRightIconListItem
class SideListItem(TwoLineRightIconListItem):
    pass
class DrinkListItem(TwoLineRightIconListItem):
    pass


class MainApp(MDApp):
    sides = []
    drinks = []
    meals = []
    drink_popup = None
    sides_popup = None

    def on_start(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '700'
        self.create_sides()
        self.create_drinks()


    def create_drinks(self):
        drinks = [["Fountain Drink", "images/fountain_drink.jpeg", "No charge"], ["Dasani", "images/water.jpg", "0.99"], ["Lemonade", "images/lemonade.jpg", "0.99"]]
        for i in range(len(drinks)):
            drink = DrinkListItem()
            drink.text = drinks[i][0]
            drink.source = drinks[i][1]
            cost = 0.0 if drinks[i][2] == "No charge" else float(drinks[i][2])
            drink.cost = cost
            drink.secondary_text = "add $"+str(cost) if drinks[i][2] != "No charge" else drinks[i][2]
            self.drinks.append(drink)

    def create_sides(self):
        sides = [["White rice", "images/white_rice.jpeg", "No charge"], ["Fried rice", "images/fried_rice.jpg", "0.99"], ["Noodles", "images/noodles.jpg", "0.99"]]
        for i in range(len(sides)):
            side = SideListItem()
            side.text = sides[i][0]
            side.source = sides[i][1]
            cost = 0.0 if sides[i][2] == "No charge" else float(sides[i][2])
            side.cost = cost
            side.secondary_text = "add $"+str(cost) if sides[i][2] != "No charge" else sides[i][2]
            self.sides.append(side)

    def add_to_cart(self, name, source, cost):
        toast("Added " + name + " to your cart.")
        meal = Meal(name, cost, source)
        self.meals.append(meal)
        self.root.ids.order_screen.add_meal(meal)
        #self.root.ids.order_screen.add_order(name, source, cost)

    def display_choose_side_menu(self, item_screen):
        self.sides_popup = ListMDDialog()
        self.sides_popup.title = "Select a side"
        self.sides_popup.size_hint = (.8, .8)
        for side in self.sides:
            if side.parent:
                side.parent.remove_widget(side)
            side.dialog = self.sides_popup
            side.item_screen = item_screen
            self.sides_popup.ids.list_layout.add_widget(side)

        self.sides_popup.open()

    def display_choose_drink_menu(self, item_screen):
        self.drink_popup = ListMDDialog()
        self.drink_popup.title = "Select a drink"
        self.drink_popup.size_hint = (.8, .8)
        for drink in self.drinks:
            if drink.parent:
                drink.parent.remove_widget(drink)
            drink.dialog = self.drink_popup
            drink.item_screen = item_screen
            self.drink_popup.ids.list_layout.add_widget(drink)
        self.drink_popup.open()




MainApp().run()

