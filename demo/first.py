from litchi.app import App
from litchi.uix import Button

class IndexApp(App):
    def press(self):
        self.button.text("Oh,do not press me!!")
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, hold="")
        return self.button

IndexApp.run(model="server")
