
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.12, 0.09, 1)

class EarnovaApp(App):
    def build(self):
        self.balance = 0

        main = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="[b]EARNOVA[/b]",
            markup=True,
            font_size=32,
            color=(0.3, 1, 0.6, 1),
            size_hint_y=None,
            height=65
        )
        main.add_widget(title)

        main.add_widget(Label(
            text="Earn More. Grow More.",
            font_size=18,
            size_hint_y=None,
            height=35
        ))

        self.wallet = Label(
            text="Your Demo Balance: 0 Points",
            font_size=23,
            size_hint_y=None,
            height=90
        )
        main.add_widget(self.wallet)

        buttons = GridLayout(
            cols=2,
            spacing=12
        )

        options = [
            "Daily Tasks",
            "Watch Ads",
            "Refer Friends",
            "My Wallet"
        ]

        for option in options:
            btn = Button(
                text=option,
                font_size=18,
                background_normal="",
                background_color=(0.08, 0.4, 0.25, 1)
            )
            btn.bind(on_press=self.select_option)
            buttons.add_widget(btn)

        main.add_widget(buttons)

        self.message = Label(
            text="Welcome to Earnova!",
            font_size=16
        )
        main.add_widget(self.message)

        return main

    def select_option(self, button):
        self.message.text = (
            button.text + " - Coming Soon!"
        )

EarnovaApp().run()
                      
