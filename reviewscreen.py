from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.card import MDCard


class ReviewCard(MDCard):
    pass


from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.dialog import ListMDDialog

from kivymd.uix.list import TwoLineListItem
class LocationListItem(TwoLineListItem):
    pass

class ReviewScreen(Screen):
    a = ObjectProperty(None)
    location_popup = ObjectProperty(None)
    location = StringProperty("") # Address of location to pick up from

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

    def display_choose_location_menu(self):#, item_screen):
        self.location_popup = ListMDDialog()
        self.location_popup.title = "Select a location"
        self.location_popup.size_hint = (.8, .8)
        locations = self.get_locations()
        for location in locations:
            location = LocationListItem(text=location[0], secondary_text=location[1])
            if location.parent:
                location.parent.remove_widget(location)
            location.dialog = self.location_popup
            #location.item_screen = item_screen
            location.screen = self
            self.location_popup.ids.list_layout.add_widget(location)
        self.location_popup.open()

    def get_locations(self):
        """Get locations from some kind of online database.

        :return:
        """
        locations = [["182 W Ridley Pl.", self.distance_to_location(0,0)+ " miles away"]]
        locations *= 3
        return locations


    def distance_to_location(self, lat, lon):
        """Calculate distance in miles from user's phone's GPS to restaurant
        location."""
        return "3.12"