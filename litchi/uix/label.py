class P:
    def __init__(self, text, on_pressed, hold, id):
        self.text = text
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None
    def convert(self):
        return '''
        <p id="{id}">{text}</p>
        <script>
            $('#{id}').click(function(){{
                $.ajax({{
                    url:"/ajax/{id}/click",
                    type:"post",
                    success:function(result){{
                        $("#{id}").html(result);
                }}}});
            }});
        </script>
        '''.format(id=self.id, text=self.text)
            
    def text(self,change):
        return change


class H1:
    def __init__(self, text, on_pressed, hold, id):
        self.text = text
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None
    def convert(self):
        return '''
        <h1 id="{id}">{text}</h1>
        <script>
            $('#{id}').click(function(){{
                $.ajax({{
                    url:"/ajax/{id}/click",
                    type:"post",
                    success:function(result){{
                        $("#{id}").html(result);
                }}}});
            }});
        </script>
        '''.format(id=self.id, text=self.text)
            
    def text(self,change):
        return change


class A:
    def __init__(self, text, on_pressed, hold, id):
        self.text = text
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None
    def convert(self):
        return '''
        <a id="{id}">{text}</a>
        <script>
            $('#{id}').click(function(){{
                $.ajax({{
                    url:"/ajax/{id}/click",
                    type:"post",
                    success:function(result){{
                        $("#{id}").html(result);
                }}}});
            }});
        </script>
        '''.format(id=self.id, text=self.text)
            
    def text(self,change):
        return change

class Img:
    def __init__(self, src, on_pressed, hold, id):
        self.src = src
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None
    def convert(self):
        return '''
        <img id="{id}" src="{src}"></img>
        <script>
            $('#{id}').click(function(){{
                $.ajax({{
                    url:"/ajax/{id}/click",
                    type:"post",
                    success:function(result){{
                        $("#{id}").html(result);
                }}}});
            }});
        </script>
        '''.format(id=self.id, src=self.src)
            
    def src(self,change):
        return change
