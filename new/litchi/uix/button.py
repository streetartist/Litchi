# Button code goes there.
class Button:
    def __init__(self, text, on_pressed, hold, id):
        self.text = text
        self.id = id
        self.on_pressed = on_pressed
    def convert(self):
        return '''
        <button class="pure-button pure-button-primary" id="{id}">{text}</button>
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
        # <button class="pure-button pure-button-primary" id="'+self.id+'">' + self.text + "</button>"+
            
    def text(self,change):
        return change
