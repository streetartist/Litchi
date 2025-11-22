"""
Renderer for Litchi 0.3.1
"""

from typing import Any, Dict, List, Optional
import json
from datetime import datetime


class Renderer:
    """
    Minimal but powerful renderer for Litchi 0.3.1
    """
    
    def __init__(self):
        """Initialize renderer"""
        pass
    
    def render(self, components: List[Any], context: Dict[str, Any], app: Any) -> str:
        """
        Render components to HTML
        
        Args:
            components: List of components to render
            context: Global context
            app: App instance
            
        Returns:
            HTML string
        """
        # Render components to Vue configuration
        vue_config = []
        for component in components:
            if hasattr(component, 'render'):
                try:
                    rendered = component.render()
                    if isinstance(rendered, dict):
                        vue_config.append(rendered)
                    else:
                        # Convert to text component
                        vue_config.append({
                            'id': f"text_{len(vue_config)}",
                            'component': 'span',
                            'props': {},
                            'events': {},
                            'children': [str(rendered)]
                        })
                except Exception as e:
                    if app.debug:
                        print(f"Error rendering component {type(component).__name__}: {e}")
                    continue
            else:
                # Convert to text component
                vue_config.append({
                    'id': f"text_{len(vue_config)}",
                    'component': 'span',
                    'props': {},
                    'events': {},
                    'children': [str(component)]
                })
        
        # Generate HTML
        html = self._generate_html(vue_config, context, app)
        return html
    
    def _generate_html(self, vue_config: List[Dict[str, Any]], context: Dict[str, Any], app: Any) -> str:
        """Generate HTML from Vue configuration"""
        
        # Inline JavaScript for event handling
        js_code = self._generate_js(vue_config)
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app.name}</title>
    
    <!-- Element Plus CSS -->
    <link rel="stylesheet" href="https://unpkg.com/element-plus@2.4.0/dist/index.css">
    
    <!-- Vue 3 -->
    <script src="https://unpkg.com/vue@3.3.0/dist/vue.global.js"></script>
    
    <!-- Element Plus -->
    <script src="https://unpkg.com/element-plus@2.4.0/dist/index.full.js"></script>
    
    <!-- Axios -->
    <script src="https://unpkg.com/axios@1.5.0/dist/axios.min.js"></script>
    
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
            background-color: #f5f7fa;
        }}
        
        #app {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .litchi-container {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }}
        
        .litchi-loading {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            font-size: 18px;
            color: #909399;
        }}
        
        /* Custom animations */
        .fade-enter-active, .fade-leave-active {{
            transition: opacity 0.3s;
        }}
        
        .fade-enter-from, .fade-leave-to {{
            opacity: 0;
        }}
        
        /* Responsive design */
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            
            .litchi-container {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div id="app">
        <div v-if="loading" class="litchi-loading">
            <el-loading-directive></el-loading-directive>
        </div>
        
        <div v-else>
            <recursive-component 
                v-for="item in components" 
                :key="item.id"
                :component="item"
            />
        </div>
    </div>

    <script>
        // Vue 3 Application
        const {{ createApp, ref, reactive, onMounted }} = Vue;
        
        // Component configurations
        const componentConfigs = {json.dumps(vue_config, indent=2)};
        
        // Debug: log component configurations
        console.log('Component configurations:', componentConfigs);
        
        // Event handling state
        let eventProcessing = false;
        
        // Event handler function
        function handleEvent(componentId, eventName, event) {{
            // Prevent default behavior
            if (event && event.preventDefault) {{
                event.preventDefault();
            }}
            
            // Avoid duplicate rapid events
            if (eventProcessing) {{
                console.log('Event already processing, skipping');
                return false;
            }}
            
            eventProcessing = true;
            
            const params = {{
                component_id: componentId,
                event: eventName,
                params: {{
                    target: event.target ? event.target.value : undefined,
                    timestamp: new Date().toISOString()
                }}
            }};
            
            console.log('Sending event:', eventName, 'for component:', componentId);
            
            axios.post('/api/event', params)
                .then(response => {{
                    const data = response.data;
                    console.log('Event response:', data);
                    
                    if (data.success) {{
                        // Handle notifications
                        if (data.data && data.data.notification) {{
                            const notification = data.data.notification;
                            ElementPlus.ElMessage({{
                                message: notification.message,
                                type: notification.type || 'info',
                                duration: 3000
                            }});
                        }}
                        
                        // Handle modals
                        if (data.data && data.data.modal) {{
                            const modal = data.data.modal;
                            ElementPlus.ElMessageBox.alert(modal.message, modal.title, {{
                                type: modal.type || 'info',
                                confirmButtonText: '确定'
                            }});
                        }}
                        
                        // Handle redirects
                        if (data.data && data.data.redirect) {{
                            window.location.href = data.data.redirect;
                        }}
                        
                        // Handle reloads
                        if (data.data && data.data.reload) {{
                            window.location.reload();
                        }}
                        
                        // Handle component updates
                        if (data.data && data.data.component_update) {{
                            const update = data.data.component_update;
                            const component = componentConfigs.find(c => c.id === update.id);
                            if (component) {{
                                Object.assign(component.props, update.updates);
                            }}
                        }}
                        
                        // Handle state updates
                        if (data.data && data.data.state_update) {{
                            const stateUpdates = data.data.state_update;
                            Object.keys(stateUpdates).forEach(key => {{
                                globalState[key] = stateUpdates[key];
                            }});
                        }}
                        
                        // Show success message if present
                        if (data.message && !data.data) {{
                            ElementPlus.ElMessage({{
                                message: data.message,
                                type: 'success',
                                duration: 2000
                            }});
                        }}
                    }} else {{
                        // Show error message
                        ElementPlus.ElMessage({{
                            message: data.error || '操作失败',
                            type: 'error',
                            duration: 3000
                        }});
                    }}
                }})
                .catch(error => {{
                    console.error('Event handling error:', error);
                    ElementPlus.ElMessage({{
                        message: '网络错误，请稍后重试',
                        type: 'error',
                        duration: 3000
                    }});
                }})
                .finally(() => {{
                    eventProcessing = false;
                }});
            
            return false;
        }}
        
        // Define recursive component
        const RecursiveComponent = {{
            name: 'RecursiveComponent',
            props: {{
                component: {{
                    type: Object,
                    required: true
                }}
            }},
            setup(props) {{
                const bindAttrs = () => {{
                    const attrs = {{ ...props.component.props }};
                    // Add event listeners
                    if (props.component.events) {{
                        Object.entries(props.component.events).forEach(([eventName, handler]) => {{
                            const onEventName = 'on' + eventName.charAt(0).toUpperCase() + eventName.slice(1);
                            attrs[onEventName] = (event) => {{
                                handleEvent(props.component.id, eventName, event);
                            }};
                        }});
                    }}
                    return attrs;
                }};
                
                return {{
                    bindAttrs
                }};
            }},
            template: `
                <component 
                    :is="component.component" 
                    v-bind="bindAttrs()"
                >
                    <template v-for="(child, index) in component.children" :key="child.id || index">
                        <recursive-component 
                            v-if="typeof child === 'object' && child && child.component"
                            :component="child"
                        />
                        <span v-else-if="typeof child !== 'object'">{{{{ child }}}}</span>
                    </template>
                </component>
            `
        }};
        
        // Global state object
        const globalState = {{}};
        
        // Create Vue app
        const app = createApp({{
            setup() {{
                const loading = ref(true);
                const components = ref(componentConfigs);
                
                onMounted(() => {{
                    loading.value = false;
                }});
                
                return {{
                    loading,
                    components
                }};
            }}
        }});
        
        // Register recursive component
        app.component('recursive-component', RecursiveComponent);
        
        // Use Element Plus
        app.use(ElementPlus);
        
        // Mount app
        app.mount('#app');
        
        // Global error handler
        window.addEventListener('error', function(event) {{
            console.error('Global error:', event.error);
        }});
        
        // Unhandled promise rejection handler
        window.addEventListener('unhandledrejection', function(event) {{
            console.error('Unhandled promise rejection:', event.reason);
        }});
    </script>
</body>
</html>"""
        
        return html
    
    def _generate_js(self, vue_config: List[Dict[str, Any]]) -> str:
        """Generate JavaScript code for components"""
        # This is a simplified version - in a full implementation,
        # you might want to generate more sophisticated JavaScript
        return f"""
        // Component configurations
        const components = {json.dumps(vue_config, indent=2)};
        
        // Initialize components
        components.forEach(config => {{
            console.log('Initializing component:', config.id, config.component);
        }});
        """