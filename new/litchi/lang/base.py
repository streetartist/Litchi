import inspect

def get_source(func):  
    code=""
    first = True
    for line in inspect.getsourcelines(func)[0][2:]:
        if first:
            code+=line[4:]
            first=False
        else:
            code+=line
    return code
