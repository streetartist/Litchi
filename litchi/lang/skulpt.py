class Skulpt:
    def __init__(self, function):
        self.function = function
        self.litchi = None
        self.require = '''
<script src="https://cdn.jsdelivr.net/npm/skulpt/dist/skulpt.min.js" type="text/javascript"></script>    
<script src="https://cdn.jsdelivr.net/npm/skulpt/dist/skulpt-stdlib.js" type="text/javascript"></script>
        '''

    def convert(self):
        return '''
<script type="text/javascript">

        function outf(text) {{
            var mypre = document.getElementById("output");  //
            mypre.innerHTML = mypre.innerHTML + text;  //文字输出
        }}
        function builtinRead(x) {{
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }}
         
        function runit() {{
            console.log("runit is going")
            var prog = "{code}"
            var mypre = document.getElementById("output");   //获取输出框
            mypre.innerHTML = '';
            Sk.pre = "output";
            Sk.configure({{ output: outf, read: builtinRead, __future__: Sk.python3 }});
 
            (Sk.TurtleGraphics || (Sk.TurtleGraphics = {{}})).target = 'mycanvas';
            var myPromise = Sk.misceval.asyncToPromise(function () {{
                return Sk.importMainWithBody("<stdin>", false, prog, true);
            }});
 
            myPromise.then(function (mod) {{
                console.log('success');    //执行成功，显示success
            }},
                function (err) {{
                    console.log(err.toString());   //执行失败，在控制台显示 err
                }});
        }}

runit();
    </script>
    
    <!-- 文字输出部分 -->
    <pre id="output"></pre>
    <!-- 画图输出部分 -->
    <div id="mycanvas"></div>
</body>
</html>
        '''.format(code=self.function)
