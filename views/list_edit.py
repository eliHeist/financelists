from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from database import session, Item

class ListEditScreen(BoxLayout):
    def __init__(self, list_id, switch_screen, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.switch_screen = switch_screen
        self.list_id = list_id

        # Item name input
        self.item_name = MDTextField(hint_text="Item Name", size_hint_y=None, height="48dp")
        self.add_widget(self.item_name)

        # Quantity input
        self.quantity = MDTextField(hint_text="Quantity", text="1", size_hint_y=None, height="48dp")
        self.add_widget(self.quantity)

        # Amount input
        self.amount = MDTextField(hint_text="Amount", size_hint_y=None, height="48dp")
        self.add_widget(self.amount)

        # Add item button
        self.add_button = MDRaisedButton(text="Add Item", on_press=self.add_item, size_hint=(None, None), size=("200dp", "48dp"), pos_hint={"center_x": 0.5})
        self.add_widget(self.add_button)

        # Back button
        self.back_button = MDFlatButton(text="Back", on_press=lambda x: self.switch_screen("list_detail", self.list_id))
        self.add_widget(self.back_button)

    def add_item(self, instance):
        new_item = Item(
            list_id=self.list_id,
            name=self.item_name.text.strip(),
            quantity=int(self.quantity.text),
            amount=float(self.amount.text),
        )
        session.add(new_item)
        session.commit()
        self.switch_screen("list_detail", self.list_id)
