# Button code goes there.
class Button:
    def __init__(self, text, on_pressed, hold):
        self.text = text
    def convert(self):
        return "<button>{self.text}</button>"
