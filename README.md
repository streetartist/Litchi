# Litchi
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/streetartist/Litchi/HEAD)

Litchi,a framework to build website with only python.

# 介绍
- Litchi，可以让您在丝毫不写html、js、css的情况下，只用python代码，轻松编写**动态**网页。
- 与Illumine结合时，您可以使用Litchi的静态页面生成功能，愉快地编写网页。
- 就算您是开发纯静态前端页面的开发者，用Litchi，您能有一种新的开发方式，又有什么损失呢？
- Litchi受到Kivy的深度影响，并使用Flask驱动

# 安装
现在您可以通过
```shell
pip install litchi-web
```
来安装

[Pypi数据](https://pypistats.org/packages/litchi-web)

# 更新
- 增加Brython支持
- 增加Session支持（测试）

# 实例
```python
from litchi.app import App
from litchi.uix.button import Button

class IndexApp(App):
    def press(self):
        return "Oh,do not press me!!"
    def build(self):
        self.button = Button(text="Hello,litchi!", on_pressed=self.press, id = "Button1")
    
IndexApp().run(model='server')
```

# 技术
jQuery ajax() 方法

jQuery AJAX 方法 jQuery AJAX 方法

## 实例

使用 AJAX 请求改变 <div> 元素的文本：

```js
$("button").click(function(){
    $.ajax({url:"demo_test.txt",success:function(result){
        $("#div1").html(result);
    }});
});
```

定义和用法
ajax() 方法用于执行 AJAX（异步 HTTP）请求。

所有的 jQuery AJAX 方法都使用 ajax() 方法。该方法通常用于其他方法不能完成的请求。

语法
$.ajax({name:value, name:value, ... })
该参数规定 AJAX 请求的一个或多个名称/值对。
