"""
State management for Litchi 0.3.1
"""

from typing import Any, Dict, List, Optional, Callable
import copy
import json


class StateManager:
    """
    Minimal but powerful state management for Litchi 0.3.1
    """
    
    def __init__(self):
        """Initialize state manager"""
        self._state: Dict[str, Any] = {}
        self._watchers: Dict[str, List[Callable]] = {}
        self._history: List[Dict[str, Any]] = []
        self._max_history = 50
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get value from state
        
        Args:
            key: State key (supports dot notation like 'user.name')
            default: Default value if key not found
            
        Returns:
            State value
        """
        try:
            keys = key.split('.')
            value = self._state
            
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    return default
            
            return value
        except Exception:
            return default
    
    def set(self, key: str, value: Any) -> None:
        """
        Set value in state
        
        Args:
            key: State key (supports dot notation like 'user.name')
            value: Value to set
        """
        # Save current state to history
        if len(self._history) >= self._max_history:
            self._history.pop(0)
        self._history.append(copy.deepcopy(self._state))
        
        # Set the value
        keys = key.split('.')
        current = self._state
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        old_value = current.get(keys[-1])
        current[keys[-1]] = value
        
        # Notify watchers
        self._notify_watchers(key, value, old_value)
    
    def update(self, updates: Dict[str, Any]) -> None:
        """
        Update multiple state values
        
        Args:
            updates: Dictionary of key-value pairs to update
        """
        for key, value in updates.items():
            self.set(key, value)
    
    def delete(self, key: str) -> bool:
        """
        Delete key from state
        
        Args:
            key: State key to delete
            
        Returns:
            True if key was deleted, False if key didn't exist
        """
        try:
            keys = key.split('.')
            current = self._state
            
            for k in keys[:-1]:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return False
            
            if keys[-1] in current:
                old_value = current[keys[-1]]
                del current[keys[-1]]
                
                # Notify watchers
                self._notify_watchers(key, None, old_value)
                return True
            
            return False
        except Exception:
            return False
    
    def has(self, key: str) -> bool:
        """
        Check if key exists in state
        
        Args:
            key: State key to check
            
        Returns:
            True if key exists
        """
        return self.get(key) is not None
    
    def watch(self, key: str, callback: Callable[[str, Any, Any], None]) -> None:
        """
        Watch for changes to a state key
        
        Args:
            key: State key to watch (supports dot notation)
            callback: Callback function called when value changes
                     Callback signature: (key, new_value, old_value)
        """
        if key not in self._watchers:
            self._watchers[key] = []
        self._watchers[key].append(callback)
    
    def unwatch(self, key: str, callback: Optional[Callable] = None) -> None:
        """
        Remove watcher for a state key
        
        Args:
            key: State key to unwatch
            callback: Specific callback to remove, or None to remove all
        """
        if key in self._watchers:
            if callback is None:
                del self._watchers[key]
            else:
                try:
                    self._watchers[key].remove(callback)
                    if not self._watchers[key]:
                        del self._watchers[key]
                except ValueError:
                    pass
    
    def get_all(self) -> Dict[str, Any]:
        """
        Get all state data
        
        Returns:
            Copy of entire state dictionary
        """
        return copy.deepcopy(self._state)
    
    def clear(self) -> None:
        """Clear all state data"""
        self._state.clear()
        self._history.clear()
        self._watchers.clear()
    
    def undo(self) -> bool:
        """
        Undo last state change
        
        Returns:
            True if undo was successful
        """
        if self._history:
            self._state = self._history.pop()
            return True
        return False
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get state history
        
        Returns:
            List of previous state snapshots
        """
        return copy.deepcopy(self._history)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert state to dictionary
        
        Returns:
            State dictionary
        """
        return self.get_all()
    
    def from_dict(self, data: Dict[str, Any]) -> None:
        """
        Load state from dictionary
        
        Args:
            data: Dictionary to load into state
        """
        self._state = copy.deepcopy(data)
    
    def to_json(self) -> str:
        """
        Convert state to JSON string
        
        Returns:
            JSON representation of state
        """
        return json.dumps(self._state, ensure_ascii=False, indent=2)
    
    def from_json(self, json_str: str) -> None:
        """
        Load state from JSON string
        
        Args:
            json_str: JSON string to load
        """
        try:
            data = json.loads(json_str)
            self.from_dict(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
    
    def _notify_watchers(self, key: str, new_value: Any, old_value: Any) -> None:
        """Notify all watchers of a key"""
        # Notify exact key watchers
        if key in self._watchers:
            for callback in self._watchers[key]:
                try:
                    callback(key, new_value, old_value)
                except Exception as e:
                    print(f"Error in state watcher for key '{key}': {e}")
        
        # Notify parent key watchers (for dot notation)
        key_parts = key.split('.')
        for i in range(len(key_parts) - 1):
            parent_key = '.'.join(key_parts[:i + 1])
            if parent_key in self._watchers:
                parent_value = self.get(parent_key)
                for callback in self._watchers[parent_key]:
                    try:
                        callback(parent_key, parent_value, None)
                    except Exception as e:
                        print(f"Error in state watcher for parent key '{parent_key}': {e}")
    
    def __repr__(self) -> str:
        return f"<StateManager(keys={len(self._state)}, watchers={len(self._watchers)})>"
