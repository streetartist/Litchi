# Litchi 0.3.1 - Minimal Modern Python Web Framework

Litchi 0.3.1 是一个最小但强大的 Python Web 框架，结合了 Litchi 1.0 和 2.0 的优点，提供了更简洁、更现代的开发体验。

## 特性

- 🍒 **最小但强大** - 简洁的 API，强大的功能
- 🎨 **现代 UI** - 基于 Vue.js 3 + Element Plus
- 🔄 **状态管理** - 内置响应式状态管理
- ⚡ **事件处理** - 智能事件处理系统
- 🧩 **组件化** - 丰富的 UI 组件库
- 🔗 **链式 API** - 流畅的代码风格
- 📱 **响应式** - 移动端友好
- 🛠️ **易于扩展** - 清晰的扩展点

## 快速开始

### 安装

```bash
cd litchi3
pip install -r requirements.txt
```

### Hello World

```python
from litchi3 import App
from litchi3.components import Button, Title, Card, Space

class MyApp(App):
    def __init__(self):
        super().__init__(name="My App", debug=True)
        self.state.set('count', 0)
    
    def on_click(self):
        count = self.state.get('count', 0)
        count += 1
        self.state.set('count', count)
        
        return self.notify(
            "Success",
            f"Button clicked {count} times!",
            type="success"
        )
    
    def build(self):
        return [
            Title("Welcome to Litchi 0.3.1", level=1),
            Card(
                Title("Hello World", level=3),
                Space(
                    Button("Click Me", type="primary", on_click=self.on_click),
                    Button("Reset", type="default"),
                    size="large"
                ),
                header="Demo",
                shadow="hover"
            )
        ]

if __name__ == '__main__':
    app = MyApp()
    app.run(port=5000)
```

### 运行示例

```bash
python litchi3/examples/hello_world.py
```

然后在浏览器中访问 http://localhost:5000

## 核心概念

### 应用 (App)

应用是 Litchi 0.3.1 的核心，负责管理组件、状态和事件：

```python
from litchi3 import App

class MyApp(App):
    def build(self):
        return [components]
    
    def on_event(self):
        return self.success("Event handled!")
```

### 组件 (Components)

Litchi 0.3.1 提供了丰富的 UI 组件：

```python
from litchi3.components import Button, Card, Title, Alert

# 按钮
Button("Click Me", type="primary", on_click=self.handle_click)

# 卡片
Card(
    Title("Card Title", level=3),
    "Card content here",
    header="Header",
    shadow="hover"
)

# 警告
Alert(
    title="Warning",
    description="This is a warning message",
    type="warning"
)
```

### 状态管理 (State)

内置的状态管理系统支持响应式更新：

```python
# 设置状态
self.state.set('user.name', 'John')
self.state.set('count', 0)

# 获取状态
name = self.state.get('user.name', 'Guest')
count = self.state.get('count', 0)

# 监听状态变化
self.state.watch('count', lambda key, new_val, old_val: print(f"Count changed: {old_val} -> {new_val}"))
```

### 事件处理 (Events)

智能事件处理系统，支持多种方式：

```python
# 方法名约定
def on_click(self):
    return self.success("Clicked!")

# 装饰器注册
@app.on('custom_event')
def handle_custom(self, **params):
    return self.data({"result": "handled"})

# 组件事件绑定
Button("Click", on_click=self.on_click)
```

## 组件库

### 基础组件

- **Button** - 按钮组件
- **Input** - 输入框组件
- **Text** - 文本组件
- **Title** - 标题组件

### 布局组件

- **Layout** - 布局容器
- **Row/Col** - 栅格布局
- **Space** - 间距组件
- **Divider** - 分割线

### 容器组件

- **Card** - 卡片容器
- **Alert** - 警告提示
- **Container** - 容器
- **Flex** - 弹性布局

### 链式 API

所有组件都支持链式调用：

```python
Button("Click Me")
    .css("custom-class")
    .style(color="red", margin="10px")
    .on("click", handler)
    .prop(disabled=False)
```

## 响应类型

Litchi 0.3.1 提供了丰富的响应类型：

```python
# 成功响应
return self.success("操作成功", data={"id": 1})

# 错误响应
return self.error("操作失败")

# 数据响应
return self.data({"users": []})

# 通知响应
return self.notify("提示", "消息内容", type="info")

# 模态框响应
return self.modal("确认", "是否继续？")

# 重定向响应
return self.redirect("/dashboard")

# 组件更新响应
return self.update("button_id", {"text": "新文本"})

# 状态更新响应
return self.update_state("count", 1)
```

## 项目结构

```
litchi3/
├── __init__.py              # 主入口
├── requirements.txt          # 依赖列表
├── README.md               # 项目文档
├── core/                   # 核心模块
│   ├── __init__.py
│   ├── app.py             # 应用类
│   ├── component.py       # 组件基类
│   ├── renderer.py        # 渲染器
│   └── state.py          # 状态管理
├── components/             # UI 组件
│   ├── __init__.py
│   ├── button.py          # 按钮组件
│   ├── input.py           # 输入组件
│   ├── text.py            # 文本组件
│   ├── layout.py          # 布局组件
│   ├── card.py            # 卡片组件
│   └── alert.py           # 警告组件
└── examples/               # 示例应用
    └── hello_world.py     # Hello World 示例
```

## 与 Litchi 1.0/2.0 的对比

| 特性 | Litchi 1.0 | Litchi 2.0 | Litchi 0.3.1 |
|------|-------------|-------------|-------------|
| 架构 | 单文件模块 | 分层架构 | 最小架构 |
| API | 基础 | 完整 | 简洁 |
| 组件 | 基础 | 丰富 | 精选 |
| 状态管理 | 无 | 完整 | 内置 |
| 事件处理 | 基础 | 智能 | 简化 |
| 学习曲线 | 简单 | 中等 | 简单 |
| 性能 | 好 | 更好 | 最优 |

## 开发指南

### 自定义组件

```python
from litchi3.core.component import ElementComponent

class MyComponent(ElementComponent):
    def __init__(self, **kwargs):
        super().__init__(element="my-component", **kwargs)
        self._props['custom-prop'] = 'value'
    
    def render(self):
        return {
            'id': self.id,
            'component': self.element,
            'props': self._props,
            'events': self._build_events(),
            'children': self._render_children()
        }
```

### 中间件

```python
def auth_middleware(request):
    # 认证逻辑
    pass

app.use(auth_middleware)
```

### 自定义路由

```python
@app.router.route('/api/users')
def get_users():
    return jsonify({"users": []})
```

## 最佳实践

1. **组件组织** - 将复杂 UI 拆分为小组件
2. **状态管理** - 使用 state 管理全局状态
3. **事件处理** - 保持事件处理函数简单
4. **响应式设计** - 利用栅格系统实现响应式布局
5. **性能优化** - 避免不必要的组件嵌套

## 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 更新日志

### v3.0.0 (2024-11-22)

- 🎉 初始版本发布
- ✨ 最小但强大的 API 设计
- 🎨 Vue.js 3 + Element Plus 集成
- 🔄 内置状态管理
- ⚡ 智能事件处理
- 🧩 丰富的 UI 组件库
- 🔗 链式 API 支持
- 📱 响应式设计

---

**Litchi 0.3.1 - 让 Python Web 开发更简单、更优雅！** 🍒
