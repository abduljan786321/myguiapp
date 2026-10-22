from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text="My First Android App",
            font_size=24,
            on_press=lambda button: setattr(button, "text", "App is Working!")
        )

MyApp().run()
