from typing import Optional
from .tree_node import TreeNode, validate_tree_node, T
from .tree_traversal import level_order_tree_traversal

# Now you can add your tree operations here
# For example:

def get_tree_height(root: Optional[TreeNode]) -> int:
    """
    Calculate the height of the binary tree.

    The height of a binary tree is defines as the maximum depth of any leaf node in the tree.
    depth is defined as the number of edges on the path from the root to the node.
    The height of an empty tree is 0.

    Args:
        root: Root node of the binary tree.
        
    Returns:
        Height of the tree (0 for an empty tree).
    """
    if not root:
        return 0
    
    validate_tree_node(root)
    stack = [(root, 0)]  # Each element is a tuple of (node, current_depth)
    max_height = 0
    
    while stack:
        node, depth = stack.pop()
        max_height = max(max_height, depth)
        
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
            
    return max_height

def serialize_tree(root: Optional[TreeNode]) -> str:
    """
    Serialize the binary tree into a list for later deserialization.

    Serialization converts the tree structure into a linear format (list) using 
    level order traversal (breadth-first traversal).

    Args:
        root: Root node of the binary tree.
        
    Returns:
        A list of node values representing the serialized binary tree.
        Returns an empty list if the tree is empty.
    """
    
    # The level_order_tree_traversal function handles validation and traversal
    return level_order_tree_traversal(root)

def deserialize_tree(data: list[T]) -> Optional[TreeNode]:
    """
    Deserialize a list back into a binary tree structure.

    Args:
        data: A list of node values produced by the serialize_tree function.
        
    Returns:
        The root node of the reconstructed binary tree.
        Returns None if the input list is empty.
    """
    if not data:
        return None
    
    validate_tree_node(data)

    root = TreeNode(data[0])
    queue = [root]  # Queue to hold nodes whose children are to be assigned
    index = 1  # Index to track the position in the data list
    
    while queue:
        node = queue.pop(0)
        
        # Assign left child if available
        if index < len(data):
            node.left = TreeNode(data[index])
            queue.append(node.left)
            index += 1
        
        # Assign right child if available
        if index < len(data):
            node.right = TreeNode(data[index])
            queue.append(node.right)
            index += 1

    return root

