from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager, MDScreenManager
from kivymd.uix.screen import Screen, MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from views.list_view import ListViewScreen
from views.list_detail import ListDetailScreen
from views.list_edit import ListEditScreen

class ListApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Orange"

        self.sm = ScreenManager()

        # Add screens to the screen manager
        self.sm.add_widget(Screen(name="list_view"))
        self.sm.add_widget(Screen(name="list_detail"))
        self.sm.add_widget(Screen(name="list_edit"))

        # Set the initial screen
        self.switch_screen("list_view")
        return self.sm

    def switch_screen(self, screen_name, list_id=None):
        self.sm.clear_widgets()

        if screen_name == "list_view":
            screen = Screen(name="list_view")
            screen.add_widget(ListViewScreen(self.switch_screen))
        elif screen_name == "list_detail":
            screen = Screen(name="list_detail")
            screen.add_widget(ListDetailScreen(list_id, self.switch_screen))
        elif screen_name == "list_edit":
            screen = Screen(name="list_edit")
            screen.add_widget(ListEditScreen(list_id, self.switch_screen))

        self.sm.add_widget(screen)
        self.sm.current = screen_name

if __name__ == "__main__":
    ListApp().run()
