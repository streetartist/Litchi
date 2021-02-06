from litchi.lang.base import get_function_body

def server(x):
    return x

class Button:
    def __init__(self, function):
        self.function = function
    def run(self):
        exec(
            '''
            @app.route(
            '''.format(id=self.id, text=self.text)
        )
            
    def text(self,change):
        return change
