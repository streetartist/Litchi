from litchi.lang.base import get_function_body
import re

def server(x):
    return x

class Button:
    def __init__(self, function):
        self.function = function
    def run(self):
        exec(
            re.search(self.function,"\s\S*\s*=\s*\s\S*")
        )
