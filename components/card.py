"""
Card components for Litchi 0.3.1
"""

from typing import Any, Optional, Union
from ..core.component import ElementComponent


class Card(ElementComponent):
    """
    Card component based on Element Plus
    """
    
    def __init__(
        self,
        *content,
        header: Optional[str] = None,
        body_style: Optional[dict] = None,
        shadow: str = "always",
        **kwargs
    ):
        """
        Initialize Card component
        
        Args:
            *content: Card content
            header: Card header text
            body_style: Body style dictionary
            shadow: Shadow effect (always, hover, never)
            **kwargs: Additional properties
        """
        super().__init__(
            element="card",
            **kwargs
        )
        
        # Set card properties
        self._props['shadow'] = shadow
        
        if body_style:
            # Convert dict to CSS string
            style_str = '; '.join(f"{k}: {v}" for k, v in body_style.items())
            self._props['body-style'] = style_str
        
        # Add header if provided
        if header:
            self._props['header'] = header
        
        # Add content as children
        for item in content:
            if item is not None:
                self.child(item)
    
    def set_header(self, header: str) -> 'Card':
        """Set card header"""
        self._props['header'] = header
        return self
    
    def set_body_style(self, style: dict) -> 'Card':
        """Set body style"""
        style_str = '; '.join(f"{k}: {v}" for k, v in style.items())
        self._props['body-style'] = style_str
        return self
    
    def set_shadow(self, shadow: str) -> 'Card':
        """Set shadow effect"""
        self._props['shadow'] = shadow
        return self


class CardHeader(ElementComponent):
    """
    Card header component
    """
    
    def __init__(
        self,
        *content,
        **kwargs
    ):
        """
        Initialize CardHeader component
        
        Args:
            *content: Header content
            **kwargs: Additional properties
        """
        super().__init__(
            element="card-header",
            **kwargs
        )
        
        for item in content:
            if item is not None:
                self.child(item)


class CardBody(ElementComponent):
    """
    Card body component
    """
    
    def __init__(
        self,
        *content,
        **kwargs
    ):
        """
        Initialize CardBody component
        
        Args:
            *content: Body content
            **kwargs: Additional properties
        """
        super().__init__(
            element="card-body",
            **kwargs
        )
        
        for item in content:
            if item is not None:
                self.child(item)


class CardFooter(ElementComponent):
    """
    Card footer component
    """
    
    def __init__(
        self,
        *content,
        **kwargs
    ):
        """
        Initialize CardFooter component
        
        Args:
            *content: Footer content
            **kwargs: Additional properties
        """
        super().__init__(
            element="card-footer",
            **kwargs
        )
        
        for item in content:
            if item is not None:
                self.child(item)


# Convenience functions
def SimpleCard(*content, **kwargs) -> Card:
    """Create a simple card"""
    return Card(*content, **kwargs)


def HeaderCard(header: str, *content, **kwargs) -> Card:
    """Create a card with header"""
    return Card(*content, header=header, **kwargs)


def ShadowCard(*content, shadow: str = "hover", **kwargs) -> Card:
    """Create a card with shadow effect"""
    return Card(*content, shadow=shadow, **kwargs)


def StyledCard(*content, body_style: dict = None, **kwargs) -> Card:
    """Create a card with custom body style"""
    return Card(*content, body_style=body_style, **kwargs)


def InfoCard(title: str, content: str, **kwargs) -> Card:
    """Create an info card with title and content"""
    from .text import Title, Paragraph
    
    return Card(
        Title(title, level=4),
        Paragraph(content),
        shadow="hover",
        **kwargs
    )


def ActionCard(title: str, content: str, *actions, **kwargs) -> Card:
    """Create a card with actions"""
    from .text import Title, Paragraph
    from .layout import Space
    
    return Card(
        Title(title, level=4),
        Paragraph(content),
        Space(*actions, size="large"),
        shadow="hover",
        **kwargs
    )


def ImageCard(title: str, image_src: str, description: str = "", **kwargs) -> Card:
    """Create a card with image"""
    from .text import Title, Paragraph
    from ..core.component import HtmlComponent
    
    img = HtmlComponent(
        tag="img",
        src=image_src,
        style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px;"
    )
    
    return Card(
        img,
        Title(title, level=4),
        Paragraph(description) if description else None,
        shadow="hover",
        **kwargs
    )


def StatsCard(title: str, value: str, description: str = "", **kwargs) -> Card:
    """Create a statistics card"""
    from .text import Title, Paragraph
    from ..core.component import HtmlComponent
    
    value_display = HtmlComponent(
        tag="div",
        css="litchi-stats-value",
        style="font-size: 2em; font-weight: bold; color: #409eff; margin: 10px 0;"
    ).child(value)
    
    return Card(
        Title(title, level=5),
        value_display,
        Paragraph(description) if description else None,
        body_style={"text-align": "center"},
        shadow="hover",
        **kwargs
    )
