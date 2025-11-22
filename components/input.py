"""
Input components for Litchi 0.3.1
"""

from typing import Any, List, Optional, Union
from ..core.component import ElementComponent


class Input(ElementComponent):
    """
    Input component based on Element Plus
    """
    
    def __init__(
        self,
        placeholder: str = "",
        type: str = "text",
        value: str = "",
        size: str = "default",
        disabled: bool = False,
        readonly: bool = False,
        clearable: bool = False,
        show_password: bool = False,
        prefix_icon: Optional[str] = None,
        suffix_icon: Optional[str] = None,
        maxlength: Optional[int] = None,
        minlength: Optional[int] = None,
        **kwargs
    ):
        """
        Initialize Input component
        
        Args:
            placeholder: Input placeholder text
            type: Input type (text, password, number, email, url, tel, textarea)
            value: Input value
            size: Input size (large, default, small)
            disabled: Whether input is disabled
            readonly: Whether input is readonly
            clearable: Whether input can be cleared
            show_password: Whether to show password toggle
            prefix_icon: Prefix icon name
            suffix_icon: Suffix icon name
            maxlength: Maximum length
            minlength: Minimum length
            **kwargs: Additional properties
        """
        super().__init__(
            element="input",
            **kwargs
        )
        
        # Set input properties
        props = {
            'type': type,
            'size': size,
            'disabled': disabled,
            'readonly': readonly,
            'clearable': clearable,
            'show-password': show_password
        }
        
        if placeholder:
            props['placeholder'] = placeholder
        
        if value:
            props['modelValue'] = value
        
        if prefix_icon:
            props['prefix-icon'] = prefix_icon
        
        if suffix_icon:
            props['suffix-icon'] = suffix_icon
        
        if maxlength is not None:
            props['maxlength'] = maxlength
        
        if minlength is not None:
            props['minlength'] = minlength
        
        self._props.update(props)
    
    def set_value(self, value: str) -> 'Input':
        """Set input value"""
        self._props['modelValue'] = value
        return self
    
    def get_value(self) -> str:
        """Get input value"""
        return self._props.get('modelValue', '')
    
    def clear(self) -> 'Input':
        """Clear input value"""
        self._props['modelValue'] = ""
        return self
    
    def disable(self) -> 'Input':
        """Disable input"""
        self._props['disabled'] = True
        return self
    
    def enable(self) -> 'Input':
        """Enable input"""
        self._props['disabled'] = False
        return self


class Textarea(ElementComponent):
    """
    Textarea component based on Element Plus
    """
    
    def __init__(
        self,
        placeholder: str = "",
        value: str = "",
        rows: int = 2,
        autosize: Union[bool, dict] = False,
        disabled: bool = False,
        readonly: bool = False,
        resize: str = "vertical",
        maxlength: Optional[int] = None,
        minlength: Optional[int] = None,
        show_word_limit: bool = False,
        **kwargs
    ):
        """
        Initialize Textarea component
        
        Args:
            placeholder: Textarea placeholder text
            value: Textarea value
            rows: Number of rows
            autosize: Whether to auto resize height (True/False or {minRows: 2, maxRows: 6})
            disabled: Whether textarea is disabled
            readonly: Whether textarea is readonly
            resize: Resize direction (vertical, horizontal, both, none)
            maxlength: Maximum length
            minlength: Minimum length
            show_word_limit: Whether to show word count
            **kwargs: Additional properties
        """
        super().__init__(
            element="input",
            **kwargs
        )
        
        # Set textarea properties
        props = {
            'type': 'textarea',
            'rows': rows,
            'disabled': disabled,
            'readonly': readonly,
            'resize': resize,
            'show-word-limit': show_word_limit
        }
        
        if placeholder:
            props['placeholder'] = placeholder
        
        if value:
            props['modelValue'] = value
        
        if autosize:
            if isinstance(autosize, dict):
                props['autosize'] = autosize
            else:
                props['autosize'] = True
        
        if maxlength is not None:
            props['maxlength'] = maxlength
        
        if minlength is not None:
            props['minlength'] = minlength
        
        self._props.update(props)
    
    def set_value(self, value: str) -> 'Textarea':
        """Set textarea value"""
        self._props['modelValue'] = value
        return self
    
    def get_value(self) -> str:
        """Get textarea value"""
        return self._props.get('modelValue', '')
    
    def clear(self) -> 'Textarea':
        """Clear textarea value"""
        self._props['modelValue'] = ""
        return self
    
    def disable(self) -> 'Textarea':
        """Disable textarea"""
        self._props['disabled'] = True
        return self
    
    def enable(self) -> 'Textarea':
        """Enable textarea"""
        self._props['disabled'] = False
        return self
    
    def set_rows(self, rows: int) -> 'Textarea':
        """Set number of rows"""
        self._props['rows'] = rows
        return self


# Convenience functions for creating common input types
def TextInput(placeholder: str = "Enter text", **kwargs) -> Input:
    """Create a text input"""
    return Input(placeholder=placeholder, type="text", **kwargs)


def PasswordInput(placeholder: str = "Enter password", **kwargs) -> Input:
    """Create a password input"""
    return Input(placeholder=placeholder, type="password", show_password=True, **kwargs)


def NumberInput(placeholder: str = "Enter number", **kwargs) -> Input:
    """Create a number input"""
    return Input(placeholder=placeholder, type="number", **kwargs)


