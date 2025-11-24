from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from database import session, Item, List

class ListDetailScreen(BoxLayout):
    def __init__(self, list_id, switch_screen, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.switch_screen = switch_screen
        self.list_id = list_id

        list_obj = session.query(List).filter_by(id=list_id).first()
        self.list_label = MDLabel(text=f"List: {list_obj.name}", theme_text_color="Primary", halign="center", size_hint_y=None, height="48dp")
        self.add_widget(self.list_label)

        # Scrollable item list
        self.scroll = ScrollView()
        self.add_widget(self.scroll)

        self.content = MDList()
        self.scroll.add_widget(self.content)

        self.refresh_items()

        # Back button
        self.back_button = MDFlatButton(text="Back", on_press=lambda x: self.switch_screen("list_view"))
        self.add_widget(self.back_button)

    def refresh_items(self):
        self.content.clear_widgets()
        items = session.query(Item).filter_by(list_id=self.list_id).all()
        for item in items:
            item_label = MDLabel(text=f"{item.name} - {item.quantity} x {item.amount}", theme_text_color="Secondary", halign="center", size_hint_y=None, height="40dp")
            self.content.add_widget(item_label)

        total_amount = sum([item.quantity * item.amount for item in items])
        total_label = MDLabel(text=f"Total: {total_amount}", theme_text_color="Primary", halign="center", size_hint_y=None, height="48dp")
        self.content.add_widget(total_label)

        # Edit list button
        self.edit_button = MDRaisedButton(text="Edit List", on_press=lambda x: self.switch_screen("list_edit", self.list_id), size_hint=(None, None), size=("200dp", "48dp"), pos_hint={"center_x": 0.5})
        self.add_widget(self.edit_button)
