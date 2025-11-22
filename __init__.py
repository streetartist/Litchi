"""
Litchi 0.3.1 - Minimal Modern Python Web Framework

A minimal but powerful Python web framework that combines the best of Litchi 1.0 and 2.0.
Built with Vue.js 3 + Element Plus for modern UI development.
"""

from .core.app import App
from .core.component import Component, ElementComponent, HtmlComponent
from .components import *

__version__ = "3.0.0"
__author__ = "Litchi Team"

# Export main classes
__all__ = [
    'App',
    'Component', 
    'ElementComponent',
    'HtmlComponent',
    # Components
    'Button', 'Input', 'Text', 'Title', 'Card', 'Layout',
    'Row', 'Col', 'Space', 'Divider'
]
