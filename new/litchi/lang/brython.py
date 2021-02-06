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
    return "<script type="text/python">{code}</script>".format(code=code)

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

class Brython:
    def __init__(self, function):
        self.function = function

    def convert(self):
        return '''
        <script type="text/python">
            {code}
        </script>
        '''.format(code=self.function)
