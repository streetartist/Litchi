from litchi.app import App
from litchi.uix.button import Button

class IndexApp(App):
    def press(self):
        return "Oh,do not press me!!"
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, hold="", id = "Button1")
        return [self.button,]
    
IndexApp().run(model='server').run()
