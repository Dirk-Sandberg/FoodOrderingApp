from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.card import MDCard


class ReviewCard(MDCard):
    pass


class ReviewScreen(Screen):
    def remove_cards(self):
        cards_to_remove = []
        for card in self.ids.card_list.children:
            if isinstance(card, ReviewCard):
                cards_to_remove.append(card)
        for card in cards_to_remove:
            self.ids.card_list.remove_widget(card)

    def set_fields(self):
        orders_screen = App.get_running_app().root.ids.order_screen
        for meal in orders_screen.meals:
            card = ReviewCard()
            card.name = meal.name
            card.cost = meal.get_total_cost()
            card.side = meal.side.name + ", " + meal.drink.name
            self.ids.card_list.add_widget(card)
