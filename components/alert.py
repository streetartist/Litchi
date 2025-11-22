"""
Alert components for Litchi 0.3.1
"""

from typing import Any, Optional
from ..core.component import ElementComponent


class Alert(ElementComponent):
    """
    Alert component based on Element Plus
    """
    
    def __init__(
        self,
        title: str = "",
        type: str = "info",
        description: str = "",
        closable: bool = True,
        center: bool = False,
        show_icon: bool = True,
        effect: str = "light",
        **kwargs
    ):
        """
        Initialize Alert component
        
        Args:
            title: Alert title
            type: Alert type (success, warning, info, error)
            description: Alert description
            closable: Whether alert is closable
            center: Whether to center text
            show_icon: Whether to show icon
            effect: Alert effect (light, dark)
            **kwargs: Additional properties
        """
        super().__init__(
            element="alert",
            **kwargs
        )
        
        # Set alert properties
        self._props.update({
            'title': title,
            'type': type,
            'closable': closable,
            'center': center,
            'show-icon': show_icon,
            'effect': effect
        })
        
        # Add description if provided
        if description:
            self._props['description'] = description
            self.child(description)
        elif title:
            self.child(title)
    
    def set_title(self, title: str) -> 'Alert':
        """Set alert title"""
        self._props['title'] = title
        return self
    
    def set_type(self, type: str) -> 'Alert':
        """Set alert type"""
        self._props['type'] = type
        return self
    
    def set_description(self, description: str) -> 'Alert':
        """Set alert description"""
        self._props['description'] = description
        return self
    
    def set_closable(self, closable: bool) -> 'Alert':
        """Set whether alert is closable"""
        self._props['closable'] = closable
        return self
    
    def set_center(self, center: bool) -> 'Alert':
        """Set whether to center text"""
        self._props['center'] = center
        return self
    
    def set_show_icon(self, show_icon: bool) -> 'Alert':
        """Set whether to show icon"""
        self._props['show-icon'] = show_icon
        return self
    
    def set_effect(self, effect: str) -> 'Alert':
        """Set alert effect"""
        self._props['effect'] = effect
        return self


# Convenience functions for creating different types of alerts
def SuccessAlert(title: str = "Success", description: str = "", **kwargs) -> Alert:
    """Create a success alert"""
    return Alert(title, type="success", description=description, **kwargs)


def WarningAlert(title: str = "Warning", description: str = "", **kwargs) -> Alert:
    """Create a warning alert"""
    return Alert(title, type="warning", description=description, **kwargs)


def InfoAlert(title: str = "Info", description: str = "", **kwargs) -> Alert:
    """Create an info alert"""
    return Alert(title, type="info", description=description, **kwargs)


def ErrorAlert(title: str = "Error", description: str = "", **kwargs) -> Alert:
    """Create an error alert"""
    return Alert(title, type="error", description=description, **kwargs)


def SimpleAlert(message: str, type: str = "info", **kwargs) -> Alert:
    """Create a simple alert with just a message"""
    return Alert(message, type=type, **kwargs)


def CenteredAlert(title: str, description: str = "", type: str = "info", **kwargs) -> Alert:
    """Create a centered alert"""
    return Alert(title, type=type, description=description, center=True, **kwargs)


def DarkAlert(title: str, description: str = "", type: str = "info", **kwargs) -> Alert:
    """Create a dark effect alert"""
    return Alert(title, type=type, description=description, effect="dark", **kwargs)


def NonClosableAlert(title: str, description: str = "", type: str = "info", **kwargs) -> Alert:
    """Create a non-closable alert"""
    return Alert(title, type=type, description=description, closable=False, **kwargs)


def NoIconAlert(title: str, description: str = "", type: str = "info", **kwargs) -> Alert:
    """Create an alert without icon"""
    return Alert(title, type=type, description=description, show_icon=False, **kwargs)


def NotificationAlert(title: str, message: str, type: str = "info", **kwargs) -> Alert:
    """Create a notification-style alert"""
    return Alert(
        title=title,
        description=message,
        type=type,
        center=True,
        show_icon=True,
        **kwargs
    )


def StatusAlert(status: str, message: str, **kwargs) -> Alert:
    """
    Create a status-based alert
    
    Args:
        status: Status (success, error, warning, info)
        message: Message to display
        **kwargs: Additional properties
    """
    status_map = {
        'success': ('success', 'Success'),
        'error': ('error', 'Error'),
        'warning': ('warning', 'Warning'),
        'info': ('info', 'Info'),
        'ok': ('success', 'OK'),
        'fail': ('error', 'Failed'),
        'complete': ('success', 'Complete'),
        'pending': ('warning', 'Pending')
    }
    
    alert_type, default_title = status_map.get(status.lower(), ('info', 'Info'))
    
    return Alert(
        title=default_title,
        description=message,
        type=alert_type,
        **kwargs
    )
