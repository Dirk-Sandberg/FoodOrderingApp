from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.card import MDCard

class ReviewCard(MDCard):
    pass

class ReviewScreen(Screen):
    def set_fields(self):
        orders_screen = App.get_running_app().root.ids.order_screen
        for i in range(len(orders_screen.orders)):
            name = orders_screen.orders[i]
            cost = orders_screen.costs[i]
            card = ReviewCard()
            card.name = name
            card.cost = cost
            card.drink_cost =
            self.ids.card_list.add_widget(card)


        pass