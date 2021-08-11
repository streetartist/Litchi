from metapensiero.pj.__main__ import transform_string

class Py2js:
    def __init__(self, function):
        self.function = function
        self.litchi = None

    def convert(self):
        return '''
<script>
    {code}
</script>
        '''.format(code=transform_string(self.function))
