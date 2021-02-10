from litchi.lang.base import get_source
from litchi.app import session

import re

def server(func):
    function = get_source(func)
    re.search("\s\S*\s*=\s*\s\S*",function)
    for i in result.groups():
        re.search("\w*",i)
        function.replace(i,"session["+i+"])
    exec(
        function
    )
        
