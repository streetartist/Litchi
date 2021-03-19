from litchi.lang.base import get_source
from litchi.app import session, app

import re

'''

            @app.route('/ajax/<id>/<event>', methods=['POST','GET'])
            def ajax(id, event):
                for element in elements:
                    if element.id == id:
                        if event == 'click':
                            return jsonify(
'''

def server(func):
    function = get_source(func)
    re.search("\s\S*\s*=\s*\s\S*",function)
    for i in result.groups():
        re.search("\w*",i)
        function.replace(i,"session["+i+"])
    
    @app()
    def main():
        pass
    exec(
        function
    )
        
