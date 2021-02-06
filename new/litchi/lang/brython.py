from litchi.lang.base import get_function_body

def brython(x):
    code = get_function_body(x())
    return "<script type="text/python">{code}</script>".format(code=code)

class Brython:
    def __init__(self, function):
        self.function = function

    def convert(self):
        return '''
        <script type="text/python">
            {code}
        </script>
        '''.format(code=self.function)
