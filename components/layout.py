"""
Layout components for Litchi 0.3.1
"""

from typing import Any, List, Optional, Union
from ..core.component import ElementComponent, HtmlComponent


class Layout(ElementComponent):
    """
    Layout container component based on Element Plus
    """
    
    def __init__(
        self,
        direction: str = "vertical",
        **kwargs
    ):
        """
        Initialize Layout component
        
        Args:
            direction: Layout direction (horizontal, vertical)
            **kwargs: Additional properties
        """
        super().__init__(
            element="container",
            **kwargs
        )
        
        if direction:
            self._props['direction'] = direction


class Row(ElementComponent):
    """
    Row component for grid layout
    """
    
    def __init__(
        self,
        gutter: int = 0,
        justify: str = "start",
        align: str = "top",
        **kwargs
    ):
        """
        Initialize Row component
        
        Args:
            gutter: Grid spacing
            justify: Horizontal alignment (start, end, center, space-around, space-between)
            align: Vertical alignment (top, middle, bottom)
            **kwargs: Additional properties
        """
        super().__init__(
            element="row",
            **kwargs
        )
        
        self._props.update({
            'gutter': gutter,
            'justify': justify,
            'align': align
        })
    


class Col(ElementComponent):
    """
    Column component for grid layout
    """
    
    def __init__(
        self,
        span: int = 24,
        offset: int = 0,
        push: int = 0,
        pull: int = 0,
        xs: Optional[int] = None,
        sm: Optional[int] = None,
        md: Optional[int] = None,
        lg: Optional[int] = None,
        xl: Optional[int] = None,
        **kwargs
    ):
        """
        Initialize Col component
        
        Args:
            span: Column span (1-24)
            offset: Left offset
            push: Right push
            pull: Left pull
            xs: Span for extra small screens (<768px)
            sm: Span for small screens (≥768px)
            md: Span for medium screens (≥992px)
            lg: Span for large screens (≥1200px)
            xl: Span for extra large screens (≥1920px)
            **kwargs: Additional properties
        """
        super().__init__(
            element="col",
            **kwargs
        )
        
        self._props.update({
            'span': span,
            'offset': offset,
            'push': push,
            'pull': pull
        })
        
        # Responsive props
        if xs is not None:
            self._props['xs'] = xs
        if sm is not None:
            self._props['sm'] = sm
        if md is not None:
            self._props['md'] = md
        if lg is not None:
            self._props['lg'] = lg
        if xl is not None:
            self._props['xl'] = xl


class Space(ElementComponent):
    """
    Space component for spacing between items
    """
    
    def __init__(
        self,
        size: Union[int, str] = "small",
        direction: str = "horizontal",
        align: str = "center",
        fill: bool = False,
        wrap: bool = False,
        **kwargs
    ):
        """
        Initialize Space component
        
        Args:
            size: Spacing size (small, default, large, or number in pixels)
            direction: Direction (horizontal, vertical)
            align: Alignment (start, end, center, baseline)
            fill: Whether to fill remaining space
            wrap: Whether to wrap items
            **kwargs: Additional properties
        """
        super().__init__(
            element="space",
            **kwargs
        )
        
        self._props.update({
            'size': size,
            'direction': direction,
            'align': align,
            'fill': fill,
            'wrap': wrap
        })
    


class Divider(ElementComponent):
    """
    Divider component
    """
    
    def __init__(
        self,
        direction: str = "horizontal",
        content_position: str = "center",
        border_style: str = "solid",
        **kwargs
    ):
        """
        Initialize Divider component
        
        Args:
            direction: Divider direction (horizontal, vertical)
            content_position: Content position (left, center, right)
            border_style: Border style (solid, dashed, dotted)
            **kwargs: Additional properties
        """
        super().__init__(
            element="divider",
            **kwargs
        )
        
        self._props.update({
            'direction': direction,
            'content-position': content_position,
            'border-style': border_style
        })


class Container(HtmlComponent):
    """
    HTML container component
    """
    
    def __init__(
        self,
        fluid: bool = False,
        **kwargs
    ):
        """
        Initialize Container component
        
        Args:
            fluid: Whether container is fluid (full width)
            **kwargs: Additional properties
        """
        super().__init__(tag="div", **kwargs)
        
        # Add container styling
        if fluid:
            self._props.setdefault('style', 'width: 100%; padding: 0 15px; margin: 0 auto;')
        else:
            self._props.setdefault('style', 'max-width: 1200px; width: 100%; padding: 0 15px; margin: 0 auto;')
        
        self.css('litchi-container')


class Flex(HtmlComponent):
    """
    Flex container component
    """
    
    def __init__(
        self,
        direction: str = "row",
        justify: str = "flex-start",
        align: str = "stretch",
        wrap: str = "nowrap",
        gap: str = "0",
        **kwargs
    ):
        """
        Initialize Flex component
        
        Args:
            direction: Flex direction (row, column, row-reverse, column-reverse)
            justify: Justify content (flex-start, flex-end, center, space-between, space-around, space-evenly)
            align: Align items (stretch, flex-start, flex-end, center, baseline)
            wrap: Flex wrap (nowrap, wrap, wrap-reverse)
            gap: Gap between items (CSS value)
            **kwargs: Additional properties
        """
        super().__init__(tag="div", **kwargs)
        
        # Add flex styling
        flex_style = f"""
            display: flex;
            flex-direction: {direction};
            justify-content: {justify};
            align-items: {align};
            flex-wrap: {wrap};
            gap: {gap};
        """
        
        self._props.setdefault('style', '')
        self._props['style'] += flex_style
        
        self.css('litchi-flex')


class Grid(HtmlComponent):
    """
    CSS Grid container component
    """
    
    def __init__(
        self,
        columns: str = "repeat(auto-fit, minmax(250px, 1fr))",
        rows: str = "auto",
        gap: str = "20px",
        **kwargs
    ):
        """
        Initialize Grid component
        
        Args:
            columns: Grid template columns (CSS value)
            rows: Grid template rows (CSS value)
            gap: Gap between grid items (CSS value)
            **kwargs: Additional properties
        """
        super().__init__(tag="div", **kwargs)
        
        # Add grid styling
        grid_style = f"""
            display: grid;
            grid-template-columns: {columns};
            grid-template-rows: {rows};
            gap: {gap};
        """
        
        self._props.setdefault('style', '')
        self._props['style'] += grid_style
        
        self.css('litchi-grid')


class Section(HtmlComponent):
    """
    Section component
    """
    
    def __init__(
        self,
        **kwargs
    ):
        """Initialize Section component"""
        super().__init__(tag="section", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', 'padding: 20px 0;')
        self.css('litchi-section')


class Header(HtmlComponent):
    """
    Header component
    """
    
    def __init__(
        self,
        sticky: bool = False,
        **kwargs
    ):
        """
        Initialize Header component
        
        Args:
            sticky: Whether header is sticky
            **kwargs: Additional properties
        """
        super().__init__(tag="header", **kwargs)
        
        # Add default styling
        style = 'padding: 20px 0; background: white; border-bottom: 1px solid #eee;'
        if sticky:
            style += 'position: sticky; top: 0; z-index: 100;'
        
        self._props.setdefault('style', style)
        self.css('litchi-header')


class Footer(HtmlComponent):
    """
    Footer component
    """
    
    def __init__(
        self,
        **kwargs
    ):
        """Initialize Footer component"""
        super().__init__(tag="footer", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', 'padding: 20px 0; background: #f8f9fa; border-top: 1px solid #eee; margin-top: 40px;')
        self.css('litchi-footer')


class Main(HtmlComponent):
    """
    Main content component
    """
    
    def __init__(
        self,
        **kwargs
    ):
        """Initialize Main component"""
        super().__init__(tag="main", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', 'min-height: 400px; padding: 20px 0;')
        self.css('litchi-main')


class Aside(HtmlComponent):
    """
    Sidebar component
    """
    
    def __init__(
        self,
        width: str = "250px",
        **kwargs
    ):
        """
        Initialize Aside component
        
        Args:
            width: Sidebar width
            **kwargs: Additional properties
        """
        super().__init__(tag="aside", **kwargs)
        
        # Add default styling
        self._props.setdefault('style', f'width: {width}; padding: 20px; background: #f8f9fa; border-right: 1px solid #eee;')
        self.css('litchi-aside')


# Convenience functions
def VSpace(size: Union[int, str] = "medium", **kwargs) -> Space:
    """Create vertical space"""
    return Space(size=size, direction="vertical", **kwargs)


def HSpace(size: Union[int, str] = "medium", **kwargs) -> Space:
    """Create horizontal space"""
    return Space(size=size, direction="horizontal", **kwargs)


def HDivider(**kwargs) -> Divider:
    """Create horizontal divider"""
    return Divider(direction="horizontal", **kwargs)


def VDivider(**kwargs) -> Divider:
    """Create vertical divider"""
    return Divider(direction="vertical", **kwargs)


def ResponsiveGrid(**kwargs) -> Grid:
    """Create responsive grid"""
    return Grid(
        columns="repeat(auto-fit, minmax(300px, 1fr))",
        gap="20px",
        **kwargs
    )
