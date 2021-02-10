import inspect

def get_source(func):  
    code=""
    for line in inspect.getsourcelines(func)[0][2:]:
        code+=line[4:]
    return code
