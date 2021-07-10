# Button code goes there.
class Button:
    def __init__(self, text, on_pressed, id, hold="server"):
        self.text = text
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None #! 用于确认是否是Litch对象

    def convert(self):
        if not callable(self.on_pressed):
            return '''
<button class="pure-button pure-button-primary" id="{id}">{text}</button>
<script>
    $('#{id}').click(function(){{
        $("#{id}").html("{change}");
    }});
</script>
            '''.format(id=self.id, text=self.text, change = self.on_pressed)
        else:
            return '''
<button class="pure-button pure-button-primary" id="{id}">{text}</button>
<script>
    $('#{id}').click(function(){{
        $.ajax({{
            url:"/ajax/{id}/click",
            type:"post",
            success:function(result){{
                $("#{id}").html(result);
            }}
        }});
    }});
</script>
            '''.format(id=self.id, text=self.text)
            # <button class="pure-button pure-button-primary" id="'+self.id+'">' + self.text + "</button>"+
            
    def text(self,change):
        return change
