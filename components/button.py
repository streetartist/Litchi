"""
Button components for Litchi 0.3.1
"""

from typing import Any, List, Optional, Union
from ..core.component import ElementComponent


class Button(ElementComponent):
    """
    Button component based on Element Plus
    """
    
    def __init__(
        self,
        text: str = "Button",
        type: str = "default",
        size: str = "default",
        disabled: bool = False,
        loading: bool = False,
        plain: bool = False,
        round: bool = False,
        circle: bool = False,
        icon: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize Button component
        
        Args:
            text: Button text
            type: Button type (primary, success, warning, danger, info, text, default)
            size: Button size (large, default, small)
            disabled: Whether button is disabled
            loading: Whether button is in loading state
            plain: Whether button is plain
            round: Whether button is round
            circle: Whether button is circle
            icon: Icon name
            **kwargs: Additional properties
        """
        super().__init__(
            element="button",
            **kwargs
        )
        
        # Set button properties
        self._props.update({
            'type': type,
            'size': size,
            'disabled': disabled,
            'loading': loading,
            'plain': plain,
            'round': round,
            'circle': circle
        })
        
        if icon:
            self._props['icon'] = icon
        
        # Add text as child
        if text:
            self.child(text)


class ButtonGroup(ElementComponent):
    """
    Button group component
    """
    
    def __init__(
        self,
        *buttons,
        **kwargs
    ):
        """
        Initialize ButtonGroup component
        
        Args:
            *buttons: Button components to group
            **kwargs: Additional properties
        """
        super().__init__(
            element="button-group",
            **kwargs
        )
        
        # Add buttons as children
        for button in buttons:
            if button is not None:
                self.child(button)
    


# Convenience functions for creating common button types
def PrimaryButton(text: str = "Primary", **kwargs) -> Button:
    """Create a primary button"""
    return Button(text, type="primary", **kwargs)


def SuccessButton(text: str = "Success", **kwargs) -> Button:
    """Create a success button"""
    return Button(text, type="success", **kwargs)


def WarningButton(text: str = "Warning", **kwargs) -> Button:
    """Create a warning button"""
    return Button(text, type="warning", **kwargs)


def DangerButton(text: str = "Danger", **kwargs) -> Button:
    """Create a danger button"""
    return Button(text, type="danger", **kwargs)


def InfoButton(text: str = "Info", **kwargs) -> Button:
    """Create an info button"""
    return Button(text, type="info", **kwargs)


def TextButton(text: str = "Text", **kwargs) -> Button:
    """Create a text button"""
    return Button(text, type="text", **kwargs)


def LargeButton(text: str = "Large", **kwargs) -> Button:
    """Create a large button"""
    return Button(text, size="large", **kwargs)


def SmallButton(text: str = "Small", **kwargs) -> Button:
    """Create a small button"""
    return Button(text, size="small", **kwargs)


def IconButton(icon: str, **kwargs) -> Button:
    """Create an icon button"""
    return Button("", icon=icon, circle=True, **kwargs)


def LoadingButton(text: str = "Loading", **kwargs) -> Button:
    """Create a loading button"""
    return Button(text, loading=True, **kwargs)
