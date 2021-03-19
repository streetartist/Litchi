from litchi.lang.base import get_source

def server(func):
    function = get_source(func)

    re.search("\s\S*\s*=\s*\s\S*",function) # 将变量定义加上session

    for i in result.groups():
        re.search("\w*",i)
        function.replace(i,"session["+i+"])

    return function
        
