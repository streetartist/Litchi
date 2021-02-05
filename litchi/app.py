# App code goes there.
from flask import Flask, jsonify

class App:
    def run(self, model):
        elements = self.build()
        html_begin = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.5.1.min.js"></script>
                <link href="https://cdn.bootcdn.net/ajax/libs/pure/2.0.3/pure-min.css" rel="stylesheet">
            </head>
            <body>
        '''
        for element in elements:
            html_begin += element.convert()
        html = html_begin + '''
            </body>
        </html>
        '''
        if model=="static":
            return html
        
        app = Flask(__name__)

        @app.route('/',methods=['GET','POST'])
        def web():
            return html

        @app.route('/ajax/<id>/<event>', methods=['POST','GET'])
        def ajax(id, event):
            for element in elements:
                if element.id == id:
                    if event == 'click':
                        return jsonify(element.on_pressed())
            # return jsonify('opsssss')
        
        return app
