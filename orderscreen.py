from kivy.uix.screenmanager import Screen, FadeTransition, NoTransition
from itemscreen import ItemScreen
from kivymd.toast import toast
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors

class OrderScreen(Screen):
    meals = []  # List of Meal objects (entrees) that the user has added to cart
    screen_stack = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def remove_meal(self, meal_name):
        sm = self.ids.screen_manager
        meal_to_remove = None
        for meal in self.meals:
            print(meal_name, meal.name)
            if meal.name == meal_name:
                meal_to_remove = meal
        self.meals.remove(meal_to_remove)
        for screen in sm.screens:
            if screen.name == meal_to_remove.name + "_screen":
                sm.screens.remove(screen)
        # Subtract the total cost
        review_screen = self.ids.review_screen
        review_screen.ids.total.text = str(float(review_screen.ids.total.text)
                                           - meal_to_remove.get_total_cost())


    def on_leave(self, *args):
        screens_to_remove = []
        for screen in self.ids.screen_manager.screens:
            if screen.name == "review_screen" or screen.name == "order_confirmation_screen":
                continue
            else:
                screens_to_remove.append(screen)
        for screen in screens_to_remove:
            self.ids.screen_manager.screens.remove(screen)
        self.ids.screen_manager.current = "review_screen"

    def on_pre_enter(self, *args):
        if not self.meals:
            # User clicked shopping cart with no items added
            toast("No entrees selected")
            return
        for i, meal in enumerate(self.meals):
            item_screen = ItemScreen()
            item_screen.screen_number = str(i+1)
            item_screen.meal = meal
            item_screen.item = meal.name
            item_screen.name = meal.name+str(i)+"_screen"
            item_screen.cost = meal.cost
            item_screen.source = meal.source
            self.ids.screen_manager.add_widget(item_screen)
        self.ids.screen_manager.transition = NoTransition()
        self.ids.screen_manager.current = self.meals[0].name+"0_screen"
        self.ids.screen_manager.transition = FadeTransition(clearcolor=get_color_from_hex(colors['Light']['Background']))


    def prev_screen(self):
        sm = self.ids.screen_manager
        sm.current = sm.previous()

    def next_screen(self):
        # If in the review screen, go to the order confirmation screen
        sm = self.ids.screen_manager
        if sm.current == "review_screen" or sm.current == "order_confirmation_screen":
            sm.current = sm.next()
            return
        # Only move to next entree screen if they've selected a side and drink
        current_screen_widget = sm.children[0]
        #if not current_screen_widget.meal.side.name:
        #    toast("Please select a side")
        #elif not current_screen_widget.meal.drink.name:
        #    toast("Please select a drink")
        #else:
        #    sm.current = sm.next()
        sm.current = sm.next()
