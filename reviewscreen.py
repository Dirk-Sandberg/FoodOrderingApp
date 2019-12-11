from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.card import MDCard


class ReviewCard(MDCard):
    pass

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty

class ReviewScreen(Screen):
    a = ObjectProperty(None)

    def animate_fab(self, *args):
        fab = self.ids.fab
        fab2 = self.ids.fab2

        self.a = Animation(y = fab.y+dp(15), duration=.200, transition='out_quart')
        self.a.bind(on_complete=self.animate_fab_down)
        self.a.start(fab2)

    def animate_fab_down(self, *args):
        fab = self.ids.fab
        fab2 = self.ids.fab2

        self.a = Animation(y=fab.y, transition='out_bounce')
        self.a.bind(on_complete=self.animate_fab)
        self.a.start(fab2)

    def remove_cards(self):
        cards_to_remove = []
        for card in self.ids.card_list.children:
            if isinstance(card, ReviewCard):
                cards_to_remove.append(card)
        for card in cards_to_remove:
            self.ids.card_list.remove_widget(card)

    def set_fields(self):
        orders_screen = App.get_running_app().root.ids.order_screen
        total_label = self.ids.total
        for meal in orders_screen.meals:
            card = ReviewCard()
            card.name = meal.name
            card.cost = meal.get_total_cost()
            card.side = meal.side.name + ", " + meal.drink.name
            self.ids.card_list.add_widget(card)
            total_label.text = str(float(total_label.text) + card.cost)
        self.ids.card_list.add_widget(ReviewCard(opacity=0))