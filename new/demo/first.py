from litchi.app import App
from litchi.uix.button import Button

class IndexApp(App):
    def press(self):
        self.button.text("Oh,do not press me!!")
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, hold="")
        return [self.button,]
    
print(IndexApp().run(model="server"))
