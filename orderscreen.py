from kivy.uix.screenmanager import Screen
from itemscreen import ItemScreen
from kivymd.toast import toast
class OrderScreen(Screen):
    orders = []
    sources = []
    costs = []
    screen_stack = []



    def add_order(self, title, source, cost):
        self.orders.append(title)
        self.sources.append(source)
        self.costs.append(cost)

    def on_pre_enter(self, *args):
        if not self.orders:
            # User clicked shopping cart with no items added
            toast("No entrees selected")
            return
        for i, order in enumerate(self.orders):
            item_screen = ItemScreen()
            item_screen.item = order
            item_screen.name = order+"_screen"
            item_screen.cost = self.costs[i]
            item_screen.source = self.sources[i]
            self.ids.screen_manager.add_widget(item_screen)
            print("adding", order)
        self.ids.screen_manager.current = self.orders[0]+"_screen"

    def prev_screen(self):
        self.ids.screen_manager.current = self.screen_stack.pop()

    def next_screen(self):
        # Goes to a screen to complete the next item

        current_screen = self.ids.screen_manager.current
        self.screen_stack.append(current_screen)
        next_screen_index = self.orders.index(current_screen.replace("_screen", ""))+1
        if next_screen_index < len(self.orders):
            self.ids.screen_manager.current = self.orders[next_screen_index]+"_screen"
        else:
            # Went through all the orders, go to the review screen
            if current_screen != "review_screen":
                self.ids.screen_manager.current = "review_screen"
            else:
                self.ids.screen_manager.current = "order_confirmation_screen"
