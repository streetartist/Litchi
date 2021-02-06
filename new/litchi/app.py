# App code goes there.

import inspect
import re
from itertools import dropwhile

def get_function_body(func):
    # print()
    # print("{func.__name__}'s body:".format(func=func))
    source_lines = inspect.getsourcelines(func)[0]
    source_lines = dropwhile(lambda x: x.startswith('@'), source_lines)
    source = ''.join(source_lines)
    pattern = re.compile(r'(async\s+)?def\s+\w+\s*\(.*?\)\s*:\s*(.*)', flags=re.S)
    lines = pattern.search(source).group(2).splitlines()
    if len(lines) == 1:
        return lines[0]
    else:
        indentation = len(lines[1]) - len(lines[1].lstrip())
        return '\n'.join([lines[0]] + [line[indentation:] for line in lines[1:]])

def brython(x):
    code = get_function_body(foo())
    return "<script type="text/javascript">{code}</script>".format(code=code)

'''
@brython
def foo():
    print("bar")


def func():
    def inner(a, b='a:b'):
        print (100)
        a = c + d
        print ('woof!')
        def inner_inner():
            print (200)
            print ('spam!')
    return inner

def func_one_liner(): print (200); print (a, b, c)

print (get_function_body(foo))
print (get_function_body(func()))
print (get_function_body(func_one_liner))

func_one_liner = some_decorator(func_one_liner)
print (get_function_body(func_one_liner))
输出：

print("bar")

print (100)
a = c + d
print ('woof!')
def inner_inner():
    print (200)
    print ('spam!')

print (200); print (a, b, c)
print (200); print (a, b, c)
'''

from flask import Flask, jsonify

class App:
    def run(self, model):
        elements = self.build()
        html_begin = '''
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script type="text/javascript" src="https://cdn.bootcdn.net/ajax/libs/brython/3.9.1/brython.min.js"></script>
                <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.5.1.min.js"></script>
                <link href="https://cdn.bootcdn.net/ajax/libs/pure/2.0.3/pure-min.css" rel="stylesheet">
            </head>
            <body onload="brython()">
        '''
        # To use Brython,use<script type="text/javascript">You code</script>
        for element in elements:
            html_begin += element.convert()
        html = html_begin + '''
            </body>
        </html>
        '''
        #return html
        
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
