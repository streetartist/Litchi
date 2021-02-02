# App code goes there.
class App:
    def run(self):
        elements = self.build()
        html_begin = '''
            <html>
                <body>
        '''
        for element in elements:
            html_begin += element.convert()
        html = html_begin + '''
            </body>
        </html>
        '''
        return html
        
        app = Flask(__name__)

        @app.route('/',methods=['GET','POST']):
        def web():
            pass
