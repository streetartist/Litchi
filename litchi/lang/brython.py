class Brython:
    def __init__(self, function):
        self.function = function
        self.litchi = None

    def convert(self):
        return '''
<script type="text/python">
    {code}
</script>
        '''.format(code=self.function)
