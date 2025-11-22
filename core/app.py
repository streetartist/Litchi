"""
Core application class for Litchi 0.3.1
"""

from typing import Any, Dict, List, Optional, Callable, Union
from flask import Flask, render_template_string, request, jsonify
import os
import json
import traceback
from datetime import datetime
from pathlib import Path

from .renderer import Renderer
from .state import StateManager


class App:
    """
    Main application class for Litchi 0.3.1
    
    Minimal but powerful web application framework
    """
    
    def __init__(
        self,
        name: str = "LitchiApp",
        debug: bool = False,
        **kwargs
    ):
        """Initialize Litchi application"""
        self.name = name
        self.debug = debug
        
        # Core components
        self.renderer = Renderer()
        self.state = StateManager()
        
        # Flask app instance (created lazily)
        self._flask_app: Optional[Flask] = None
        
        # Component registry
        self._components: List[Any] = []
        
        # Event handlers
        self._event_handlers: Dict[str, Callable] = {}
        
        # Component ID to event handler mapping
        self._component_handlers: Dict[str, Dict[str, Callable]] = {}
        
        # Global context
        self._context: Dict[str, Any] = {}
    
    def build(self) -> Union[Any, List[Any]]:
        """
        Build application UI
        
        Override this method in your app to define the UI structure.
        
        Returns:
            Component or list of components
        """
        return []
    
    def setup(self) -> None:
        """
        Setup hook called before app starts
        
        Override this method to initialize resources, connect to databases, etc.
        """
        pass
    
    def teardown(self) -> None:
        """
        Teardown hook called when app stops
        
        Override this method to cleanup resources.
        """
        pass
    
    # ==================== Component Management ====================
    
    def add_component(self, component: Any) -> 'App':
        """Add a component to the app"""
        self._components.append(component)
        return self
    
    def get_components(self) -> List[Any]:
        """Get all registered components"""
        return self._components
    
    def _register_component_handlers(self, component: Any) -> None:
        """
        Recursively register component event handlers by ID
        
        Args:
            component: The component to register
        """
        if not hasattr(component, 'id') or not hasattr(component, '_events'):
            return
        
        component_id = component.id
        events = component._events
        
        # Register this component's handlers
        if events:
            self._component_handlers[component_id] = events.copy()
        
        # Recursively register children
        if hasattr(component, '_children'):
            for child in component._children:
                self._register_component_handlers(child)
    
    # ==================== Event Handling ====================
    
    def on(self, event_name: str) -> Callable:
        """
        Decorator for registering event handlers
        
        Usage:
            @app.on('click')
            def handle_click(self, **params):
                return self.success("Clicked!")
        """
        def decorator(func: Callable) -> Callable:
            self._event_handlers[event_name] = func
            return func
        return decorator
    
    def emit(self, event_name: str, **params) -> Any:
        """Emit an event and call its handler"""
        handler = self._event_handlers.get(event_name)
        if handler:
            return handler(self, **params)
        return None
    
    # ==================== Context Management ====================
    
    def set_context(self, key: str, value: Any) -> 'App':
        """Set global context value"""
        self._context[key] = value
        return self
    
    def get_context(self, key: str, default: Any = None) -> Any:
        """Get global context value"""
        return self._context.get(key, default)
    
    # ==================== Response Helpers ====================
    
    def success(self, message: str, data: Any = None, **kwargs) -> Dict[str, Any]:
        """Create success response"""
        response = {
            'success': True,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        if data is not None:
            response['data'] = data
        response.update(kwargs)
        return response
    
    def error(self, message: str, **kwargs) -> Dict[str, Any]:
        """Create error response"""
        response = {
            'success': False,
            'error': message,
            'timestamp': datetime.now().isoformat()
        }
        response.update(kwargs)
        return response
    
    def data(self, data: Any, **kwargs) -> Dict[str, Any]:
        """Create data response"""
        response = {
            'success': True,
            'data': data,
            'timestamp': datetime.now().isoformat()
        }
        response.update(kwargs)
        return response
    
    def notify(
        self,
        title: str,
        message: str,
        type: str = 'info',
        **kwargs
    ) -> Dict[str, Any]:
        """Create notification response"""
        return self.data({
            'notification': {
                'title': title,
                'message': message,
                'type': type
            }
        }, **kwargs)
    
    def modal(
        self,
        title: str,
        message: str,
        type: str = 'alert',
        **kwargs
    ) -> Dict[str, Any]:
        """Create modal response"""
        return self.data({
            'modal': {
                'title': title,
                'message': message,
                'type': type
            }
        }, **kwargs)
    
    def redirect(self, url: str, **kwargs) -> Dict[str, Any]:
        """Create redirect response"""
        return self.data({
            'redirect': url
        }, **kwargs)
    
    def reload(self, **kwargs) -> Dict[str, Any]:
        """Create reload response"""
        return self.data({
            'reload': True
        }, **kwargs)
    
    def update(
        self,
        component_id: str,
        updates: Dict[str, Any],
        **kwargs
    ) -> Dict[str, Any]:
        """Create component update response"""
        return self.data({
            'component_update': {
                'id': component_id,
                'updates': updates
            }
        }, **kwargs)
    
    def update_state(self, key: str, value: Any, **kwargs) -> Dict[str, Any]:
        """Update state and return response"""
        self.state.set(key, value)
        return self.data({
            'state_update': {key: value}
        }, **kwargs)
    
    # ==================== Rendering ====================
    
    def render(self) -> str:
        """Render application to HTML"""
        try:
            # Call setup hook
            self.setup()
            
            # Build UI components
            components = self.build()
            if not isinstance(components, list):
                components = [components] if components else []
            
            # Register all component handlers
            self._component_handlers.clear()
            for component in components:
                self._register_component_handlers(component)
            
            # Render to HTML
            html = self.renderer.render(components, self._context, self)
            
            return html
            
        except Exception as e:
            if self.debug:
                return self._render_error(e)
            else:
                return self._render_error_page()
    
    def _render_error(self, error: Exception) -> str:
        """Render detailed error page for debug mode"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Litchi 0.3.1 Error</title>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: 'Segoe UI', system-ui, sans-serif;
                    margin: 0;
                    padding: 40px;
                    background: #f5f5f5;
                }}
                .error-container {{
                    max-width: 900px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .error-header {{
                    background: #f56c6c;
                    color: white;
                    padding: 20px 30px;
                }}
                .error-header h1 {{
                    margin: 0;
                    font-size: 24px;
                    font-weight: 500;
                }}
                .error-body {{
                    padding: 30px;
                }}
                .error-info {{
                    background: #fff5f5;
                    border-left: 4px solid #f56c6c;
                    padding: 15px 20px;
                    margin-bottom: 20px;
                    border-radius: 4px;
                }}
                .error-info h3 {{
                    margin: 0 0 10px 0;
                    color: #c03639;
                    font-size: 18px;
                }}
                .error-info p {{
                    margin: 5px 0;
                    color: #666;
                }}
                .traceback {{
                    background: #f8f8f8;
                    border: 1px solid #e1e1e1;
                    padding: 20px;
                    border-radius: 4px;
                    overflow-x: auto;
                }}
                .traceback pre {{
                    margin: 0;
                    font-family: 'Consolas', 'Monaco', monospace;
                    font-size: 14px;
                    line-height: 1.6;
                    color: #333;
                }}
                .debug-info {{
                    margin-top: 20px;
                    padding-top: 20px;
                    border-top: 1px solid #e1e1e1;
                }}
                .debug-info h4 {{
                    margin: 0 0 10px 0;
                    color: #666;
                    font-size: 14px;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                }}
                .debug-info table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .debug-info td {{
                    padding: 8px;
                    border-bottom: 1px solid #f0f0f0;
                }}
                .debug-info td:first-child {{
                    font-weight: 500;
                    color: #666;
                    width: 150px;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <div class="error-header">
                    <h1>🚨 Litchi 0.3.1 Application Error</h1>
                </div>
                <div class="error-body">
                    <div class="error-info">
                        <h3>{type(error).__name__}</h3>
                        <p><strong>Error:</strong> {str(error)}</p>
                    </div>
                    
                    <div class="traceback">
                        <pre>{traceback.format_exc()}</pre>
                    </div>
                    
                    <div class="debug-info">
                        <h4>Debug Information</h4>
                        <table>
                            <tr>
                                <td>App Name</td>
                                <td>{self.name}</td>
                            </tr>
                            <tr>
                                <td>Debug Mode</td>
                                <td>{self.debug}</td>
                            </tr>
                            <tr>
                                <td>Timestamp</td>
                                <td>{datetime.now().isoformat()}</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _render_error_page(self) -> str:
        """Render simple error page for production"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Application Error</title>
            <meta charset="utf-8">
            <style>
                body {
                    font-family: 'Segoe UI', system-ui, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                    background: #f5f5f5;
                }
                .error-box {
                    text-align: center;
                    padding: 40px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    max-width: 500px;
                }
                .error-icon {
                    font-size: 64px;
                    margin-bottom: 20px;
                }
                h1 {
                    margin: 0 0 10px 0;
                    color: #f56c6c;
                    font-size: 28px;
                }
                p {
                    margin: 0;
                    color: #666;
                    line-height: 1.6;
                }
            </style>
        </head>
        <body>
            <div class="error-box">
                <div class="error-icon">⚠️</div>
                <h1>Application Error</h1>
                <p>Sorry, something went wrong. Please try again later.</p>
            </div>
        </body>
        </html>
        """
    
    # ==================== Flask Integration ====================
    
    def _create_flask_app(self) -> Flask:
        """Create and configure Flask application"""
        # Get template directory
        template_dir = Path(__file__).parent.parent / 'templates'
        static_dir = Path(__file__).parent.parent / 'static'
        
        flask_app = Flask(
            self.name,
            template_folder=str(template_dir),
            static_folder=str(static_dir),
            static_url_path='/static'
        )
        
        # Configure Flask
        flask_app.config['SECRET_KEY'] = 'litchi3-secret-key-change-in-production'
        
        # Register routes
        self._register_routes(flask_app)
        
        return flask_app
    
    def _register_routes(self, flask_app: Flask) -> None:
        """Register all routes with Flask"""
        
        # Main route
        @flask_app.route('/', methods=['GET', 'POST'])
        def index():
            html = self.render()
            return html
        
        # API route for event handling
        @flask_app.route('/api/event', methods=['POST'])
        def handle_event():
            try:
                data = request.get_json()
                if not data:
                    return jsonify(self.error("No data provided")), 400
                
                event_name = data.get('event')
                action = data.get('action', event_name)  # Get action if provided, otherwise use event
                params = data.get('params', {})
                component_id = data.get('component_id')
                
                if not event_name:
                    return jsonify(self.error("Missing event name")), 400
                
                # Handle event - pass action as the event to find the correct handler
                result = self._handle_event(action, component_id, params)
                
                if result is None:
                    result = self.success("Event handled")
                
                return jsonify(result)
                
            except Exception as e:
                error_response = self.error(str(e))
                if self.debug:
                    error_response['traceback'] = traceback.format_exc()
                return jsonify(error_response), 500
        
        # State API
        @flask_app.route('/api/state/<key>', methods=['GET', 'POST'])
        def handle_state(key):
            try:
                if request.method == 'GET':
                    value = self.state.get(key)
                    return jsonify(self.data(value))
                else:
                    data = request.get_json()
                    value = data.get('value')
                    self.state.set(key, value)
                    return jsonify(self.success("State updated", value))
            except Exception as e:
                return jsonify(self.error(str(e))), 500
    
    def _handle_event(self, event_name: str, component_id: Optional[str], params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Handle event by finding appropriate handler via component ID"""
        import inspect
        
        # First, try to find handler via component_id
        if component_id and component_id in self._component_handlers:
            component_handlers = self._component_handlers[component_id]
            
            # Look for the event in this component's handlers
            if event_name in component_handlers:
                handler = component_handlers[event_name]
                if callable(handler):
                    try:
                        sig = inspect.signature(handler)
                        filtered_params = {}
                        for param_name, param in sig.parameters.items():
                            if param_name in params:
                                filtered_params[param_name] = params[param_name]
                        return handler(**filtered_params)
                    except Exception as e:
                        if self.debug:
                            raise
                        return self.error(f"Error calling handler: {str(e)}")
        
        # Fallback: Try to find method handler (on_<event_name>)
        method_name = f"on_{event_name}"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            if callable(method):
                try:
                    sig = inspect.signature(method)
                    filtered_params = {}
                    for param_name, param in sig.parameters.items():
                        if param_name in params:
                            filtered_params[param_name] = params[param_name]
                        elif param.default is inspect.Parameter.empty and param.kind not in (
                            inspect.Parameter.VAR_KEYWORD,
                            inspect.Parameter.VAR_POSITIONAL
                        ):
                            pass
                    return method(**filtered_params)
                except Exception as e:
                    if self.debug:
                        raise
                    return self.error(f"Error calling {method_name}: {str(e)}")
        
        # Fallback: Try registered event handlers
        handler = self._event_handlers.get(event_name)
        if handler:
            try:
                sig = inspect.signature(handler)
                filtered_params = {}
                for param_name, param in sig.parameters.items():
                    if param_name != 'self' and param_name in params:
                        filtered_params[param_name] = params[param_name]
                return handler(self, **filtered_params)
            except Exception as e:
                if self.debug:
                    raise
                return self.error(f"Error calling handler: {str(e)}")
        
        return None
    
    # ==================== Running ====================
    
    def run(
        self,
        host: str = '0.0.0.0',
        port: int = 5000,
        debug: Optional[bool] = None,
        **kwargs
    ) -> None:
        """Run the application"""
        if debug is not None:
            self.debug = debug
        
        # Create Flask app if not exists
        if self._flask_app is None:
            self._flask_app = self._create_flask_app()
        
        # Print startup message
        print(f"\n{'='*60}")
        print(f"  🍒 Litchi 0.3.1 - {self.name}")
        print(f"{'='*60}")
        print(f"  📍 Server: http://{host}:{port}")
        print(f"  🐛 Debug: {self.debug}")
        print(f"  ⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        # Run Flask
        try:
            self._flask_app.run(
                host=host,
                port=port,
                debug=self.debug,
                **kwargs
            )
        finally:
            # Call teardown hook
            self.teardown()
    
    def save_static(self, output_path: str = 'dist/index.html') -> str:
        """Save application as static HTML file"""
        html = self.render()
        
        # Create directory if needed
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Static HTML saved to: {output_path}")
        return str(output_file)
    
    def __repr__(self) -> str:
        return f"<App(name='{self.name}', debug={self.debug})>"
