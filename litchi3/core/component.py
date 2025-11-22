"""
Core component classes for Litchi 0.3.1
"""

from typing import Any, Dict, List, Optional, Callable, Union
from abc import ABC, abstractmethod
import uuid


class Component(ABC):
    """
    Base component class for Litchi 0.3.1
    
    Minimal but powerful component system with chainable API
    """
    
    def __init__(
        self,
        id: Optional[str] = None,
        css_class: Optional[Union[str, List[str]]] = None,
        style: Optional[Union[str, Dict[str, str]]] = None,
        **kwargs
    ):
        """Initialize component with basic properties"""
        self.id = id or f"litchi_{uuid.uuid4().hex[:8]}"
        self._props: Dict[str, Any] = {}
        self._events: Dict[str, Callable] = {}
        self._children: List[Any] = []
        
        # Handle CSS classes
        if css_class:
            if isinstance(css_class, list):
                self._props['class'] = ' '.join(css_class)
            else:
                self._props['class'] = css_class
        
        # Handle styles
        if style:
            if isinstance(style, dict):
                self._props['style'] = '; '.join(f"{k}: {v}" for k, v in style.items())
            else:
                self._props['style'] = style
        
        # Handle other properties and events
        for key, value in kwargs.items():
            if key.startswith('on_'):
                event_name = key[3:]  # Remove 'on_' prefix
                self.on(event_name, value)
            else:
                self._props[key] = value
    
    def on(self, event: str, handler: Union[Callable, str]) -> 'Component':
        """Add event handler"""
        self._events[event] = handler
        return self
    
    def prop(self, **props) -> 'Component':
        """Set properties"""
        self._props.update(props)
        return self
    
    def css(self, *classes) -> 'Component':
        """Add CSS classes"""
        current_classes = self._props.get('class', '').split()
        for cls in classes:
            if cls and cls not in current_classes:
                current_classes.append(cls)
        self._props['class'] = ' '.join(current_classes)
        return self
    
    def style(self, **styles) -> 'Component':
        """Add CSS styles"""
        current_style = self._props.get('style', '')
        new_styles = '; '.join(f"{k}: {v}" for k, v in styles.items())
        
        if current_style:
            self._props['style'] = f"{current_style}; {new_styles}"
        else:
            self._props['style'] = new_styles
        
        return self
    
    def child(self, *children) -> 'Component':
        """Add child components"""
        for child in children:
            if child is not None:
                self._children.append(child)
        return self
    
    def _build_events(self) -> Dict[str, str]:
        """Build events dictionary for frontend"""
        events = {}
        for event_name, handler in self._events.items():
            if callable(handler):
                events[event_name] = f"handleEvent('{self.id}', '{event_name}', $event)"
            elif isinstance(handler, str):
                events[event_name] = handler
        return events
    
    def _render_children(self) -> List[Any]:
        """Render child components"""
        rendered = []
        for child in self._children:
            if child is None:
                continue
            elif hasattr(child, 'render'):
                rendered.append(child.render())
            elif isinstance(child, (str, int, float, bool)):
                rendered.append(str(child))
            elif isinstance(child, dict):
                rendered.append(child)
            elif isinstance(child, list):
                rendered.extend(child)
        return rendered
    
    @abstractmethod
    def render(self) -> Dict[str, Any]:
        """Render component to configuration dictionary"""
        pass
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id='{self.id}')>"


class ElementComponent(Component):
    """
    Element Plus component base class
    """
    
    def __init__(self, element: str, **kwargs):
        """Initialize Element Plus component"""
        super().__init__(**kwargs)
        self.element = f"el-{element}"
    
    def render(self) -> Dict[str, Any]:
        """Render Element Plus component"""
        return {
            'id': self.id,
            'component': self.element,
            'props': self._props.copy(),
            'events': self._build_events(),
            'children': self._render_children()
        }


class HtmlComponent(Component):
    """
    HTML component base class
    """
    
    def __init__(self, tag: str = 'div', **kwargs):
        """Initialize HTML component"""
        super().__init__(**kwargs)
        self.tag = tag
    
    def render(self) -> Dict[str, Any]:
        """Render HTML component"""
        return {
            'id': self.id,
            'component': self.tag,
            'props': self._props.copy(),
            'events': self._build_events(),
            'children': self._render_children()
        }
