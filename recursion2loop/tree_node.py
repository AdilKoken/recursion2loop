from typing import TypeVar, Optional, Any
from dataclasses import dataclass

# enforces consistency of tree root and node values
T = TypeVar('T')

@dataclass
class TreeNode:
    value: T
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

def validate_tree_node(node: Any):
    """Validate that a node implements the minimum tree node interface.
    
    Args:
        node: Any object to check as a tree node

    Raises:
        AttributeError: If the node does not have the required attributes
    """
    if node is not None:
        if not hasattr(node, 'value'):
            raise AttributeError("Node must have a 'value' attribute")
        if not hasattr(node, 'left'):
            raise AttributeError("Node must have a 'left' attribute")
        if not hasattr(node, 'right'):
            raise AttributeError("Node must have a 'right' attribute") 