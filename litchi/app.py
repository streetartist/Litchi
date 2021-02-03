# App code goes there.
class App:
    def run(self, model):
        elements = self.build()
        html_begin = '''
<html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    </head>
    <body>
        <div id="app">
        '''
        for element in elements:
            html_begin += element.convert()
        html = html_begin + '''
        </div>
    </body>
</html>
        '''
        return html
        
        app = Flask(__name__)

        @app.route('/',methods=['GET','POST'])
        def web():
            pass
