from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ajax/<id>/<event>', methods=['POST','GET'])
def ajax(id, event):
    return jsonify('opsssss')

@app.route('/')
def indexs():
    return '''
    <!DOCTYPE HTML>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-3.5.1.min.js"></script>
            <link href="https://cdn.bootcdn.net/ajax/libs/pure/2.0.3/pure-min.css" rel="stylesheet">
        </head>
        <body>
            <button class="pure-button pure-button-primary" id="Button1">Hello!</button>
            <script>
                $('#Button1').click(function(){
                    $.ajax({
                        url:"http://127.0.0.1:5000/ajax/Button1/click",
                        type:"post",
                        success:function(result){
                            $("#Button1").html(result);
                    }});
                });
            </script>
        </body>
    </html>
    '''

app.run()