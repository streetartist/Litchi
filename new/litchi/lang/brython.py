from litchi.lang.base import get_source

def brython(func):
    code = get_source(func)
    return '''<script type="text/python">{code}</script>'''.format(code=code)

class Brython:
    def __init__(self, function):
        self.function = function

    def convert(self):
        return '''
        <script type="text/python">
            {code}
        </script>
        '''.format(code=self.function)
