from litchi.app import App
from litchi.uix.button import Button
from litchi.lang.brython import brython, Brython

class IndexApp(App):
    @brython
    def code():
        from browser import document
        document <= "Hello !"
    def press(self):
        return "Oh,do not press me!!"
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, hold="", id = "Button1")
        self.webcode = Brython(function=self.code)
        return [self.button,self.webcode]
    
IndexApp().run(model='server').run()
