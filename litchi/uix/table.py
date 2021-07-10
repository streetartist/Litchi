class Table:
    def __init__(self, table, on_pressed, hold, id):
        self.table = table # [("",""),(("",""),("",""))]
        self.id = id
        self.on_pressed = on_pressed
        self.litchi = None
    def convert(self):
        return '''
        <table class="pure-table" id="{id}">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Make</th>
                    <th>Model</th>
                    <th>Year</th>
                </tr>
            </thead>

            <tbody>
                <tr class="pure-table-odd">
                    <td>1</td>
                    <td>Honda</td>
                    <td>Accord</td>
                    <td>2009</td>
                </tr>
            </tbody>
        </table>
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
