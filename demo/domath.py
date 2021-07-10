from sys import path

path.append(r"C:/Users/yuzhou/Desktop/Litchi-main/")

from litchi.app import App
from litchi.uix.button import Button
from litchi.lang.brython import brython, Brython
from litchi.uix.html import HTML

class IndexApp(App):
    @brython
    def code():
        from browser import document, html

        # Construction de la calculatrice
        calc = html.TABLE()
        calc <= html.TR(html.TH(html.DIV("0", id="result"), colspan=3) +
                        html.TD("C"))
        lines = ["789/", "456*", "123-", "0.=+"]

        calc <= (html.TR(html.TD(x) for x in line) for line in lines)

        document <= calc

        result = document["result"] # direct acces to an element by its id

        def action(event):
            """Handles the "click" event on a button of the calculator."""
            # The element the user clicked on is the attribute "target" of the
            # event object
            element = event.target
            # The text printed on the button is the element's "text" attribute
            value = element.text
            if value not in "=C":
                # update the result zone
                if result.text in ["0", "error"]:
                    result.text = value
                else:
                    result.text = result.text + value
            elif value == "C":
                # reset
                result.text = "0"
            elif value == "=":
                # execute the formula in result zone
                try:
                    result.text = eval(result.text)
                except:
                    result.text = "error"

        # Associate function action() to the event "click" on all buttons
        for button in document.select("td"):
            button.bind("click", action)

    style='''
<style>
*{
    font-family: sans-serif;
    font-weight: normal;
    font-size: 1.1em;
}
td{
    background-color: #ccc;
    padding: 10px 30px 10px 30px;
    border-radius: 0.2em;
    text-align: center;
    cursor: default;
}
#result{
    border-color: #000;
    border-width: 1px;
    border-style: solid;
    padding: 10px 30px 10px 30px;
    text-align: right;
}
</style>
    '''
    def press(self):
        return "Oh,do not press me!!"
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, id = "Button1")
        self.webcode = Brython(function=self.code)
        self.html = HTML(code=self.style)
        return [self.button,self.webcode,self.html]
    
IndexApp().run(model='server').run()
