from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from database import session, List

class ListViewScreen(BoxLayout):
    def __init__(self, switch_screen, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.switch_screen = switch_screen

        # Title label
        self.list_label = MDLabel(text="Lists", theme_text_color="Secondary", halign="center", size_hint_y=None, height="48dp")
        self.add_widget(self.list_label)

        # Scrollable list
        self.scroll = ScrollView()
        self.add_widget(self.scroll)

        # Scroll view content
        self.content = MDList()
        self.scroll.add_widget(self.content)

        self.refresh_list()

        # Add new list button
        self.add_button = MDRaisedButton(text="Add New List", on_press=self.add_list, size_hint=(None, None), size=("280dp", "48dp"), pos_hint={"center_x": 0.5})
        self.add_widget(self.add_button)

    def refresh_list(self):
        self.content.clear_widgets()
        lists = session.query(List).all()
        for lst in lists:
            card = MDCard(size_hint=(None, None), size=("280dp", "120dp"), pos_hint={"center_x": 0.5})
            card.add_widget(MDLabel(text=lst.name, theme_text_color="Primary", halign="center", size_hint_y=None, height="40dp"))
            card.add_widget(MDRaisedButton(text="View", on_press=lambda x, lst=lst: self.view_list(lst.id), size_hint=(None, None), size=("150dp", "40dp"), pos_hint={"center_x": 0.5}))
            self.content.add_widget(card)

    def add_list(self, instance):
        new_list = List(name=f"List {len(session.query(List).all()) + 1}")
        session.add(new_list)
        session.commit()
        self.refresh_list()

    def view_list(self, list_id):
        self.switch_screen("list_detail", list_id)
