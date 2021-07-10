from sys import path

path.append(r"C:/Users/yuzhou/Desktop/Litchi-main/")

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
        self.button = Button(text="Hello,litchi!", on_pressed="self.press", id = "Button1")
        self.webcode = Brython(function=self.code)

IndexApp().run(model='server')