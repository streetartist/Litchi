"""
Hello World example for Litchi 0.3.1
"""

import sys
import os

# Add the parent directory to the path so we can import litchi3
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from litchi import App
from litchi.components import Button, Title, Card, Space, Alert, Row, Col


class HelloWorldApp(App):
    """Simple Hello World application demonstrating Litchi 0.3.1"""
    
    def __init__(self):
        super().__init__(name="Litchi 0.3.1 Hello World", debug=True)
        
        # Initialize some state
        self.state.set('click_count', 0)
        self.state.set('message', 'Welcome to Litchi 0.3.1!')
        self.state.set('show_alert', False)
    
    def on_click(self):
        """Handle button click"""
        count = self.state.get('click_count', 0)
        count += 1
        self.state.set('click_count', count)
        
        return self.notify(
            "Button Clicked",
            f"You've clicked the button {count} times!",
            type="success"
        )
    
    def on_reset(self):
        """Reset counter"""
        self.state.set('click_count', 0)
        return self.success("Counter reset successfully!")
    
    def on_show_alert(self):
        """Show alert"""
        self.state.set('show_alert', True)
        return self.data({
            'notification': {
                'title': 'Alert Shown',
                'message': 'This is a test alert from Litchi 0.3.1!',
                'type': 'info'
            }
        })
    
    def build(self):
        """Build the UI"""
        return [
            # Header
            Title("Welcome to Litchi 0.3.1", level=1),
            
            # Main content in a card
            Card(
                Title("Hello World Demo", level=3),
                
                # Alert section
                Alert(
                    title="Welcome!",
                    description="This is a demonstration of Litchi 0.3.1 - a minimal but powerful Python web framework.",
                    type="info",
                    show_icon=True,
                    closable=True
                ),
                
                # Button section
                Space(size="large").child(
                    Button(
                        f"Click Me ({self.state.get('click_count', 0)})",
                        type="primary",
                        size="default",
                        on_click=self.on_click
                    ),
                    Button("Reset", type="default", size="default", on_click=self.on_reset),
                    Button("Show Alert", type="success", size="default", on_click=self.on_show_alert)
                ),
                
                # Grid layout demo
                Row(gutter=20).child(
                    Col(span=8).child(
                        Card(
                            Title("Feature 1", level=4),
                            "Litchi 0.3.1 provides a clean, minimal API for building web applications.",
                            shadow="hover"
                        )
                    ),
                    Col(span=8).child(
                        Card(
                            Title("Feature 2", level=4),
                            "Built with Vue.js 3 and Element Plus for modern UI components.",
                            shadow="hover"
                        )
                    ),
                    Col(span=8).child(
                        Card(
                            Title("Feature 3", level=4),
                            "State management and event handling made simple.",
                            shadow="hover"
                        )
                    )
                ),
                
                header="Litchi 0.3.1 Demo",
                shadow="hover"
            )
        ]


if __name__ == '__main__':
    app = HelloWorldApp()
    app.run(port=5000)
