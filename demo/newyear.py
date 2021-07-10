from litchi.app import App
from litchi.uix.label import H1
from litchi.uix.html import HTML
from litchi.uix.button import Button
from litchi.lang.brython import brython, Brython

class IndexApp(App):
    @brython
    def code():
        from browser import document
        import random
        document <= html.B("新年快乐",id="wish")
        wish = [
            "一岁一礼，一寸欢喜。",
            "新年到，往事清零，开心延续！",
            "百毒不侵年年好，牛转钱坤步步高!"
        ]
        def action(event):
            document["wish"].text = wish[random.randit(0,2)]
        for button in document.select("button"):
            button.bind("click", action)
    def build(self):
        self.webcode = Brython(function=self.code)
        return [self.webcode]
    
IndexApp().run(model='server').run()
