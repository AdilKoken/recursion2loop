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


def inorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative inorder traversal of a binary tree.
    Inorder traversal visits nodes in the order: left subtree, root, right subtree.
    This is commonly used to visit binary tree nodes in ascending order.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in inorder traversal order
    """
    if not root:
        return []
    
    validate_tree_node(root)
    
    stack = []
    result = []
    
    while root or stack:
        # Traverse to leftmost node
        while root:
            stack.append(root)
            root = root.left

        # Process current node and move to right subtree
        root = stack.pop()
        result.append(root.value)
        root = root.right

    return result


def preorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative preorder traversal of a binary tree.
    Preorder traversal visits nodes in the order: root, left subtree, right subtree.
    This traversal is useful for creating a copy of the tree or serializing tree structure.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in preorder traversal order
    """
    if not root:
        return []
    
    stack = [root]
    result = []

    while stack:
        # Process current node
        node = stack.pop()
        result.append(node.value)
        
        # Push right child first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder_tree_traversal(root: Optional[TreeNode]) -> list[T]:
    """
    Performs an iterative postorder traversal of a binary tree.
    Postorder traversal visits nodes in the order: left subtree, right subtree, root.
    This is useful when deleting nodes or evaluating mathematical expressions.

    Args:
        root: Root node of the binary tree

    Returns:
        List of node values in postorder traversal order
    """
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        # Modified preorder traversal (root, right, left)
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reverse to get postorder (left, right, root)
    return result[::-1]