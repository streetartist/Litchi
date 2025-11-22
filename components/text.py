"""
Text components for Litchi 0.3.1
"""

from typing import Any, Optional
from ..core.component import HtmlComponent


class Text(HtmlComponent):
    """
    Text component for displaying text content
    """
    
    def __init__(
        self,
        content: str = "",
        tag: str = "span",
        **kwargs
    ):
        """
        Initialize Text component
        
        Args:
            content: Text content
            tag: HTML tag (span, p, div, etc.)
            **kwargs: Additional properties
        """
        super().__init__(tag=tag, **kwargs)
        
        if content:
            self.child(content)


class Title(HtmlComponent):
    """
    Title component for headings
    """
    
    def __init__(
        self,
        text: str = "",
        level: int = 1,
        **kwargs
    ):
        """
        Initialize Title component
        
        Args:
            text: Title text
            level: Heading level (1-6)
            **kwargs: Additional properties
        """
        if level < 1 or level > 6:
            level = 1
        
        super().__init__(tag=f"h{level}", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', '')
        if level == 1:
            self._props['style'] += 'font-size: 2em; margin: 0.67em 0; font-weight: bold;'
        elif level == 2:
            self._props['style'] += 'font-size: 1.5em; margin: 0.75em 0; font-weight: bold;'
        elif level == 3:
            self._props['style'] += 'font-size: 1.17em; margin: 0.83em 0; font-weight: bold;'
        elif level == 4:
            self._props['style'] += 'font-size: 1em; margin: 1.12em 0; font-weight: bold;'
        elif level == 5:
            self._props['style'] += 'font-size: 0.83em; margin: 1.5em 0; font-weight: bold;'
        elif level == 6:
            self._props['style'] += 'font-size: 0.75em; margin: 1.67em 0; font-weight: bold;'
        
        if text:
            self.child(text)


class Paragraph(HtmlComponent):
    """
    Paragraph component
    """
    
    def __init__(
        self,
        text: str = "",
        **kwargs
    ):
        """
        Initialize Paragraph component
        
        Args:
            text: Paragraph text
            **kwargs: Additional properties
        """
        super().__init__(tag="p", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', 'margin: 1em 0; line-height: 1.6;')
        
        if text:
            self.child(text)


class Label(HtmlComponent):
    """
    Label component
    """
    
    def __init__(
        self,
        text: str = "",
        for_id: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize Label component
        
        Args:
            text: Label text
            for_id: ID of the associated form element
            **kwargs: Additional properties
        """
        super().__init__(tag="label", **kwargs)
        
        if for_id:
            self._props['for'] = for_id
        
        # Add default styling
        self._props.setdefault('style', 'display: inline-block; margin-bottom: 5px; font-weight: 500;')
        
        if text:
            self.child(text)


class Code(HtmlComponent):
    """
    Code component for inline code
    """
    
    def __init__(
        self,
        code: str = "",
        inline: bool = True,
        **kwargs
    ):
        """
        Initialize Code component
        
        Args:
            code: Code content
            inline: Whether to use inline code or block code
            **kwargs: Additional properties
        """
        tag = "code" if inline else "pre"
        super().__init__(tag=tag, **kwargs)
        
        # Add default styling
        if inline:
            self._props.setdefault('style', 'background: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-family: monospace;')
        else:
            self._props.setdefault('style', 'background: #f5f5f5; padding: 10px; border-radius: 5px; font-family: monospace; overflow-x: auto;')
        
        if code:
            self.child(code)


class Strong(HtmlComponent):
    """
    Strong/bold text component
    """
    
    def __init__(
        self,
        text: str = "",
        **kwargs
    ):
        """
        Initialize Strong component
        
        Args:
            text: Text to make bold
            **kwargs: Additional properties
        """
        super().__init__(tag="strong", **kwargs)
        
        if text:
            self.child(text)


class Em(HtmlComponent):
    """
    Emphasis/italic text component
    """
    
    def __init__(
        self,
        text: str = "",
        **kwargs
    ):
        """
        Initialize Em component
        
        Args:
            text: Text to emphasize
            **kwargs: Additional properties
        """
        super().__init__(tag="em", **kwargs)
        
        if text:
            self.child(text)


class Small(HtmlComponent):
    """
    Small text component
    """
    
    def __init__(
        self,
        text: str = "",
        **kwargs
    ):
        """
        Initialize Small component
        
        Args:
            text: Small text
            **kwargs: Additional properties
        """
        super().__init__(tag="small", **kwargs)
        
        if text:
            self.child(text)


class Blockquote(HtmlComponent):
    """
    Blockquote component for quotes
    """
    
    def __init__(
        self,
        text: str = "",
        **kwargs
    ):
        """
        Initialize Blockquote component
        
        Args:
            text: Quote text
            **kwargs: Additional properties
        """
        super().__init__(tag="blockquote", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', 'border-left: 4px solid #ddd; margin: 1em 0; padding-left: 1em; color: #666; font-style: italic;')
        
        if text:
            self.child(text)


# Convenience functions
def H1(text: str = "", **kwargs) -> Title:
    """Create H1 title"""
    return Title(text, level=1, **kwargs)


def H2(text: str = "", **kwargs) -> Title:
    """Create H2 title"""
    return Title(text, level=2, **kwargs)


def H3(text: str = "", **kwargs) -> Title:
    """Create H3 title"""
    return Title(text, level=3, **kwargs)


def H4(text: str = "", **kwargs) -> Title:
    """Create H4 title"""
    return Title(text, level=4, **kwargs)


def H5(text: str = "", **kwargs) -> Title:
    """Create H5 title"""
    return Title(text, level=5, **kwargs)


def H6(text: str = "", **kwargs) -> Title:
    """Create H6 title"""
    return Title(text, level=6, **kwargs)


def P(text: str = "", **kwargs) -> Paragraph:
    """Create paragraph"""
    return Paragraph(text, **kwargs)


def B(text: str = "", **kwargs) -> Strong:
    """Create bold text"""
    return Strong(text, **kwargs)


def I(text: str = "", **kwargs) -> Em:
    """Create italic text"""
    return Em(text, **kwargs)


def Span(text: str = "", **kwargs) -> Text:
    """Create span text"""
    return Text(text, tag="span", **kwargs)


def Div(text: str = "", **kwargs) -> Text:
    """Create div text"""
    return Text(text, tag="div", **kwargs)
