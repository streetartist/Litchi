from litchi.lang.base import get_function_body
from litchi.app import session

import re

def server(x):
    return x

class Button:
    def __init__(self, function):
        self.function = function
    def convert(self):
        re.search("\s\S*\s*=\s*\s\S*",self.function)
        for i in result.groups():
            re.search("\w*",i)
            self.function.replace(i,"session["+i+"])
        exec(
            self.function
        )
