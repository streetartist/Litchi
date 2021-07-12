# App code goes there.
from flask import Flask, jsonify, session

def del_waste(self, wastes):
    waste = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', \ 
        'build', 'run', 'generate',]
    
    production = []

    for i in wastes:
        j = getattr(self, i)

        if i not in waste and hasattr(j, "litchi") == True:
            production.insert(0, j)

    return production

class App:
    def generate(self, model):
        elements = self.build() if self.build() != None else del_waste(self, dir(self))
        # 如有返回，使用返回顺序
        # print(elements)

        html_begin = '''
<!DOCTYPE HTML>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script type="text/javascript"
            src="https://cdn.jsdelivr.net/npm/brython@3.9.1/brython.min.js">
        </script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.5.1.min.js"></script>
        <link href="https://cdn.bootcdn.net/ajax/libs/pure/2.0.3/pure-min.css" rel="stylesheet">
    </head>
    <body onload="brython()">
        '''
        # To use Brython,use<script type="text/python">You code</script>
        for element in elements:
            html_begin += element.convert()
        html = html_begin + '''
    </body>
</html>
        '''
        if model== "static":
            return html
        else:
            self.app = Flask(__name__)

            @self.app.route('/',methods=['GET','POST'])
            def web():
                return html

            @self.app.route('/ajax/<id>/<event>', methods=['POST','GET'])
            def ajax(id, event):
                for element in elements:
                    if element.id == id:
                        if event == 'click':
                            return jsonify(element.on_pressed())
        
            return self.app

    def run(self, model, *args):
        self.generate(mode).run(*args)

